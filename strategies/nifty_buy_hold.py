"""Benchmark: put the whole ₹50k in NIFTYBEES and never sell. Every bot should beat this."""
from engine import Strategy


class NiftyBuyHold(Strategy):
    description = "Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold"
    style = "benchmark"
    symbols = ["NSE:NIFTYBEES"]
    interval = "1D"
    run_at = "09:45"
    capital = 50_000

    def on_bar(self, ctx):
        sym = self.symbols[0]
        if not ctx.position(sym):
            ctx.buy(sym, pct=99, reason="benchmark buy & hold")
