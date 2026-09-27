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

    def entry(self, ctx, sym, df):
        return None

    def exit(self, ctx, sym, df, qty):
        return None

    def on_bar(self, ctx):
        entries_ok = not ((self.no_entry_after and ctx.local_time > self.no_entry_after) or
                          (self.no_entry_before and ctx.local_time < self.no_entry_before))
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
            sig = self.entry(ctx, sym, df)
            if not sig:
                continue
            side, why = sig[0], sig[1]
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
            kw = dict(pct=self.alloc_pct, sl=stop, tp=tp, sl_pct=None if stop else self.sl_pct,
                      tp_pct=None if tp else self.tp_pct, trail_pct=self.trail_pct, reason=why)
            if long:
                ctx.buy(sym, **kw)
            elif self.allow_short:
                ctx.sell(sym, **kw)

    # helpers for "once per symbol per day" rules
    def traded_today(self, ctx, sym) -> bool:
        return ctx.memory.get("day") == ctx.today and sym in ctx.memory.get("traded", [])

    def mark_traded(self, ctx, sym):
        if ctx.memory.get("day") != ctx.today:
            ctx.memory["day"], ctx.memory["traded"] = ctx.today, []
        ctx.memory["traded"].append(sym)
