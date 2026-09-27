"""Relative-strength rotation: hold the 3 strongest NIFTY 50 stocks by 3-month performance."""
from engine import Strategy


class MomentumRotation(Strategy):
    description = "Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10"
    style = "positional"
    market = "NSE"
    interval = "1D"
    run_at = "15:10"
    capital = 50_000
    hold = 3
    keep_rank = 10

    def on_bar(self, ctx):
        board = ctx.screener(
            market="india", universe=["SYML:NSE;NIFTY"],
            columns=["name", "close", "Perf.3M", "SMA50", "Recommend.All"],
            sort_by="Perf.3M", limit=50,
        )
        if board.empty:
            return
        board = board[(board.close > board.SMA50) & (board["Recommend.All"] > 0) & (board["Perf.3M"] > 0)]
        board = board.reset_index(drop=True)
        top_keep = set(board.symbol.head(self.keep_rank))
        for sym in list(ctx.positions()):
            if sym not in top_keep:
                ctx.close(sym, reason="dropped out of top 10 momentum")
        per = ctx.equity() / self.hold
        for _, row in board.head(self.hold * 3).iterrows():
            if len(ctx.positions()) >= self.hold:
                break
            if ctx.position(row.symbol) or row.close > per:
                continue
            ctx.buy(row.symbol, value=per, sl_pct=12, reason=f"3M perf {row['Perf.3M']:+.1f}%")
