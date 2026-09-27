"""Backtest bots on historical TradingView bars with the exact same code that runs live.

    python -m engine.backtest ema_crossover             # one bot, last 120 days
    python -m engine.backtest ema_crossover --days 180
    python -m engine.backtest --all                     # every bot, same period -> BACKTESTS.md

Orders placed on a bar's close fill at the NEXT bar's open (no look-ahead). Stops/targets
are checked against each bar's high/low. Results -> backtests/<bot>_trades.csv + _equity.csv
"""
from __future__ import annotations

import argparse
import csv
import math
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pandas as pd

from . import markets, tv
from .broker import PaperBroker, Portfolio
from .loader import ROOT, load_strategies
from .strategy import INTERVAL_MIN, Context, NotAvailableInBacktest

WARMUP_BARS = 260


def bars_needed(interval: str, market: str, days: int) -> int:
    mins = INTERVAL_MIN[interval]
    if market == "CRYPTO":
        per_day = 1440 / mins
        trading_days = days
    else:
        s = markets.SESSIONS[market]
        session_min = (s.close.hour * 60 + s.close.minute) - (s.open.hour * 60 + s.open.minute)
        per_day = max(1.0, session_min / mins) if mins < 1440 else 1.0
        trading_days = days * 5 / 7
    if mins >= 1440:
        per_day = 1440 / mins
    return min(5000, int(math.ceil(trading_days * per_day)) + WARMUP_BARS)


class BacktestData:
    def __init__(self, market: str, days: int):
        self.market, self.days = market, days
        self.frames: dict = {}

    def frame(self, symbol, interval):
        key = (symbol, interval)
        if key not in self.frames:
            self.frames[key] = tv.ohlcv(symbol, interval, bars_needed(interval, self.market, self.days))
        return self.frames[key]

    def bars(self, symbol, interval, n, now):
        df = self.frame(symbol, interval)
        cutoff = pd.Timestamp(now) - timedelta(minutes=INTERVAL_MIN[interval])
        i = df.index.searchsorted(cutoff, side="right")
        return df.iloc[max(0, i - n):i]

    def price(self, symbol, now):
        for iv in sorted((iv for s, iv in self.frames if s == symbol), key=INTERVAL_MIN.get):
            b = self.bars(symbol, iv, 1, now)
            if len(b):
                return float(b.close.iloc[-1])
        return float("nan")


def run(name: str, days: int = 120, capital: float | None = None, fees_pct=0.05, slippage_pct=0.02,
        quiet=True) -> dict:
    strategies, errors = load_strategies([name])
    if not strategies:
        raise SystemExit(f"bot {name!r} not found. {errors}")
    s = strategies[0]
    base = {"bot": s.name, "style": s.style, "interval": s.interval}
    if not s.symbols:
        return {**base, "status": "live-only (uses the live screener)"}
    market = s.market or markets.market_of_symbol(s.symbols[0])
    data = BacktestData(market, days)
    step = timedelta(minutes=INTERVAL_MIN[s.interval])
    for sym in s.symbols:
        data.frame(sym, s.interval)
    timeline = data.frame(s.symbols[0], s.interval).index
    start = pd.Timestamp(datetime.now(timezone.utc) - timedelta(days=days))
    first = max(int(timeline.searchsorted(start)), 30)
    pf = Portfolio(s.name, capital or s.capital, capital or s.capital)
    trades: list[dict] = []
    broker = PaperBroker(pf, fees_pct, slippage_pct, s.allow_short, trades)
    pending: list[tuple] = []
    curve = []

    def executor(symbol, delta, reason, sl, tp, trail):
        pending.append((symbol, delta, reason, sl, tp, trail))

    ctx = Context(s, broker, market, data_provider=data, executor=executor,
                  logger=(lambda *a: None) if quiet else print)
    frames = {sym: data.frame(sym, s.interval) for sym in s.symbols}
    try:
        s.on_start(ctx)
        for i in range(first, len(timeline)):
            t = timeline[i]
            when = t.isoformat()
            row = {sym: df.loc[t] for sym, df in frames.items() if t in df.index}
            for sym, delta, reason, sl, tp, trail in pending:  # fill last bar's orders at this open
                px = row[sym].open if sym in row else data.price(sym, t)
                if delta < 0 and broker.position(sym) <= 0 and not s.allow_short:
                    continue
                broker.order(sym, delta, float(px), when, reason, sl, tp, trail)
            pending.clear()
            if pf.positions:
                broker.check_exits({k: float(v.open) for k, v in row.items()}, when,
                                   {k: float(v.high) for k, v in row.items()},
                                   {k: float(v.low) for k, v in row.items()})
            ctx._clock = (t + step).to_pydatetime()
            if s.intraday and not markets.SESSIONS[market].always_open and \
                    markets.minutes_to_close(market, ctx._clock) <= s.square_off_minutes:
                for sym, p in list(pf.positions.items()):
                    px = float(row[sym].close) if sym in row else data.price(sym, t)
                    broker.order(sym, -p["qty"], px, when, "intraday square-off")
            else:
                s.on_bar(ctx)
            curve.append((t, pf.equity({k: float(v.close) for k, v in row.items()})))
    except NotAvailableInBacktest as e:
        return {**base, "status": f"live-only ({e})"}

    eq = pd.Series([v for _, v in curve], index=[t for t, _ in curve])
    closes = [t["pnl"] for t in trades if t.get("kind") == "close"]
    wins, losses = [p for p in closes if p > 0], [-p for p in closes if p <= 0]
    ist = ZoneInfo("Asia/Kolkata")
    stats = {
        **base, "status": "ok", "symbols": len(s.symbols),
        "from": timeline[first].tz_convert(ist).strftime("%d %b %Y"),
        "to": timeline[-1].tz_convert(ist).strftime("%d %b %Y"),
        "start_equity": round(pf.initial), "end_equity": round(eq.iloc[-1]),
        "return_pct": round((eq.iloc[-1] / pf.initial - 1) * 100, 2),
        "max_drawdown_pct": round((eq / eq.cummax() - 1).min() * 100, 2),
        "closed_trades": len(closes),
        "win_rate_pct": round(100 * len(wins) / len(closes), 1) if closes else None,
        "profit_factor": round(sum(wins) / sum(losses), 2) if losses and sum(losses) else None,
        "avg_trade": round(sum(closes) / len(closes)) if closes else None,
        "fees_paid": round(pf.fees),
    }
    out = ROOT / "backtests"
    out.mkdir(exist_ok=True)
    if trades:
        with (out / f"{s.name}_trades.csv").open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(trades[0].keys()))
            w.writeheader()
            w.writerows(trades)
    eq.rename("equity").to_csv(out / f"{s.name}_equity.csv")
    return stats


def write_board(results: list[dict], days: int):
    ok = sorted([r for r in results if r["status"] == "ok"], key=lambda r: r["return_pct"], reverse=True)
    other = [r for r in results if r["status"].startswith("live-only")]
    failed = [r for r in results if r["status"].startswith("error")]
    medals = {1: "🥇", 2: "🥈", 3: "🥉"}
    f = lambda v, suf="": "–" if v is None else f"{v}{suf}"
    L = ["# Backtest leaderboard", "",
         f"_Last {days} days of TradingView data · ₹50,000 per bot · fees {0.05}% + slippage {0.02}% per side · "
         f"generated {datetime.now(ZoneInfo('Asia/Kolkata')).strftime('%d %b %Y %H:%M IST')}_", "",
         "Past performance on a few months of data says little about the future — this is a sanity check, "
         "the live paper leaderboard in STATUS.md is the real test.", "",
         "| # | Bot | Style | Period | Return | Max DD | Trades | Win % | Profit factor | Avg trade | Fees |",
         "|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    for i, r in enumerate(ok, 1):
        L.append(f"| {medals.get(i, i)} | **{r['bot']}** | {r['style']} {r['interval']} | {r['from']} → {r['to']} | "
                 f"{r['return_pct']:+.2f}% | {r['max_drawdown_pct']:.1f}% | {r['closed_trades']} | "
                 f"{f(r['win_rate_pct'])} | {f(r['profit_factor'])} | {f(r['avg_trade'])} | {r['fees_paid']:,} |")
    if other:
        L += ["", "**Not backtestable** (they use live TradingView snapshots — ratings/screener — which have no history):", ""]
        L += [f"- {r['bot']} — {r['status']}" for r in other]
    (ROOT / "BACKTESTS.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    return L


def main():
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("bot", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--days", type=int, default=120)
    ap.add_argument("--capital", type=float)
    a = ap.parse_args()
    if a.all:
        results = []
        for s in load_strategies()[0]:
            try:
                r = run(s.name, a.days, a.capital)
            except Exception as e:
                r = {"bot": s.name, "style": s.style, "interval": s.interval, "status": f"error: {e}"}
            print(f"{r['bot']:<22} {r.get('return_pct', r['status'])}")
            results.append(r)
        print("\n".join(write_board(results, a.days)))
        return
    if not a.bot:
        ap.error("give a bot name or --all")
    stats = run(a.bot, a.days, a.capital)
    w = max(map(len, stats))
    print("\n".join(f"{k.ljust(w)}  {v}" for k, v in stats.items()))


if __name__ == "__main__":
    main()
