"""VWAP mean reversion: fade stretched moves (2 sigma away from VWAP) back to VWAP."""
from engine import ta
from engine.bots import SignalBot


class VwapReversion(SignalBot):
    description = "Fade 2-sigma stretches from VWAP, exit back at VWAP"
    style = "intraday"
    interval = "15m"
    intraday = True
    allow_short = True
    sl_atr = 1.5
    no_entry_before = "10:00"
    no_entry_after = "14:30"

    def _z(self, df):
        dev = df.close - ta.vwap(df)
        return dev / dev.rolling(20).std()

    def entry(self, ctx, sym, df):
        z = self._z(df).iloc[-1]
        if z < -2:
            return "long", f"{z:.1f} sigma below VWAP"
        if z > 2:
            return "short", f"{z:.1f} sigma above VWAP"
        return None

    def exit(self, ctx, sym, df, qty):
        z = self._z(df).iloc[-1]
        if (qty > 0 and z > -0.2) or (qty < 0 and z < 0.2):
            return "back to VWAP"
        return None
