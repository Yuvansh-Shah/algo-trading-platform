"""Opening Range Breakout: trade the break of the first 15-minute candle (09:15-09:30)."""
from engine import ta
from engine.bots import SignalBot


class OrbBreakout(SignalBot):
    description = "15-min opening range breakout, long/short, stop at other side, 2R target"
    style = "intraday"
    interval = "15m"
    intraday = True
    allow_short = True
    rr = 2
    no_entry_after = "11:30"

    def entry(self, ctx, sym, df):
        day = ta.session(df)
        if len(day) < 2 or self.traded_today(ctx, sym):
            return None
        hi, lo = day.high.iloc[0], day.low.iloc[0]
        c, pc = day.close.iloc[-1], day.close.iloc[-2]
        if (hi - lo) / c > 0.02:  # skip huge opening ranges
            return None
        if c > hi and pc <= hi:
            self.mark_traded(ctx, sym)
            return "long", f"ORB up > {hi:.1f}", lo
        if c < lo and pc >= lo:
            self.mark_traded(ctx, sym)
            return "short", f"ORB down < {lo:.1f}", hi
        return None
