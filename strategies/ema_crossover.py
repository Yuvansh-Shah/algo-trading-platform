"""Intraday EMA crossover on NSE large caps (15-minute bars).

Long when EMA 9 crosses above EMA 21 with RSI > 50 and price above VWAP.
1.5x ATR stop, 3x ATR target, exit on the opposite cross, squared off 15 min before close.
"""
from engine import Strategy, ta


class EmaCrossover(Strategy):
    symbols = ["NSE:RELIANCE", "NSE:HDFCBANK", "NSE:ICICIBANK", "NSE:INFY", "NSE:TCS"]
    interval = "15m"
    capital = 100_000
    intraday = True

    fast, slow = 9, 21
    alloc_pct = 20  # % of equity per trade

    def on_bar(self, ctx):
        for sym in self.symbols:
            df = ctx.data(sym, bars=200)
            if len(df) < self.slow + 5:
                continue
            fast, slow = ta.ema(df.close, self.fast), ta.ema(df.close, self.slow)
            rsi = ta.rsi(df.close, 14).iloc[-1]
            vwap = ta.vwap(df).iloc[-1]
            atr = ta.atr(df, 14).iloc[-1]
            px = df.close.iloc[-1]
            pos = ctx.position(sym)

            if pos == 0 and ta.crossover(fast, slow) and rsi > 50 and px > vwap:
                ctx.buy(sym, pct=self.alloc_pct, sl=px - 1.5 * atr, tp=px + 3 * atr,
                        reason=f"EMA{self.fast}>{self.slow}, RSI {rsi:.0f}")
            elif pos > 0 and ta.crossunder(fast, slow):
                ctx.close(sym, reason="EMA cross down")
