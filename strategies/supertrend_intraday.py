"""Supertrend(10, 3) intraday trend following on 15-minute bars."""
from engine import ta
from engine.bots import SignalBot


class SupertrendIntraday(SignalBot):
    description = "Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R"
    style = "intraday"
    interval = "15m"
    intraday = True
    allow_short = True
    rr = 2
    no_entry_after = "14:30"

    def entry(self, ctx, sym, df):
        st, d = ta.supertrend(df, 10, 3)
        if d.iloc[-1] == 1 and d.iloc[-2] == -1:
            return "long", "Supertrend flipped up", float(st.iloc[-1])
        if d.iloc[-1] == -1 and d.iloc[-2] == 1:
            return "short", "Supertrend flipped down", float(st.iloc[-1])
        return None

    def exit(self, ctx, sym, df, qty):
        _, d = ta.supertrend(df, 10, 3)
        if (qty > 0 and d.iloc[-1] == -1) or (qty < 0 and d.iloc[-1] == 1):
            return "Supertrend reversed"
        return None
