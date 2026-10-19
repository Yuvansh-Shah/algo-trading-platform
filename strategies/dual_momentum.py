"""Dual momentum across Indian ETFs: once a month, hold the ETF with the best 6-month return,
or stay in cash if none of them is up (sidesteps long bear markets)."""
from engine import Strategy


class DualMomentum(Strategy):
    description = "Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash"
    style = "positional"
    symbols = ["NSE:NIFTYBEES", "NSE:BANKBEES", "NSE:JUNIORBEES", "NSE:GOLDBEES"]
    interval = "1D"
    run_at = "15:10"
    capital = 50_000
    lookback = 126  # ~6 months of trading days

    def on_bar(self, ctx):
        first = ctx.data(self.symbols[0], "1D", 5)
        day = first.index[-1].tz_convert("Asia/Kolkata").date()
        month = f"{day.year}-{day.month}"
        if ctx.memory.get("month") == month:
            return  # rebalance once per month
        ctx.memory["month"] = month
        rets = {}
        for sym in self.symbols:
            c = ctx.data(sym, "1D", self.lookback + 5).close
            if len(c) > self.lookback:
                rets[sym] = c.iloc[-1] / c.iloc[-self.lookback] - 1
        if not rets:
            return
        best, r = max(rets.items(), key=lambda kv: kv[1])
        target = best if r > 0 else None
        for sym in list(ctx.positions()):
            if sym != target:
                ctx.close(sym, reason=f"rotating to {target or 'cash'}")
        if target and not ctx.position(target):
            ctx.buy(target, pct=98, reason=f"strongest 6M return {r:+.1%}")
