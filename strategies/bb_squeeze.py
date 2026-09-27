"""Bollinger Band squeeze breakout: volatility contraction then expansion."""
from engine import ta
from engine.bots import SignalBot


class BbSqueeze(SignalBot):
    description = "BB width at a 30-bar low, then a close outside the band; exit at mid band"
    style = "intraday"
    interval = "15m"
    intraday = True
    allow_short = True
    sl_atr = 1.5
    tp_atr = 3
    no_entry_after = "14:30"

    def entry(self, ctx, sym, df):
        up, mid, lo = ta.bbands(df.close, 20, 2)
        width = (up - lo) / mid
        squeezed = width.iloc[-2] <= width.iloc[-31:-1].min() * 1.05
        c = df.close.iloc[-1]
        if squeezed and c > up.iloc[-1]:
            return "long", "squeeze breakout up"
        if squeezed and c < lo.iloc[-1]:
            return "short", "squeeze breakout down"
        return None

    def exit(self, ctx, sym, df, qty):
        _, mid, _ = ta.bbands(df.close, 20, 2)
        c = df.close.iloc[-1]
        if (qty > 0 and c < mid.iloc[-1]) or (qty < 0 and c > mid.iloc[-1]):
            return "back to mid band"
        return None
