"""TradingView data client.

Uses the same public endpoints the TradingView MCP uses (scanner.tradingview.com
for indicators/ratings/screener and the chart websocket for OHLCV bars), so a
strategy running in the cloud sees the same numbers you see through the MCP.

READ-ONLY and LOGGED-OUT by design: no username, password, cookie or session
token is ever sent, so this code cannot see or change anyone's TradingView
account (layouts, indicators, alerts, watchlists all stay untouched).
"""
from __future__ import annotations

import json
import random
import re
import string
import time

import pandas as pd
import requests
from websocket import create_connection

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
    "Origin": "https://www.tradingview.com",
    "Referer": "https://www.tradingview.com/",
}
SCAN_URL = "https://scanner.tradingview.com/{market}/scan"
WS_URL = "wss://data.tradingview.com/socket.io/websocket"

EXCHANGE_MARKET = {
    "NSE": "india", "BSE": "india", "MCX": "india",
    "NASDAQ": "america", "NYSE": "america", "AMEX": "america", "CBOE": "america", "ARCA": "america",
    "BINANCE": "crypto", "COINBASE": "crypto", "BYBIT": "crypto", "OKX": "crypto", "KRAKEN": "crypto",
    "BITSTAMP": "crypto", "CRYPTO": "crypto", "BITGET": "crypto", "MEXC": "crypto",
    "FX": "forex", "FX_IDC": "forex", "OANDA": "forex", "FOREXCOM": "forex", "SAXO": "forex",
    "LSE": "uk", "XETR": "germany", "TSE": "japan",
}

# interval -> suffix used on scanner columns ("RSI|15" = RSI on 15m chart)
TF_SCANNER = {"1m": "1", "5m": "5", "15m": "15", "30m": "30", "1h": "60", "2h": "120",
              "4h": "240", "1D": "", "1W": "1W", "1M": "1M"}
# interval -> resolution code for the chart websocket
TF_CHART = {"1m": "1", "3m": "3", "5m": "5", "15m": "15", "30m": "30", "1h": "60", "2h": "120",
            "4h": "240", "1D": "1D", "1W": "1W", "1M": "1M"}

# Same fields the MCP's get_technicals_rating returns.
TECHNICAL_COLUMNS = [
    "Recommend.All", "Recommend.MA", "Recommend.Other", "close",
    "RSI", "Stoch.K", "Stoch.D", "CCI20", "ADX", "ADX+DI", "ADX-DI", "MACD.macd", "MACD.signal",
    "Mom", "AO", "W.R", "BBPower", "UO",
    "EMA10", "EMA20", "EMA30", "EMA50", "EMA100", "EMA200",
    "SMA10", "SMA20", "SMA30", "SMA50", "SMA100", "SMA200",
    "VWMA", "HullMA9", "Ichimoku.BLine", "BB.upper", "BB.lower", "ATR",
]


def market_of(symbol: str) -> str:
    return EXCHANGE_MARKET.get(symbol.split(":")[0].upper(), "global")


def rating_label(value) -> str:
    if value is None:
        return "N/A"
    if value >= 0.5:
        return "STRONG_BUY"
    if value >= 0.1:
        return "BUY"
    if value > -0.1:
        return "NEUTRAL"
    if value > -0.5:
        return "SELL"
    return "STRONG_SELL"


def _post(url: str, payload: dict, tries: int = 5) -> dict:
    delay = 2.0
    for attempt in range(tries):
        try:
            r = requests.post(url, json=payload, headers=HEADERS, timeout=20)
            if r.status_code == 200:
                return r.json()
            if r.status_code not in (429, 500, 502, 503, 504):
                raise RuntimeError(f"TradingView scanner {r.status_code}: {r.text[:300]}")
        except requests.RequestException:
            if attempt == tries - 1:
                raise
        time.sleep(delay + random.random())
        delay *= 2
    raise RuntimeError(f"TradingView scanner kept failing (rate limited?): {url}")


def with_tf(columns: list[str], interval: str) -> list[str]:
    suffix = TF_SCANNER[interval]
    return [c if (not suffix or "|" in c) else f"{c}|{suffix}" for c in columns]


def scan(symbols: list[str], columns: list[str]) -> dict[str, dict]:
    """Fetch arbitrary screener columns for many symbols (like MCP get_symbol_data_batch).

    Column names are the same ones the MCP accepts, e.g. "close", "RSI", "RSI|15",
    "Recommend.All|60", "EMA20|240", "market_cap_basic", "price_earnings_ttm".
    Returns {symbol: {column: value}}.
    """
    by_market: dict[str, list[str]] = {}
    for s in symbols:
        by_market.setdefault(market_of(s), []).append(s)
    out: dict[str, dict] = {}
    for market, syms in by_market.items():
        for i in range(0, len(syms), 200):
            chunk = syms[i:i + 200]
            data = _post(SCAN_URL.format(market=market),
                         {"symbols": {"tickers": chunk}, "columns": columns})
            for row in data.get("data", []):
                out[row["s"]] = dict(zip(columns, row["d"]))
    return out


def quote(symbols: list[str]) -> dict[str, float]:
    """Latest price for each symbol (delayed ~15 min for NSE/BSE without a login)."""
    rows = scan(symbols, ["close"])
    return {s: v["close"] for s, v in rows.items() if v.get("close") is not None}


def technicals(symbol: str, interval: str = "1D") -> dict:
    """Same indicator snapshot as MCP get_technicals_rating, keys without the |tf suffix."""
    cols = with_tf(TECHNICAL_COLUMNS, interval)
    row = scan([symbol], cols).get(symbol, {})
    snap = {c.split("|")[0]: row.get(c) for c in cols}
    snap["rating"] = rating_label(snap.get("Recommend.All"))
    snap["rating_ma"] = rating_label(snap.get("Recommend.MA"))
    snap["rating_osc"] = rating_label(snap.get("Recommend.Other"))
    return snap


def _filter_expr(filters: dict) -> list[dict]:
    expr = []
    for field, rng in (filters or {}).items():
        if isinstance(rng, (list, tuple)) and len(rng) == 2:
            lo, hi = rng
            if lo is not None and hi is not None:
                expr.append({"left": field, "operation": "in_range", "right": [lo, hi]})
            elif lo is not None:
                expr.append({"left": field, "operation": "greater", "right": lo})
            elif hi is not None:
                expr.append({"left": field, "operation": "less", "right": hi})
        else:
            expr.append({"left": field, "operation": "equal", "right": rng})
    return expr


def screener(market: str = "india", filters: dict | None = None, columns: list[str] | None = None,
             sort_by: str = "volume", order: str = "desc", limit: int = 50,
             universe: list[str] | None = None, types: list[str] | None = None) -> pd.DataFrame:
    """Run the TradingView screener (like MCP run_screener).

    filters:  {"RSI": [None, 30], "close": [100, None], "Recommend.All|60": [0.1, None]}
    universe: index symbolsets, e.g. ["SYML:NSE;NIFTY"] for NIFTY 50,
              ["SYML:NSE;CNX500"] for NIFTY 500, ["SYML:SP;SPX"] for S&P 500
    """
    columns = columns or ["name", "close", "change", "volume", "RSI", "Recommend.All"]
    payload = {
        "columns": columns,
        "filter": _filter_expr(filters),
        "sort": {"sortBy": sort_by, "sortOrder": order},
        "range": [0, limit],
        "markets": [market],
    }
    if universe:
        payload["symbols"] = {"symbolset": universe}
    if types:
        payload["filter2"] = {"operator": "and", "operands": [
            {"expression": {"left": "type", "operation": "in_range", "right": types}}]}
    data = _post(SCAN_URL.format(market=market), payload)
    rows = [{"symbol": r["s"], **dict(zip(columns, r["d"]))} for r in data.get("data", [])]
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- OHLCV bars

def _rand(n: int = 12) -> str:
    return "".join(random.choice(string.ascii_lowercase) for _ in range(n))


def _frame(method: str, params: list) -> str:
    msg = json.dumps({"m": method, "p": params}, separators=(",", ":"))
    return f"~m~{len(msg)}~m~{msg}"


_OHLCV_CACHE: dict = {}


def ohlcv(symbol: str, interval: str = "1D", bars: int = 300, tries: int = 3,
          use_cache: bool = True) -> pd.DataFrame:
    """Historical bars (like MCP get_ohlcv). Index = bar open time (UTC, tz-aware).
    Cached for the rest of the process, so 20 bots on the same symbols fetch once."""
    key = (symbol, interval)
    if use_cache and key in _OHLCV_CACHE and len(_OHLCV_CACHE[key]) >= bars:
        return _OHLCV_CACHE[key].tail(bars)
    df = _fetch_ohlcv(symbol, interval, max(bars, 500), tries)
    _OHLCV_CACHE[key] = df
    return df.tail(bars)


def _fetch_ohlcv(symbol: str, interval: str, bars: int, tries: int) -> pd.DataFrame:
    res = TF_CHART[interval]
    last_err = None
    for _ in range(tries):
        try:
            ws = create_connection(WS_URL, header=[f"{k}: {v}" for k, v in HEADERS.items()], timeout=20)
            try:
                cs = "cs_" + _rand()
                ws.send(_frame("set_auth_token", ["unauthorized_user_token"]))
                ws.send(_frame("chart_create_session", [cs, ""]))
                ws.send(_frame("resolve_symbol", [cs, "sym_1",
                                                  '=' + json.dumps({"symbol": symbol, "adjustment": "splits"})]))
                ws.send(_frame("create_series", [cs, "s1", "s1", "sym_1", res, int(bars)]))
                raw, t0 = "", time.time()
                while time.time() - t0 < 25:
                    msg = ws.recv()
                    for hb in re.findall(r"~m~\d+~m~(~h~\d+)", msg):
                        ws.send(f"~m~{len(hb)}~m~{hb}")
                    raw += msg
                    if "series_completed" in msg or "symbol_error" in msg or "series_error" in msg:
                        break
            finally:
                ws.close()
            if "symbol_error" in raw:
                raise ValueError(f"TradingView does not know symbol {symbol!r}")
            m = re.search(r'"s":\[(.*?)\],"ns"', raw)
            if not m:
                raise RuntimeError(f"no bars returned for {symbol} {interval}")
            rows = [b["v"][:6] for b in json.loads("[" + m.group(1) + "]")]
            df = pd.DataFrame(rows, columns=["time", "open", "high", "low", "close", "volume"][:len(rows[0])])
            if "volume" not in df:
                df["volume"] = 0.0
            df.index = pd.DatetimeIndex(pd.to_datetime(df.pop("time"), unit="s", utc=True)).as_unit("ns")
            return df.astype(float)
        except ValueError:
            raise
        except Exception as e:  # network hiccup -> retry
            last_err = e
            time.sleep(2 + random.random() * 2)
    raise RuntimeError(f"OHLCV fetch failed for {symbol} {interval}: {last_err}")
