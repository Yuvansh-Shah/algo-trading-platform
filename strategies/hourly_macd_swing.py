"""Short-term swing on hourly bars: MACD signal-line cross in the direction of the 200-EMA."""
from engine import ta
from engine.bots import SignalBot


class HourlyMacdSwing(SignalBot):
    description = "1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR"
    style = "swing"
    interval = "1h"
    bars = 300
    min_bars = 210
    sl_atr = 2
    tp_atr = 4

    def entry(self, ctx, sym, df):
        line, sig, _ = ta.macd(df.close)
        if ta.crossover(line, sig) and df.close.iloc[-1] > ta.ema(df.close, 200).iloc[-1]:
            return "long", "1h MACD bull cross above EMA200"
        return None

    def exit(self, ctx, sym, df, qty):
        line, sig, _ = ta.macd(df.close)
        if ta.crossunder(line, sig):
            return "1h MACD bear cross"
        return None
