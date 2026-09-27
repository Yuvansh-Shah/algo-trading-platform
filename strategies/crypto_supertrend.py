"""24/7 crypto trend follower: long while Supertrend(10, 3) on 1h bars is up. BTC + ETH.
Crypto data is real-time, but to save GitHub minutes it is only checked during NSE-hours runs. Capital is in USDT."""
from engine import Strategy, ta


class CryptoSupertrend(Strategy):
    description = "BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT)"
    style = "crypto"
    symbols = ["BINANCE:BTCUSDT", "BINANCE:ETHUSDT"]
    interval = "1h"
    capital = 50_000

    def on_bar(self, ctx):
        for sym in self.symbols:
            df = ctx.data(sym, bars=300)
            _, direction = ta.supertrend(df, 10, 3.0)
            up = direction.iloc[-1] == 1
            pos = ctx.position(sym)
            if pos == 0 and up:
                ctx.buy(sym, pct=45, reason="Supertrend up")
            elif pos > 0 and not up:
                ctx.close(sym, reason="Supertrend turned down")
