"""Daily trend swing: buy when price reclaims EMA20 inside an EMA20 > EMA50 uptrend."""
from engine import ta
from engine.bots import SignalBot


class EmaTrendSwing(SignalBot):
    description = "EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop"
    style = "swing"
    interval = "1D"
    run_at = "15:10"
    bars = 150
    min_bars = 60
    trail_pct = 8

    def entry(self, ctx, sym, df):
        e20, e50 = ta.ema(df.close, 20), ta.ema(df.close, 50)
        if e20.iloc[-1] > e50.iloc[-1] and ta.crossover(df.close, e20):
            return "long", "reclaimed EMA20 in uptrend"
        return None

    def exit(self, ctx, sym, df, qty):
        e20, e50 = ta.ema(df.close, 20), ta.ema(df.close, 50)
        if e20.iloc[-1] < e50.iloc[-1]:
            return "EMA20 fell below EMA50"
        return None
