"""Gap and Go: stocks that gap more than 0.8% and confirm with the first candle keep running."""
from engine import ta
from engine.bots import SignalBot


class GapAndGo(SignalBot):
    description = "Gap >0.8% + first 15m candle confirms + break of its high/low, 2R"
    style = "intraday"
    interval = "15m"
    intraday = True
    allow_short = True
    rr = 2
    no_entry_after = "11:00"

    def entry(self, ctx, sym, df):
        day, prev = ta.session(df), ta.prev_session(df)
        if len(day) < 2 or prev.empty or self.traded_today(ctx, sym):
            return None
        gap = day.open.iloc[0] / prev.close.iloc[-1] - 1
        first = day.iloc[0]
        c = day.close.iloc[-1]
        if gap > 0.008 and first.close > first.open and c > first.high:
            self.mark_traded(ctx, sym)
            return "long", f"gap up {gap:+.1%} and go", float(first.low)
        if gap < -0.008 and first.close < first.open and c < first.low:
            self.mark_traded(ctx, sym)
            return "short", f"gap down {gap:+.1%} and go", float(first.high)
        return None
