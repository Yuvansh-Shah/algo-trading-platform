"""Daily Bollinger Band mean reversion inside a long-term uptrend."""
from engine import ta
from engine.bots import SignalBot


class BbReversionDaily(SignalBot):
    description = "Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band"
    style = "swing"
    interval = "1D"
    run_at = "15:10"
    bars = 300
    min_bars = 210
    sl_pct = 6

    def entry(self, ctx, sym, df):
        _, _, lo = ta.bbands(df.close, 20, 2)
        c = df.close.iloc[-1]
        if c < lo.iloc[-1] and c > ta.sma(df.close, 200).iloc[-1]:
            return "long", "below lower band in uptrend"
        return None

    def exit(self, ctx, sym, df, qty):
        _, mid, _ = ta.bbands(df.close, 20, 2)
        if df.close.iloc[-1] >= mid.iloc[-1]:
            return "back to middle band"
        return None
