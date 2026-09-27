"""Backtest a bot on historical TradingView bars with the exact same code that runs live.

    python -m engine.backtest ema_crossover            # default 3000 bars
    python -m engine.backtest ema_crossover --bars 5000

Orders placed on a bar's close fill at the NEXT bar's open (no look-ahead). Stops/targets
are checked against each bar's high/low. Results -> backtests/<bot>_trades.csv + equity.csv
"""
from __future__ import annotations

import argparse
import csv
from datetime import timedelta

import pandas as pd

from . import markets, tv
from .broker import PaperBroker, Portfolio
from .loader import ROOT, load_strategies
from .strategy import INTERVAL_MIN, Context


class BacktestData:
    def __init__(self, total_bars: int):
        self.total = total_bars
        self.frames: dict = {}

    def frame(self, symbol, interval):
        key = (symbol, interval)
        if key not in self.frames:
            self.frames[key] = tv.ohlcv(symbol, interval, min(self.total, 5000))
        return self.frames[key]

    def bars(self, symbol, interval, n, now):
        df = self.frame(symbol, interval)
        closed = df[df.index + timedelta(minutes=INTERVAL_MIN[interval]) <= now]
        return closed.tail(n)

    def price(self, symbol, now):
        for iv in sorted((iv for s, iv in self.frames if s == symbol), key=INTERVAL_MIN.get):
            b = self.bars(symbol, iv, 1, now)
            if len(b):
                return float(b.close.iloc[-1])
        return float("nan")


def run(name: str, bars: int = 3000, capital: float | None = None, fees_pct=0.05, slippage_pct=0.02,
        quiet=False):
    strategies, errors = load_strategies([name])
    if not strategies:
        raise SystemExit(f"bot {name!r} not found. {errors}")
    s = strategies[0]
    if not s.symbols:
        raise SystemExit("backtests need a fixed `symbols` list (screener-based bots can only paper-trade live)")
    market = s.market or markets.market_of_symbol(s.symbols[0])
    data = BacktestData(bars)
    step = timedelta(minutes=INTERVAL_MIN[s.interval])
    for sym in s.symbols:
        data.frame(sym, s.interval)
    timeline = data.frame(s.symbols[0], s.interval).index
    pf = Portfolio(s.name, capital or s.capital, capital or s.capital)
    trades: list[dict] = []
    broker = PaperBroker(pf, fees_pct, slippage_pct, s.allow_short, trades)
    pending: list[tuple] = []
    curve = []

    def executor(symbol, delta, reason, sl, tp, trail):
        pending.append((symbol, delta, reason, sl, tp, trail))

    ctx = Context(s, broker, market, data_provider=data, executor=executor, logger=(lambda *a: None) if quiet else print)
    s.on_start(ctx)
    warmup = min(50, len(timeline) // 5)
    for i in range(warmup, len(timeline)):
        t = timeline[i]
        when = t.isoformat()
        bar = {sym: data.frame(sym, s.interval) for sym in s.symbols}
        row = {sym: df.loc[t] for sym, df in bar.items() if t in df.index}
        # fill yesterday's orders at this bar's open
        for sym, delta, reason, sl, tp, trail in pending:
            px = row[sym].open if sym in row else data.price(sym, t)
            if delta < 0 and broker.position(sym) <= 0 and not s.allow_short:
                continue
            broker.order(sym, delta, float(px), when, reason, sl, tp, trail)
        pending.clear()
        # stops/targets inside this bar
        if pf.positions:
            opens = {k: float(v.open) for k, v in row.items()}
            broker.check_exits(opens, when, {k: float(v.high) for k, v in row.items()},
                               {k: float(v.low) for k, v in row.items()})
        ctx._clock = (t + step).to_pydatetime()
        # intraday square-off near the close
        if s.intraday and not markets.SESSIONS[market].always_open and \
                markets.minutes_to_close(market, ctx._clock) <= s.square_off_minutes:
            for sym, p in list(pf.positions.items()):
                broker.order(sym, -p["qty"], float(row[sym].close) if sym in row else data.price(sym, t),
                             when, "intraday square-off")
        else:
            s.on_bar(ctx)
        closes = {k: float(v.close) for k, v in row.items()}
        curve.append((t, pf.equity(closes)))

    eq = pd.Series([v for _, v in curve], index=[t for t, _ in curve])
    dd = (eq / eq.cummax() - 1).min() * 100
    first = data.frame(s.symbols[0], s.interval)
    bh = (first.close.iloc[-1] / first.close.iloc[warmup] - 1) * 100
    closed = pf.wins + pf.losses
    gross_win = sum(t["pnl"] for t in trades if t["pnl"] > 0)
    gross_loss = -sum(t["pnl"] for t in trades if t["pnl"] < 0)
    stats = {
        "bot": s.name, "interval": s.interval, "symbols": ", ".join(s.symbols),
        "from": str(timeline[warmup])[:16], "to": str(timeline[-1])[:16],
        "start_equity": round(pf.initial), "end_equity": round(eq.iloc[-1]),
        "return_pct": round((eq.iloc[-1] / pf.initial - 1) * 100, 2),
        "buy_hold_pct": round(bh, 2), "max_drawdown_pct": round(dd, 2),
        "fills": len(trades), "closed_trades": closed,
        "win_rate_pct": round(100 * pf.wins / closed, 1) if closed else None,
        "profit_factor": round(gross_win / gross_loss, 2) if gross_loss else None,
        "fees_paid": round(pf.fees),
    }
    out = ROOT / "backtests"
    out.mkdir(exist_ok=True)
    if trades:
        with (out / f"{s.name}_trades.csv").open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(trades[0].keys()))
            w.writeheader()
            w.writerows(trades)
    eq.rename("equity").to_csv(out / f"{s.name}_equity.csv")
    return stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bot")
    ap.add_argument("--bars", type=int, default=3000)
    ap.add_argument("--capital", type=float)
    a = ap.parse_args()
    stats = run(a.bot, a.bars, a.capital, quiet=True)
    w = max(map(len, stats))
    print("\n".join(f"{k.ljust(w)}  {v}" for k, v in stats.items()))


if __name__ == "__main__":
    main()
