"""Intraday EMA 9/21 crossover with RSI and VWAP filters."""
from engine import ta
from engine.bots import SignalBot


class EmaCrossover(SignalBot):
    description = "EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR"
    style = "intraday"
    interval = "15m"
    intraday = True
    allow_short = True
    sl_atr = 1.5
    tp_atr = 3
    no_entry_after = "14:45"

    def entry(self, ctx, sym, df):
        f, s = ta.ema(df.close, 9), ta.ema(df.close, 21)
        r, v, c = ta.rsi(df.close).iloc[-1], ta.vwap(df).iloc[-1], df.close.iloc[-1]
        if ta.crossover(f, s) and r > 50 and c > v:
            return "long", f"EMA9>21, RSI {r:.0f}"
        if ta.crossunder(f, s) and r < 50 and c < v:
            return "short", f"EMA9<21, RSI {r:.0f}"
        return None

    def exit(self, ctx, sym, df, qty):
        f, s = ta.ema(df.close, 9), ta.ema(df.close, 21)
        if (qty > 0 and ta.crossunder(f, s)) or (qty < 0 and ta.crossover(f, s)):
            return "opposite EMA cross"
        return None
