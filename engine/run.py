"""Engine entry point: `python -m engine.run` (GitHub Actions calls this every 15 min).

For each bot: skip if its market is closed -> manage stops/targets -> intraday square-off
-> call on_bar() if a new bar has closed -> record equity. Then write STATUS.md + dashboard.
"""
from __future__ import annotations

import argparse
import csv
import json
import shutil
import traceback
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

from . import markets, notify, report
from .broker import LiveForwarder, PaperBroker, Portfolio
from .loader import ROOT, load_strategies
from .strategy import INTERVAL_MIN, Context, Strategy

STATE = ROOT / "state"
INBOX = ROOT / "signals" / "inbox"
PROCESSED = ROOT / "signals" / "processed"
TRADE_FIELDS = ["time", "strategy", "symbol", "side", "qty", "price", "fee", "pnl",
                "position_after", "kind", "reason", "live"]


def load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")


def load_config() -> dict:
    return yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8")) or {}


def market_for(s: Strategy) -> str:
    return s.market or (markets.market_of_symbol(s.symbols[0]) if s.symbols else "NSE")


def bar_key(s: Strategy, market: str, now: datetime) -> str | None:
    """Identifier of the latest *closed* bar period; None = not due yet today (daily bots)."""
    mins = INTERVAL_MIN[s.interval]
    if mins < 1440:
        return str(int(now.timestamp() // 60 // mins))
    sess = markets.SESSIONS[market]
    local = now.astimezone(ZoneInfo(sess.tz))
    run_at = s.run_at or ("00:05" if sess.always_open else
                          f"{(sess.close.hour * 60 + sess.close.minute - 25) // 60:02d}:"
                          f"{(sess.close.hour * 60 + sess.close.minute - 25) % 60:02d}")
    hh, mm = map(int, run_at.split(":"))
    if (local.hour, local.minute) < (hh, mm):
        return None
    if mins == 1440:
        return local.date().isoformat()
    if mins == 10080:
        return f"{local.isocalendar()[0]}-W{local.isocalendar()[1]}" if local.weekday() >= 4 else None
    return f"{local.year}-{local.month}"


def load_signals() -> dict[str, list]:
    by_strategy: dict[str, list] = {}
    now = datetime.now(timezone.utc)
    for f in sorted(INBOX.glob("*.json")):
        raw = load_json(f, None)
        items = raw if isinstance(raw, list) else [raw] if raw else []
        for sig in items:
            exp = sig.get("expires")
            try:
                if exp and datetime.fromisoformat(exp.replace("Z", "+00:00")) < now:
                    continue
            except ValueError:
                pass
            sig["_file"] = f.name
            by_strategy.setdefault(sig.get("strategy", "external_signals"), []).append(sig)
    return by_strategy


def archive_signals(consumed_by: set[str], by_strategy: dict[str, list]):
    """Move an inbox file out once every signal in it was read (or expired/unaddressed)."""
    pending = {sig["_file"] for strat, sigs in by_strategy.items()
               if strat not in consumed_by for sig in sigs}
    PROCESSED.mkdir(parents=True, exist_ok=True)
    for f in INBOX.glob("*.json"):
        if f.name not in pending:
            shutil.move(str(f), PROCESSED / f.name)


def append_trades(trades: list[dict]):
    if not trades:
        return
    path = STATE / "trades.csv"
    new = not path.exists()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=TRADE_FIELDS, extrasaction="ignore")
        if new:
            w.writeheader()
        w.writerows(trades)


def append_equity(rows: list[tuple]):
    if not rows:
        return
    path = STATE / "equity.csv"
    new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["time", "strategy", "equity", "cash", "open_positions"])
        w.writerows(rows)


def fmt_trade(t: dict) -> str:
    pnl = f" | P&L {t['pnl']:+,.0f}" if t.get("pnl") and abs(t["pnl"]) > t["fee"] else ""
    return f"{t['side']} {t['qty']:g} {t['symbol']} @ {t['price']:,.2f}{pnl} ({t['reason']})"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="comma-separated bot names to run")
    ap.add_argument("--force", action="store_true", help="run on_bar now, ignoring market hours/schedule")
    args = ap.parse_args(argv)

    cfg = load_config()
    now = datetime.now(timezone.utc)
    stamp = now.isoformat(timespec="seconds")
    only = [x.strip() for x in args.only.split(",")] if args.only else None
    strategies, load_errors = load_strategies(only)
    runtime = load_json(STATE / "runtime.json", {})
    signals = load_signals()
    consumed: set[str] = set()
    all_trades, equity_rows, messages = [], [], []
    overrides = cfg.get("strategies") or {}
    notify_trades = cfg.get("notify", {}).get("trades", True)

    for err in load_errors:
        print(err)
        messages.append(("Strategy file error", err.splitlines()[0]))

    for s in strategies:
        o = overrides.get(s.name) or {}
        enabled = o.get("enabled", s.enabled)
        if not enabled:
            continue
        for k in ("capital", "interval", "symbols", "intraday", "live", "run_at"):
            if k in o:
                setattr(s, k, o[k])
        market = market_for(s)
        rt = runtime.setdefault(s.name, {})
        pf_path = STATE / "portfolios" / f"{s.name}.json"
        pf = (Portfolio.from_json(load_json(pf_path, {})) if pf_path.exists()
              else Portfolio(s.name, float(s.capital), float(s.capital)))
        trades: list[dict] = []
        live = LiveForwarder(cfg.get("live")) if (s.live and cfg.get("live", {}).get("enabled")) else None
        broker = PaperBroker(pf, cfg.get("fees_pct", 0.05), cfg.get("slippage_pct", 0.02),
                             s.allow_short, trades, live)
        ctx = Context(s, broker, market, signals=signals.get(s.name, []),
                      notifier=lambda m, t: notify.send(m, t))

        rt["market"], rt["interval"] = market, s.interval
        rt["style"] = s.style
        rt["description"] = s.description or (s.__doc__ or "").strip().splitlines()[0] if (s.description or s.__doc__) else ""
        is_open = markets.is_open(market)
        if not is_open and not args.force:
            if s.intraday and pf.positions:  # left open by a missed run -> flatten at next chance
                rt["note"] = "intraday positions pending square-off at next open"
            save_json(pf_path, pf.to_json())
            continue
        try:
            when = stamp
            # 1) stops / targets / trailing stops
            if pf.positions:
                broker.check_exits(ctx.prices(list(pf.positions)), when)
            # 2) intraday square-off (near close, or stale positions from a previous day)
            local_today = markets.local_now(market).date().isoformat()
            stale = any(p.get("opened", "")[:10] < (now.date().isoformat())
                        for p in pf.positions.values()) if s.intraday else False
            closing = s.intraday and not args.force and not markets.SESSIONS[market].always_open and \
                markets.minutes_to_close(market) <= s.square_off_minutes
            if s.intraday and pf.positions and (closing or stale):
                ctx.close_all("intraday square-off")
            # 3) strategy logic on each new closed bar
            key = bar_key(s, market, now)
            due = args.force or (key is not None and rt.get("last_bar") != key)
            if due and not closing:
                if not rt.get("started"):
                    s.on_start(ctx)
                    rt["started"] = True
                s.on_bar(ctx)
                rt["last_bar"] = key
                rt["last_run"] = stamp
                rt.pop("last_error", None)
            if ctx._signals_read or not signals.get(s.name):
                consumed.add(s.name)
            # 4) bookkeeping
            eq = pf.equity(ctx.prices(list(pf.positions)) if pf.positions else {})
            day = rt.get("day") or {}
            if day.get("date") != local_today:
                rt["day"] = {"date": local_today, "start_equity": round(eq, 2)}
            rt["equity"] = round(eq, 2)
            equity_rows.append((stamp, s.name, round(eq, 2), round(pf.cash, 2), len(pf.positions)))
        except Exception as e:
            tb = traceback.format_exc(limit=6)
            print(f"[{s.name}] ERROR\n{tb}")
            first_today = rt.get("last_error", {}).get("msg") != str(e)
            rt["last_error"] = {"time": stamp, "msg": str(e), "trace": tb[-1500:]}
            if first_today:
                messages.append((f"{s.name} crashed", str(e)[:300]))
        save_json(pf_path, pf.to_json())
        if trades:
            print(f"[{s.name}] " + "\n".join(fmt_trade(t) for t in trades))
            if notify_trades:
                notify.send("\n".join(fmt_trade(t) for t in trades), f"{s.name} ({market})",
                            tags="moneybag")
        all_trades += trades

    # unknown-strategy signals: archive so they don't pile up forever
    known = {s.name for s in strategies}
    consumed |= {k for k in signals if k not in known}
    archive_signals(consumed, signals)

    append_trades(all_trades)
    append_equity(equity_rows)

    # daily summary after the Indian close
    ist = datetime.now(ZoneInfo("Asia/Kolkata"))
    meta = runtime.setdefault("_meta", {})
    if cfg.get("notify", {}).get("daily_summary", True) and ist.weekday() < 5 and \
            (ist.hour, ist.minute) >= (15, 35) and meta.get("last_summary") != ist.date().isoformat():
        save_json(STATE / "runtime.json", runtime)
        board = report.leaderboard(STATE)
        lines = [f"{r['rank']}. {r['bot']}: {r['ret']:+.2f}% (today {r['today']:+,.0f})" for r in board[:5]]
        if len(board) > 5:
            lines.append("...")
            lines += [f"{r['rank']}. {r['bot']}: {r['ret']:+.2f}%" for r in board[-3:]]
        if lines:
            notify.send("\n".join(lines), "Daily summary", tags="bar_chart")
        meta["last_summary"] = ist.date().isoformat()
    meta["last_engine_run"] = stamp

    for title, msg in messages:
        notify.send(msg, title, tags="warning", priority="high")

    save_json(STATE / "runtime.json", runtime)
    report.build(STATE, ROOT)
    print(f"done: {len(strategies)} bots, {len(all_trades)} trades")


if __name__ == "__main__":
    main()
