"""Strategy base class and the `ctx` object every strategy receives.

Minimal strategy:

    from engine import Strategy, ta

    class MyBot(Strategy):
        symbols = ["NSE:RELIANCE"]
        interval = "15m"

        def on_bar(self, ctx):
            df = ctx.data("NSE:RELIANCE")
            if ta.crossover(ta.ema(df.close, 9), ta.ema(df.close, 21)):
                ctx.buy("NSE:RELIANCE", pct=50, sl_pct=1.5, tp_pct=3)
"""
from __future__ import annotations

import math
from datetime import datetime, timedelta, timezone

import pandas as pd

from . import tv
from .broker import PaperBroker

INTERVAL_MIN = {"1m": 1, "3m": 3, "5m": 5, "15m": 15, "30m": 30, "1h": 60, "2h": 120, "4h": 240,
                "1D": 1440, "1W": 10080, "1M": 43200}
# Logged-out TradingView data is delayed for these exchanges (minutes).
DATA_DELAY_MIN = {"NSE": 15, "BSE": 15, "MCX": 15}


class NotAvailableInBacktest(RuntimeError):
    pass


class Strategy:
    name: str | None = None          # defaults to the file name
    symbols: list[str] = []          # fixed universe (can be empty if you use ctx.screener)
    interval: str = "15m"            # how often on_bar runs: 5m 15m 30m 1h 4h 1D ...
    market: str | None = None        # NSE / US / CRYPTO / FOREX / MCX (auto from first symbol)
    capital: float = 100_000         # paper money for this bot
    enabled: bool = True
    intraday: bool = False           # auto square-off before market close
    square_off_minutes: int = 15     # ...this many minutes before close
    allow_short: bool = False
    run_at: str | None = None        # for 1D bots: local market time to run, e.g. "15:10"
    live: bool = False               # forward orders to live webhook (see config.yaml)

    def on_start(self, ctx: "Context"):
        """Called once, the first time the bot ever runs."""

    def on_bar(self, ctx: "Context"):
        raise NotImplementedError


class Context:
    def __init__(self, strategy: Strategy, broker: PaperBroker, market: str,
                 clock: datetime | None = None, data_provider=None, executor=None,
                 signals: list | None = None, notifier=None, logger=print):
        self.strategy = strategy
        self.broker = broker
        self.market = market
        self._clock = clock
        self._data = data_provider  # backtest provider; None = live TradingView
        self._exec = executor       # backtest executor; None = fill now at live quote
        self._signals = signals or []
        self._signals_read = False
        self._notifier = notifier
        self._logger = logger
        self._cache: dict = {}
        self._quotes: dict = {}
        self.backtest = data_provider is not None

    # ------------------------------------------------------------------ time
    @property
    def now(self) -> datetime:
        return self._clock or datetime.now(timezone.utc)

    # ------------------------------------------------------------------ data
    def data(self, symbol: str, interval: str | None = None, bars: int = 300,
             closed_only: bool = True) -> pd.DataFrame:
        """OHLCV DataFrame (open/high/low/close/volume), newest bar last.
        closed_only drops the still-forming bar so signals don't repaint."""
        interval = interval or self.strategy.interval
        if self._data:
            return self._data.bars(symbol, interval, bars, self.now)
        key = (symbol, interval, bars)
        if key not in self._cache:
            df = tv.ohlcv(symbol, interval, bars + 1)
            if closed_only and len(df):
                delay = DATA_DELAY_MIN.get(symbol.split(":")[0].upper(), 0)
                visible_until = pd.Timestamp(self.now) - timedelta(minutes=delay)
                if df.index[-1] + timedelta(minutes=INTERVAL_MIN[interval]) > visible_until:
                    df = df.iloc[:-1]
            self._cache[key] = df.tail(bars)
        return self._cache[key]

    def price(self, symbol: str) -> float:
        if self._data:
            return self._data.price(symbol, self.now)
        if symbol not in self._quotes:
            self._quotes.update(tv.quote([symbol]))
        return self._quotes.get(symbol, float("nan"))

    def prices(self, symbols: list[str]) -> dict[str, float]:
        if self._data:
            return {s: self.price(s) for s in symbols}
        missing = [s for s in symbols if s not in self._quotes]
        if missing:
            self._quotes.update(tv.quote(missing))
        return {s: self._quotes.get(s) for s in symbols}

    def tv(self, symbol: str, columns: list[str]) -> dict:
        """Any TradingView screener columns for one symbol (same as MCP get_symbol_data).
        e.g. ctx.tv("NSE:TCS", ["RSI|15", "Recommend.All|60", "price_earnings_ttm"])"""
        self._live_only("ctx.tv")
        return tv.scan([symbol], columns).get(symbol, {})

    def tv_many(self, symbols: list[str], columns: list[str]) -> dict[str, dict]:
        self._live_only("ctx.tv_many")
        return tv.scan(symbols, columns)

    def technicals(self, symbol: str, interval: str | None = None) -> dict:
        """TradingView technical rating snapshot (same as MCP get_technicals_rating).
        Keys: rating (STRONG_BUY..STRONG_SELL), Recommend.All, RSI, MACD.macd, EMA20, ..."""
        self._live_only("ctx.technicals")
        return tv.technicals(symbol, interval or self.strategy.interval)

    def screener(self, **kw) -> pd.DataFrame:
        """TradingView screener (same as MCP run_screener). See engine/tv.py:screener."""
        self._live_only("ctx.screener")
        return tv.screener(**kw)

    def _live_only(self, what: str):
        if self._data:
            raise NotAvailableInBacktest(f"{what} uses live TradingView snapshots and can't be backtested")

    # ------------------------------------------------------------- portfolio
    @property
    def cash(self) -> float:
        return self.broker.pf.cash

    @property
    def memory(self) -> dict:
        """Persistent dict for your bot's own state between runs (must be JSON-serialisable)."""
        return self.broker.pf.memory

    def position(self, symbol: str) -> float:
        return self.broker.position(symbol)

    def positions(self) -> dict:
        return dict(self.broker.pf.positions)

    def equity(self) -> float:
        return self.broker.pf.equity(self.prices(list(self.broker.pf.positions)))

    # ---------------------------------------------------------------- orders
    def _qty(self, symbol, qty, value, pct) -> float:
        if qty is not None:
            return qty
        px = self.price(symbol)
        if not px or math.isnan(px):
            return 0
        if pct is not None:
            value = self.equity() * pct / 100
        if self.market in ("CRYPTO", "FOREX"):  # fractional units allowed
            return math.floor((value or 0) / px * 1e6) / 1e6
        return math.floor((value or 0) / px)

    def _levels(self, symbol, side, sl, tp, sl_pct, tp_pct):
        if sl_pct is None and tp_pct is None:
            return sl, tp
        px = self.price(symbol)
        if sl_pct is not None and sl is None:
            sl = px * (1 - sl_pct / 100) if side > 0 else px * (1 + sl_pct / 100)
        if tp_pct is not None and tp is None:
            tp = px * (1 + tp_pct / 100) if side > 0 else px * (1 - tp_pct / 100)
        return sl, tp

    def _submit(self, symbol, delta, reason, sl=None, tp=None, trail_pct=None):
        if not delta:
            return None
        if self._exec:
            return self._exec(symbol, delta, reason, sl, tp, trail_pct)
        return self.broker.order(symbol, delta, self.price(symbol), self.now.isoformat(timespec="seconds"),
                                 reason, sl, tp, trail_pct)

    def buy(self, symbol: str, qty: float | None = None, value: float | None = None,
            pct: float | None = None, sl: float | None = None, tp: float | None = None,
            sl_pct: float | None = None, tp_pct: float | None = None,
            trail_pct: float | None = None, reason: str = ""):
        """Buy by qty, by money `value`, or by `pct` of equity. Optional stop/target
        as prices (sl/tp) or percentages (sl_pct/tp_pct), and a trailing stop (trail_pct)."""
        q = self._qty(symbol, qty, value, pct)
        sl, tp = self._levels(symbol, +1, sl, tp, sl_pct, tp_pct)
        return self._submit(symbol, abs(q), reason or "buy", sl, tp, trail_pct)

    def sell(self, symbol: str, qty: float | None = None, value: float | None = None,
             pct: float | None = None, sl: float | None = None, tp: float | None = None,
             sl_pct: float | None = None, tp_pct: float | None = None,
             trail_pct: float | None = None, reason: str = ""):
        """Sell (reduce a long, or open a short if allow_short=True)."""
        q = self._qty(symbol, qty, value, pct)
        sl, tp = self._levels(symbol, -1, sl, tp, sl_pct, tp_pct)
        return self._submit(symbol, -abs(q), reason or "sell", sl, tp, trail_pct)

    def close(self, symbol: str, reason: str = "close"):
        q = self.position(symbol)
        return self._submit(symbol, -q, reason) if q else None

    def close_all(self, reason: str = "close all"):
        return [self.close(s, reason) for s in list(self.broker.pf.positions)]

    def set_stop(self, symbol: str, sl: float | None = None, tp: float | None = None):
        p = self.broker.pf.positions.get(symbol)
        if p:
            if sl is not None:
                p["sl"] = sl
            if tp is not None:
                p["tp"] = tp

    # ----------------------------------------------------------- signals/io
    def signals(self) -> list[dict]:
        """External signals addressed to this bot (e.g. written by Claude using the TradingView MCP)."""
        self._signals_read = True
        return list(self._signals)

    def log(self, *msg):
        self._logger(f"[{self.strategy.name}]", *msg)

    def notify(self, msg: str, title: str | None = None):
        if self._notifier and not self.backtest:
            self._notifier(msg, title or self.strategy.name)
        else:
            self.log("NOTIFY:", msg)
