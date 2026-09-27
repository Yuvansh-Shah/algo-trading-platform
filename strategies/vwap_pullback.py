"""VWAP pullback: in an intraday trend, buy the dip to VWAP (sell the rip in a downtrend)."""
from engine import ta
from engine.bots import SignalBot


class VwapPullback(SignalBot):
    description = "Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target"
    style = "intraday"
    interval = "15m"
    intraday = True
    allow_short = True
    sl_atr = 1.0
    rr = 2
    no_entry_before = "09:45"
    no_entry_after = "14:30"

    def entry(self, ctx, sym, df):
        v = ta.vwap(df)
        e20, e50 = ta.ema(df.close, 20), ta.ema(df.close, 50)
        c, o, lo, hi, vw = df.close.iloc[-1], df.open.iloc[-1], df.low.iloc[-1], df.high.iloc[-1], v.iloc[-1]
        if e20.iloc[-1] > e50.iloc[-1] and lo <= vw * 1.001 and c > vw and c > o:
            return "long", "pullback held VWAP in uptrend"
        if e20.iloc[-1] < e50.iloc[-1] and hi >= vw * 0.999 and c < vw and c < o:
            return "short", "rally rejected at VWAP in downtrend"
        return None

    def exit(self, ctx, sym, df, qty):
        vw, c = ta.vwap(df).iloc[-1], df.close.iloc[-1]
        if (qty > 0 and c < vw * 0.997) or (qty < 0 and c > vw * 1.003):
            return "lost VWAP"
        return None
