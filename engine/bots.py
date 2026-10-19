"""SignalBot: a reusable base for "scan a list of symbols, enter on a signal, exit on a rule" bots.

Subclass it and implement:
    entry(ctx, sym, df) -> None | ("long"|"short", reason) | ("long"|"short", reason, stop_price)
    exit(ctx, sym, df, qty) -> None | reason        (optional; stops/targets are automatic)
"""
from __future__ import annotations

from . import ta
from .strategy import Strategy

# Liquid NIFTY 50 names that fit a ₹50k account (all under ~₹4k/share).
NIFTY_LIQUID = [
    "NSE:RELIANCE", "NSE:HDFCBANK", "NSE:ICICIBANK", "NSE:INFY", "NSE:TCS", "NSE:SBIN",
    "NSE:AXISBANK", "NSE:KOTAKBANK", "NSE:LT", "NSE:BHARTIARTL", "NSE:ITC", "NSE:SUNPHARMA",
]


NIFTY50 = [
    "NSE:ADANIENT", "NSE:ADANIPORTS", "NSE:APOLLOHOSP", "NSE:ASIANPAINT", "NSE:AXISBANK", "NSE:BAJAJFINSV",
    "NSE:BAJAJ_AUTO", "NSE:BAJFINANCE", "NSE:BEL", "NSE:BHARTIARTL", "NSE:CIPLA", "NSE:COALINDIA",
    "NSE:DRREDDY", "NSE:EICHERMOT", "NSE:ETERNAL", "NSE:GRASIM", "NSE:HCLTECH", "NSE:HDFCBANK", "NSE:HDFCLIFE",
    "NSE:HINDALCO", "NSE:HINDUNILVR", "NSE:ICICIBANK", "NSE:INDIGO", "NSE:INFY", "NSE:ITC", "NSE:JIOFIN",
    "NSE:JSWSTEEL", "NSE:KOTAKBANK", "NSE:LT", "NSE:M&M", "NSE:MARUTI", "NSE:MAXHEALTH", "NSE:NESTLEIND",
    "NSE:NTPC", "NSE:ONGC", "NSE:POWERGRID", "NSE:RELIANCE", "NSE:SBILIFE", "NSE:SBIN", "NSE:SHRIRAMFIN",
    "NSE:SUNPHARMA", "NSE:TATACONSUM", "NSE:TATASTEEL", "NSE:TCS", "NSE:TECHM", "NSE:TITAN", "NSE:TMPV",
    "NSE:TRENT", "NSE:ULTRACEMCO", "NSE:BSE",
]  # constituents as of Oct 2026 (backtests on this list carry survivorship bias)


def nifty_bullish(ctx) -> bool:
    """True when NIFTY closed above its 20-day EMA on the last completed trading day."""
    idx = ctx.data("NSE:NIFTY", "1D", 60, closed_only=True)
    if not ctx.backtest and len(idx) and str(idx.index[-1].tz_convert("Asia/Kolkata").date()) == ctx.today:
        idx = idx.iloc[:-1]  # live: ignore today's forming daily bar
    return bool(idx.close.iloc[-1] > ta.ema(idx.close, 20).iloc[-1])


class SignalBot(Strategy):
    symbols = NIFTY_LIQUID
    capital = 50_000
    bars = 250
    min_bars = 60
    max_positions = 3
    alloc_pct = 33             # % of equity per position
    sl_atr: float | None = None  # stop = entry -/+ sl_atr * ATR   (if entry() gives no stop)
    tp_atr: float | None = None
    rr: float | None = None      # target = entry +/- rr * risk   (risk from the stop)
    sl_pct: float | None = None
    tp_pct: float | None = None
    trail_pct: float | None = None
    no_entry_after: str | None = None  # e.g. "14:45" for intraday bots
    no_entry_before: str | None = None
    regime: str | None = None    # "nifty_trend": longs only if NIFTY closed above its 20-day EMA
                                 # yesterday, shorts only if below
    max_entries_per_day: int | None = None
    stop_mult: float = 1.0       # widen (2.0) or tighten (0.5) the stop; the target is not changed

    def entry(self, ctx, sym, df):
        return None

    def exit(self, ctx, sym, df, qty):
        return None

    def on_bar(self, ctx):
        entries_ok = not ((self.no_entry_after and ctx.local_time > self.no_entry_after) or
                          (self.no_entry_before and ctx.local_time < self.no_entry_before))
        trend = self._regime(ctx) if self.regime else None
        for sym in self.symbols:
            df = ctx.data(sym, bars=self.bars)
            if len(df) < self.min_bars:
                continue
            qty = ctx.position(sym)
            if qty:
                why = self.exit(ctx, sym, df, qty)
                if why:
                    ctx.close(sym, reason=why)
                continue
            if not entries_ok or len(ctx.positions()) >= self.max_positions:
                continue
            if self.max_entries_per_day and self._entries_today(ctx) >= self.max_entries_per_day:
                continue
            sig = self.entry(ctx, sym, df)
            if not sig:
                continue
            side, why = sig[0], sig[1]
            if trend is not None and (side == "long") != trend:
                continue  # against the market regime
            if side == "short" and not self.allow_short:
                continue
            if self.max_entries_per_day:
                ctx.memory["entries"] = [ctx.today, self._entries_today(ctx) + 1]
            stop = sig[2] if len(sig) > 2 else None
            px = float(df.close.iloc[-1])
            long = side == "long"
            if stop is None and self.sl_atr:
                a = float(ta.atr(df, 14).iloc[-1])
                stop = px - self.sl_atr * a if long else px + self.sl_atr * a
            tp = None
            if self.rr and stop is not None:
                tp = px + self.rr * (px - stop) if long else px - self.rr * (stop - px)
            elif self.tp_atr:
                a = float(ta.atr(df, 14).iloc[-1])
                tp = px + self.tp_atr * a if long else px - self.tp_atr * a
            sl_pct = None if stop else self.sl_pct
            if self.stop_mult != 1.0:
                if stop is not None:
                    stop = px - (px - stop) * self.stop_mult
                if sl_pct:
                    sl_pct *= self.stop_mult
            kw = dict(pct=self.alloc_pct, sl=stop, tp=tp, sl_pct=sl_pct,
                      tp_pct=None if tp else self.tp_pct, trail_pct=self.trail_pct, reason=why)
            if long:
                ctx.buy(sym, **kw)
            elif self.allow_short:
                ctx.sell(sym, **kw)

    def _regime(self, ctx) -> bool:
        return nifty_bullish(ctx)

    def _entries_today(self, ctx) -> int:
        e = ctx.memory.get("entries")
        return e[1] if e and e[0] == ctx.today else 0

    # helpers for "once per symbol per day" rules
    def traded_today(self, ctx, sym) -> bool:
        return ctx.memory.get("day") == ctx.today and sym in ctx.memory.get("traded", [])

    def mark_traded(self, ctx, sym):
        if ctx.memory.get("day") != ctx.today:
            ctx.memory["day"], ctx.memory["traded"] = ctx.today, []
        ctx.memory["traded"].append(sym)
