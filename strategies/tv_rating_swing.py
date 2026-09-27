"""Swing bot driven by TradingView's own technical ratings (same numbers the TradingView MCP
returns from get_technicals_rating / run_screener).

Every trading day at 15:05 IST:
  - scan NIFTY 50 for STRONG BUY on both daily and weekly ratings, RSI 50-70, above EMA 50
  - buy up to 5 of them (equal weight), 7% trailing stop
  - exit when the daily rating drops to SELL or worse
"""
from engine import Strategy


class TvRatingSwing(Strategy):
    market = "NSE"
    interval = "1D"
    run_at = "15:05"
    capital = 200_000
    max_positions = 5

    def on_bar(self, ctx):
        # 1) exits: re-check the rating of what we hold
        held = list(ctx.positions())
        if held:
            ratings = ctx.tv_many(held, ["Recommend.All"])
            for sym in held:
                r = ratings.get(sym, {}).get("Recommend.All")
                if r is not None and r <= -0.1:
                    ctx.close(sym, reason=f"TV rating turned SELL ({r:+.2f})")

        # 2) entries
        slots = self.max_positions - len(ctx.positions())
        if slots <= 0:
            return
        picks = ctx.screener(
            market="india",
            universe=["SYML:NSE;NIFTY"],                 # NIFTY 50
            filters={"Recommend.All": [0.5, None],       # daily STRONG BUY
                     "Recommend.All|1W": [0.3, None],    # weekly bullish too
                     "RSI": [50, 70]},
            columns=["name", "close", "Recommend.All", "Recommend.All|1W", "RSI", "EMA50"],
            sort_by="Recommend.All", limit=15,
        )
        if picks.empty:
            ctx.log("no candidates today")
            return
        picks = picks[picks.close > picks.EMA50]
        per_trade = ctx.equity() / self.max_positions
        for _, row in picks.iterrows():
            if slots == 0:
                break
            if ctx.position(row.symbol):
                continue
            ctx.buy(row.symbol, value=per_trade, trail_pct=7,
                    reason=f"TV STRONG BUY {row['Recommend.All']:+.2f}, RSI {row.RSI:.0f}")
            slots -= 1
