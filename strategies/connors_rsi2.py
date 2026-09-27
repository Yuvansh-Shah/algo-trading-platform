"""Larry Connors RSI(2): buy short-term dips in long-term uptrends, sell into the bounce."""
from engine import ta
from engine.bots import SignalBot


class ConnorsRsi2(SignalBot):
    description = "Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days)"
    style = "swing"
    interval = "1D"
    run_at = "15:10"
    bars = 300
    min_bars = 210
    sl_pct = 6

    def entry(self, ctx, sym, df):
        c = df.close
        r2 = ta.rsi(c, 2).iloc[-1]
        if c.iloc[-1] > ta.sma(c, 200).iloc[-1] and r2 < 10:
            return "long", f"RSI2 {r2:.0f} dip in uptrend"
        return None

    def exit(self, ctx, sym, df, qty):
        if df.close.iloc[-1] > ta.sma(df.close, 5).iloc[-1]:
            return "closed above SMA5"
        return None
