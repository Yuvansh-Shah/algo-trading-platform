"""Trading sessions. Holidays are detected from live data (no holiday list to maintain):
if the market's benchmark has no bar for today 30+ min after the open, it is a holiday."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, time as dtime, timedelta
from functools import lru_cache
from zoneinfo import ZoneInfo

from . import tv


@dataclass(frozen=True)
class Session:
    tz: str
    open: dtime
    close: dtime
    days: tuple = (0, 1, 2, 3, 4)  # Mon..Fri
    benchmark: str | None = None  # used for holiday detection
    always_open: bool = False


SESSIONS = {
    "NSE": Session("Asia/Kolkata", dtime(9, 15), dtime(15, 30), benchmark="NSE:NIFTY"),
    "BSE": Session("Asia/Kolkata", dtime(9, 15), dtime(15, 30), benchmark="BSE:SENSEX"),
    "MCX": Session("Asia/Kolkata", dtime(9, 0), dtime(23, 30), benchmark="MCX:GOLD1!"),
    "US": Session("America/New_York", dtime(9, 30), dtime(16, 0), benchmark="AMEX:SPY"),
    "CRYPTO": Session("UTC", dtime(0, 0), dtime(23, 59, 59), days=tuple(range(7)), always_open=True),
    "FOREX": Session("America/New_York", dtime(0, 0), dtime(23, 59, 59), days=(0, 1, 2, 3, 4, 6)),
}


def now(tz: str = "Asia/Kolkata") -> datetime:
    return datetime.now(ZoneInfo(tz))


def local_now(market: str) -> datetime:
    return now(SESSIONS[market].tz)


def in_hours(market: str, at: datetime | None = None) -> bool:
    s = SESSIONS[market]
    t = (at or now()).astimezone(ZoneInfo(s.tz))
    if s.always_open:
        return True
    return t.weekday() in s.days and s.open <= t.time() <= s.close


@lru_cache(maxsize=None)
def _traded_today(market: str, day: str) -> bool:
    s = SESSIONS[market]
    try:
        bars = tv.ohlcv(s.benchmark, "1D", 3)
    except Exception:
        return True  # can't tell -> assume open, strategies will just see stale data
    last = bars.index[-1].tz_convert(s.tz).date().isoformat()
    return last == day


def is_open(market: str, at: datetime | None = None) -> bool:
    if not in_hours(market, at):
        return False
    s = SESSIONS[market]
    if s.always_open or not s.benchmark:
        return True
    # Open only once today's bars actually exist. With delayed NSE data that's ~09:31 IST,
    # which also means holidays are never mistaken for trading days.
    t = (at or now()).astimezone(ZoneInfo(s.tz))
    return _traded_today(market, t.date().isoformat())


def minutes_to_close(market: str, at: datetime | None = None) -> float:
    s = SESSIONS[market]
    t = (at or now()).astimezone(ZoneInfo(s.tz))
    close = t.replace(hour=s.close.hour, minute=s.close.minute, second=0, microsecond=0)
    return (close - t).total_seconds() / 60


def market_of_symbol(symbol: str) -> str:
    ex = symbol.split(":")[0].upper()
    m = tv.market_of(symbol)
    return {"india": "MCX" if ex == "MCX" else "NSE", "america": "US", "crypto": "CRYPTO",
            "forex": "FOREX"}.get(m, "NSE")
