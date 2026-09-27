"""24/7 crypto trend follower: Supertrend(10, 3) on 1h bars, long-only, BTC + ETH.
Crypto data from TradingView is real-time (no delay) and the market never closes."""
from engine import Strategy, ta


class CryptoSupertrend(Strategy):
    symbols = ["BINANCE:BTCUSDT", "BINANCE:ETHUSDT"]
    interval = "1h"
    capital = 10_000  # USDT

    def on_bar(self, ctx):
        for sym in self.symbols:
            df = ctx.data(sym, bars=300)
            _, direction = ta.supertrend(df, 10, 3.0)
            flipped_up = direction.iloc[-1] == 1 and direction.iloc[-2] == -1
            flipped_down = direction.iloc[-1] == -1 and direction.iloc[-2] == 1
            pos = ctx.position(sym)
            if pos == 0 and flipped_up:
                ctx.buy(sym, pct=45, reason="Supertrend flipped up")
            elif pos > 0 and flipped_down:
                ctx.close(sym, reason="Supertrend flipped down")
