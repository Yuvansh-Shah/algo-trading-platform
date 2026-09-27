"""MACD momentum with an ADX trend-strength filter."""
from engine import ta
from engine.bots import SignalBot


class MacdAdx(SignalBot):
    description = "MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross"
    style = "intraday"
    interval = "15m"
    intraday = True
    allow_short = True
    sl_atr = 1.5
    tp_atr = 3
    no_entry_after = "14:30"

    def entry(self, ctx, sym, df):
        _, _, hist = ta.macd(df.close)
        adx, _, _ = ta.adx(df)
        c, e50 = df.close.iloc[-1], ta.ema(df.close, 50).iloc[-1]
        if adx.iloc[-1] < 20:
            return None
        if ta.crossover(hist, 0) and c > e50:
            return "long", f"MACD up, ADX {adx.iloc[-1]:.0f}"
        if ta.crossunder(hist, 0) and c < e50:
            return "short", f"MACD down, ADX {adx.iloc[-1]:.0f}"
        return None

    def exit(self, ctx, sym, df, qty):
        _, _, hist = ta.macd(df.close)
        if (qty > 0 and ta.crossunder(hist, 0)) or (qty < 0 and ta.crossover(hist, 0)):
            return "MACD reversed"
        return None
