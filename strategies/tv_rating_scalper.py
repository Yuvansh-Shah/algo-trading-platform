"""Trades the TradingView 15m technical rating (same data as the MCP get_technicals_rating), with 1h confirmation."""
from engine import Strategy
from engine.bots import NIFTY_LIQUID


class TvRatingScalper(Strategy):
    description = "TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral"
    style = "intraday"
    symbols = NIFTY_LIQUID
    interval = "15m"
    capital = 50_000
    intraday = True
    allow_short = True
    max_positions = 3

    def on_bar(self, ctx):
        snap = ctx.tv_many(self.symbols, ["Recommend.All|15", "Recommend.All|60"])
        for sym, row in snap.items():
            r15 = row.get("Recommend.All|15")
            q = ctx.position(sym)
            if r15 is not None and ((q > 0 and r15 <= 0) or (q < 0 and r15 >= 0)):
                ctx.close(sym, reason=f"15m rating faded ({r15:+.2f})")
        if ctx.local_time > "14:30":
            return
        ranked = sorted(snap.items(), key=lambda kv: abs(kv[1].get("Recommend.All|15") or 0), reverse=True)
        for sym, row in ranked:
            if len(ctx.positions()) >= self.max_positions or ctx.position(sym):
                continue
            r15, r60 = row.get("Recommend.All|15") or 0, row.get("Recommend.All|60") or 0
            why = f"TV 15m {r15:+.2f} / 1h {r60:+.2f}"
            if r15 >= 0.5 and r60 >= 0.1:
                ctx.buy(sym, pct=33, sl_pct=0.8, tp_pct=1.6, reason=why)
            elif r15 <= -0.5 and r60 <= -0.1:
                ctx.sell(sym, pct=33, sl_pct=0.8, tp_pct=1.6, reason=why)
