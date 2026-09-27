"""COPY THIS FILE to strategies/my_bot.py (no leading underscore) to create a new bot.
Push it to GitHub and it starts running on the next cycle. Backtest first:
    python -m engine.backtest my_bot

Everything available on `ctx`:
  DATA
    ctx.data(sym, interval=None, bars=300)  -> OHLCV DataFrame (closed bars only)
    ctx.price(sym)                          -> latest price
    ctx.technicals(sym, "15m")              -> TradingView rating + RSI/MACD/EMAs... (= MCP get_technicals_rating)
    ctx.tv(sym, ["RSI|15", "Recommend.All|60", "price_earnings_ttm"])  -> any TradingView column (= MCP get_symbol_data)
    ctx.tv_many([syms], [cols])             -> same, many symbols in one call
    ctx.screener(market="india", universe=["SYML:NSE;NIFTY"], filters={...}, columns=[...])  (= MCP run_screener)
  PORTFOLIO
    ctx.position(sym) ctx.positions() ctx.cash ctx.equity()
    ctx.memory  -> dict that persists between runs
  ORDERS (size by qty= / value= / pct= of equity; stops by sl=/tp= prices or sl_pct=/tp_pct=/trail_pct=)
    ctx.buy(sym, pct=20, sl_pct=1, tp_pct=2, reason="...")
    ctx.sell(sym, qty=10)   ctx.close(sym)   ctx.close_all()   ctx.set_stop(sym, sl=..., tp=...)
  OTHER
    ctx.signals()  -> external signals for this bot (from Claude / TradingView MCP)
    ctx.log(...)   ctx.notify("message to phone")   ctx.now (UTC datetime)
  INDICATORS (engine.ta): sma ema rma wma hma rsi macd atr bbands stoch vwap supertrend
                          crossover crossunder highest lowest
"""
from engine import Strategy, ta


class MyBot(Strategy):
    symbols = ["NSE:SBIN"]       # EXCHANGE:TICKER, exactly as on TradingView
    interval = "15m"             # 5m 15m 30m 1h 4h 1D  (cloud runs every 15 min)
    capital = 100_000
    intraday = False             # True = auto square-off before close
    # enabled = False            # uncomment to pause without deleting

    def on_bar(self, ctx):
        for sym in self.symbols:
            df = ctx.data(sym)
            rsi = ta.rsi(df.close, 14)
            if ctx.position(sym) == 0 and ta.crossover(rsi, 30):
                ctx.buy(sym, pct=25, sl_pct=2, tp_pct=4, reason="RSI back above 30")
            elif ctx.position(sym) > 0 and rsi.iloc[-1] > 70:
                ctx.close(sym, reason="RSI overbought")
