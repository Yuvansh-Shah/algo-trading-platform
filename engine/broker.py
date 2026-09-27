"""Paper broker (default) + optional live order forwarding.

Every strategy gets its own paper portfolio, so you can compare bots side by side.
Signed quantities: +qty = long, -qty = short.
"""
from __future__ import annotations

import json
import math
import os
from dataclasses import asdict, dataclass, field

import requests


@dataclass
class Portfolio:
    strategy: str
    initial: float
    cash: float
    positions: dict = field(default_factory=dict)  # sym -> {qty, avg, sl, tp, trail_pct, opened}
    realized: float = 0.0
    fees: float = 0.0
    trades: int = 0
    wins: int = 0
    losses: int = 0
    memory: dict = field(default_factory=dict)  # strategy's own persistent scratchpad

    def equity(self, prices: dict[str, float]) -> float:
        return self.cash + sum(p["qty"] * prices.get(s, p["avg"]) for s, p in self.positions.items())

    def to_json(self) -> dict:
        return asdict(self)

    @classmethod
    def from_json(cls, d: dict) -> "Portfolio":
        return cls(**d)


class PaperBroker:
    def __init__(self, pf: Portfolio, fees_pct: float = 0.05, slippage_pct: float = 0.02,
                 allow_short: bool = False, trade_log: list | None = None, live=None):
        self.pf = pf
        self.fees = fees_pct / 100
        self.slip = slippage_pct / 100
        self.allow_short = allow_short
        self.log = trade_log if trade_log is not None else []
        self.live = live  # optional LiveForwarder

    def position(self, sym: str) -> float:
        return self.pf.positions.get(sym, {}).get("qty", 0)

    def order(self, sym: str, delta: float, price: float, when: str, reason: str = "",
              sl: float | None = None, tp: float | None = None, trail_pct: float | None = None) -> dict | None:
        if not delta or not price or math.isnan(price):
            return None
        pos = self.pf.positions.get(sym)
        q = pos["qty"] if pos else 0
        new_q = q + delta
        if new_q < 0 and not self.allow_short:
            delta, new_q = -q, 0  # clamp: can only sell what we hold
            if not delta:
                return None
        fill = price * (1 + self.slip) if delta > 0 else price * (1 - self.slip)
        # opening/increasing exposure must be affordable (shorts need cash as margin)
        opening = abs(new_q) > abs(q) and (q == 0 or (q > 0) == (new_q > 0))
        if opening:
            add = abs(new_q) - abs(q)
            max_add = max(self.pf.cash, 0) / (fill * (1 + self.fees))
            max_add = math.floor(max_add) if float(add).is_integer() else math.floor(max_add * 1e6) / 1e6
            if add > max_add:
                add = max_add
                delta = add if delta > 0 else -add
                new_q = q + delta
            if not delta:
                return None
        fee = abs(delta) * fill * self.fees
        pnl = 0.0
        if q and (q > 0) != (delta > 0):  # reducing / flipping
            closed = min(abs(delta), abs(q))
            pnl = closed * (fill - pos["avg"]) * (1 if q > 0 else -1)
            self.pf.realized += pnl
            if pnl - fee >= 0:
                self.pf.wins += 1
            else:
                self.pf.losses += 1
        self.pf.cash -= delta * fill + fee
        self.pf.fees += fee
        self.pf.trades += 1

        if new_q == 0:
            self.pf.positions.pop(sym, None)
        elif q == 0 or (q > 0) != (new_q > 0):  # fresh position (or flipped)
            self.pf.positions[sym] = {"qty": new_q, "avg": fill, "sl": sl, "tp": tp,
                                      "trail_pct": trail_pct, "opened": when}
        else:
            p = self.pf.positions[sym]
            if abs(new_q) > abs(q):
                p["avg"] = (q * p["avg"] + delta * fill) / new_q
            p["qty"] = new_q
            for k, v in (("sl", sl), ("tp", tp), ("trail_pct", trail_pct)):
                if v is not None:
                    p[k] = v

        trade = {"time": when, "strategy": self.pf.strategy, "symbol": sym,
                 "side": "BUY" if delta > 0 else "SELL", "qty": abs(delta), "price": round(fill, 4),
                 "fee": round(fee, 2), "pnl": round(pnl - fee, 2) if pnl else round(-fee, 2),
                 "position_after": new_q, "reason": reason}
        self.log.append(trade)
        if self.live:
            trade["live"] = self.live.forward(trade)
        return trade

    def check_exits(self, prices: dict[str, float], when: str, highs: dict | None = None,
                    lows: dict | None = None) -> list[dict]:
        """Stop-loss / target / trailing-stop management. Uses bar high/low when given (backtests)."""
        done = []
        for sym, p in list(self.pf.positions.items()):
            px = prices.get(sym)
            if px is None:
                continue
            hi = (highs or {}).get(sym, px)
            lo = (lows or {}).get(sym, px)
            long = p["qty"] > 0
            if p.get("trail_pct"):
                t = p["trail_pct"] / 100
                trail = hi * (1 - t) if long else lo * (1 + t)
                if p.get("sl") is None or (long and trail > p["sl"]) or (not long and trail < p["sl"]):
                    p["sl"] = trail
            sl, tp = p.get("sl"), p.get("tp")
            exit_px, why = None, None
            if sl is not None and ((long and lo <= sl) or (not long and hi >= sl)):
                exit_px, why = (min(px, sl) if long else max(px, sl)) if highs else px, "stop-loss"
            elif tp is not None and ((long and hi >= tp) or (not long and lo <= tp)):
                exit_px, why = (tp if highs else px), "target"
            if exit_px:
                t = self.order(sym, -p["qty"], exit_px, when, why)
                if t:
                    done.append(t)
        return done


class LiveForwarder:
    """Forwards paper fills to a real execution endpoint. OFF unless you configure it.

    `webhook`: POSTs every order as JSON to LIVE_WEBHOOK_URL (GitHub secret). Works with any
    bridge that accepts TradingView-style webhook orders (e.g. Dhan / Tradetron / your own
    server). The JSON template can be customised in config.yaml -> live.template.
    """

    def __init__(self, cfg: dict):
        self.cfg = cfg or {}
        self.url = os.environ.get("LIVE_WEBHOOK_URL", "")

    def forward(self, trade: dict) -> str:
        if not self.url:
            return "skipped: LIVE_WEBHOOK_URL not set"
        tmpl = self.cfg.get("template")
        body = json.loads(json.dumps(tmpl)) if tmpl else dict(trade)
        if tmpl:
            body = json.loads(json.dumps(body)
                              .replace("{{symbol}}", trade["symbol"].split(":")[-1])
                              .replace("{{exchange}}", trade["symbol"].split(":")[0])
                              .replace("{{side}}", trade["side"])
                              .replace('"{{qty}}"', str(int(trade["qty"])))
                              .replace('"{{price}}"', str(trade["price"])))
        try:
            r = requests.post(self.url, json=body, timeout=15)
            return f"sent {r.status_code}"
        except Exception as e:
            return f"error: {e}"
