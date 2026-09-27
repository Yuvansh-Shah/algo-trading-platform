"""Turtle-style Donchian breakout: buy 20-day highs, exit on 10-day lows."""
from engine import ta
from engine.bots import SignalBot


class DonchianTurtle(SignalBot):
    description = "Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop"
    style = "swing"
    interval = "1D"
    run_at = "15:10"
    bars = 120
    min_bars = 40
    sl_atr = 2

    def entry(self, ctx, sym, df):
        hh = ta.highest(df.high, 20).shift(1).iloc[-1]
        if df.close.iloc[-1] > hh:
            return "long", f"20-day breakout > {hh:.1f}"
        return None

    def exit(self, ctx, sym, df, qty):
        ll = ta.lowest(df.low, 10).shift(1).iloc[-1]
        if df.close.iloc[-1] < ll:
            return "10-day low"
        return None
