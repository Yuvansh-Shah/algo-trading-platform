"""Very short holding: RSI(2) extremes in the direction of the 50-EMA, out within about an hour."""
from engine import ta
from engine.bots import SignalBot


class Rsi2Scalper(SignalBot):
    description = "RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars"
    style = "scalp"
    interval = "15m"
    intraday = True
    allow_short = True
    sl_pct = 0.8
    no_entry_before = "09:45"
    no_entry_after = "14:45"
    max_hold_bars = 4

    def entry(self, ctx, sym, df):
        r2, e50, c = ta.rsi(df.close, 2).iloc[-1], ta.ema(df.close, 50).iloc[-1], df.close.iloc[-1]
        if c > e50 and r2 < 10:
            ctx.memory.setdefault("held", {})[sym] = 0
            return "long", f"RSI2 {r2:.0f} in uptrend"
        if c < e50 and r2 > 90:
            ctx.memory.setdefault("held", {})[sym] = 0
            return "short", f"RSI2 {r2:.0f} in downtrend"
        return None

    def exit(self, ctx, sym, df, qty):
        held = ctx.memory.setdefault("held", {})
        held[sym] = held.get(sym, 0) + 1
        r2 = ta.rsi(df.close, 2).iloc[-1]
        if (qty > 0 and r2 > 70) or (qty < 0 and r2 < 30):
            return f"RSI2 snapped back ({r2:.0f})"
        if held[sym] >= self.max_hold_bars:
            return "time stop (1h)"
        return None
