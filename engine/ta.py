"""Common indicators in plain pandas (TradingView-compatible formulas).

Every function takes pandas Series (e.g. df.close) and returns a Series,
so you can write `ta.ema(df.close, 20)` just like `ta.ema(close, 20)` in Pine.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n).mean()


def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def rma(s: pd.Series, n: int) -> pd.Series:
    """Wilder's moving average (Pine's ta.rma)."""
    return s.ewm(alpha=1 / n, adjust=False).mean()


def wma(s: pd.Series, n: int) -> pd.Series:
    w = np.arange(1, n + 1)
    return s.rolling(n).apply(lambda x: np.dot(x, w) / w.sum(), raw=True)


def hma(s: pd.Series, n: int) -> pd.Series:
    return wma(2 * wma(s, n // 2) - wma(s, n), int(np.sqrt(n)))


def rsi(s: pd.Series, n: int = 14) -> pd.Series:
    d = s.diff()
    up = rma(d.clip(lower=0), n)
    down = rma(-d.clip(upper=0), n)
    return 100 - 100 / (1 + up / down.replace(0, np.nan))


def macd(s: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    line = ema(s, fast) - ema(s, slow)
    sig = ema(line, signal)
    return line, sig, line - sig


def true_range(df: pd.DataFrame) -> pd.Series:
    pc = df.close.shift()
    return pd.concat([df.high - df.low, (df.high - pc).abs(), (df.low - pc).abs()], axis=1).max(axis=1)


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    return rma(true_range(df), n)


def bbands(s: pd.Series, n: int = 20, mult: float = 2.0):
    mid = sma(s, n)
    dev = s.rolling(n).std(ddof=0)
    return mid + mult * dev, mid, mid - mult * dev


def stoch(df: pd.DataFrame, k: int = 14, smooth_k: int = 3, d: int = 3):
    ll, hh = df.low.rolling(k).min(), df.high.rolling(k).max()
    kline = sma(100 * (df.close - ll) / (hh - ll), smooth_k)
    return kline, sma(kline, d)


def vwap(df: pd.DataFrame) -> pd.Series:
    """Session VWAP, resetting each calendar day (IST)."""
    tp = (df.high + df.low + df.close) / 3
    day = df.index.tz_convert("Asia/Kolkata").date
    pv = (tp * df.volume).groupby(day).cumsum()
    vol = df.volume.groupby(day).cumsum()
    return pv / vol.replace(0, np.nan)


def supertrend(df: pd.DataFrame, n: int = 10, mult: float = 3.0):
    """Returns (supertrend_line, direction) where direction = 1 uptrend, -1 downtrend."""
    a = atr(df, n)
    hl2 = (df.high + df.low) / 2
    upper = (hl2 + mult * a).to_numpy(dtype=float, copy=True)
    lower = (hl2 - mult * a).to_numpy(dtype=float, copy=True)
    close = df.close.to_numpy(dtype=float)
    st, dirn = np.full(len(df), np.nan), np.ones(len(df))
    for i in range(1, len(df)):
        if np.isnan(a.iloc[i]):
            continue
        if not (lower[i] > lower[i - 1] or close[i - 1] < lower[i - 1]):
            lower[i] = lower[i - 1]
        if not (upper[i] < upper[i - 1] or close[i - 1] > upper[i - 1]):
            upper[i] = upper[i - 1]
        if np.isnan(st[i - 1]) or st[i - 1] == upper[i - 1]:
            dirn[i] = 1 if close[i] > upper[i] else -1
        else:
            dirn[i] = -1 if close[i] < lower[i] else 1
        st[i] = lower[i] if dirn[i] == 1 else upper[i]
    return pd.Series(st, index=df.index), pd.Series(dirn, index=df.index)


def crossover(a: pd.Series, b) -> bool:
    """True if `a` crossed above `b` on the last bar (Pine's ta.crossover)."""
    b = b if isinstance(b, pd.Series) else pd.Series(b, index=a.index)
    return bool(a.iloc[-2] <= b.iloc[-2] and a.iloc[-1] > b.iloc[-1])


def crossunder(a: pd.Series, b) -> bool:
    b = b if isinstance(b, pd.Series) else pd.Series(b, index=a.index)
    return bool(a.iloc[-2] >= b.iloc[-2] and a.iloc[-1] < b.iloc[-1])


def highest(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n).max()


def lowest(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n).min()


def adx(df: pd.DataFrame, n: int = 14):
    """Returns (adx, +DI, -DI) like Pine's ta.dmi."""
    up, down = df.high.diff(), -df.low.diff()
    plus_dm = pd.Series(np.where((up > down) & (up > 0), up, 0.0), index=df.index)
    minus_dm = pd.Series(np.where((down > up) & (down > 0), down, 0.0), index=df.index)
    tr = rma(true_range(df), n)
    plus_di = 100 * rma(plus_dm, n) / tr
    minus_di = 100 * rma(minus_dm, n) / tr
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    return rma(dx, n), plus_di, minus_di


def session(df: pd.DataFrame, tz: str = "Asia/Kolkata") -> pd.DataFrame:
    """Bars of the most recent trading day in `df` (for opening-range / gap logic)."""
    days = df.index.tz_convert(tz).date
    return df[days == days[-1]]


def prev_session(df: pd.DataFrame, tz: str = "Asia/Kolkata") -> pd.DataFrame:
    days = df.index.tz_convert(tz).date
    prior = sorted(set(days))[:-1]
    return df[days == prior[-1]] if prior else df.iloc[0:0]
