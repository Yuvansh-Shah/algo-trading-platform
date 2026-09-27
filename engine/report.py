"""Writes STATUS.md (readable in the GitHub app) and dashboard/index.html (equity curves)."""
from __future__ import annotations

import csv
import json
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def _read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _ist(ts: str) -> str:
    try:
        return datetime.fromisoformat(ts).astimezone(ZoneInfo("Asia/Kolkata")).strftime("%d %b %H:%M")
    except Exception:
        return ts


def build(state: Path, root: Path):
    runtime = json.loads((state / "runtime.json").read_text(encoding="utf-8")) \
        if (state / "runtime.json").exists() else {}
    trades = _read_csv(state / "trades.csv")
    equity = _read_csv(state / "equity.csv")
    pfs = {}
    for f in (state / "portfolios").glob("*.json"):
        pfs[f.stem] = json.loads(f.read_text(encoding="utf-8"))

    now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%d %b %Y %H:%M IST")
    L = [f"# Algo Trading Status", "", f"_Updated {now} · paper trading unless marked LIVE_", "",
         "| Bot | Market | TF | Equity | Total P&L | Today | Trades | Win % | Open | Last run | Health |",
         "|---|---|---|---:|---:|---:|---:|---:|---:|---|---|"]
    for name, pf in sorted(pfs.items()):
        rt = runtime.get(name, {})
        eq = rt.get("equity", pf["cash"])
        total = eq - pf["initial"]
        start = (rt.get("day") or {}).get("start_equity", eq)
        closed = pf["wins"] + pf["losses"]
        win = f"{100 * pf['wins'] / closed:.0f}%" if closed else "–"
        health = "❌ " + rt["last_error"]["msg"][:60] if rt.get("last_error") else "✅"
        L.append(f"| {name} | {rt.get('market', '')} | {rt.get('interval', '')} | {eq:,.0f} | "
                 f"{total:+,.0f} ({100 * total / pf['initial']:+.2f}%) | {eq - start:+,.0f} | {pf['trades']} | "
                 f"{win} | {len(pf['positions'])} | {_ist(rt.get('last_run', '')) if rt.get('last_run') else '–'} | {health} |")

    L += ["", "## Open positions", ""]
    rows = [(n, s, p) for n, pf in pfs.items() for s, p in pf["positions"].items()]
    if rows:
        L += ["| Bot | Symbol | Qty | Avg | Stop | Target | Opened |", "|---|---|---:|---:|---:|---:|---|"]
        for n, s, p in rows:
            f = lambda v: f"{v:,.2f}" if v else "–"
            L.append(f"| {n} | {s} | {p['qty']:g} | {p['avg']:,.2f} | {f(p.get('sl'))} | {f(p.get('tp'))} | "
                     f"{_ist(p.get('opened', ''))} |")
    else:
        L.append("_None_")

    L += ["", "## Last 25 trades", ""]
    if trades:
        L += ["| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |", "|---|---|---|---:|---|---:|---:|---|"]
        for t in trades[-25:][::-1]:
            L.append(f"| {_ist(t['time'])} | {t['strategy']} | {t['side']} | {float(t['qty']):g} | {t['symbol']} | "
                     f"{float(t['price']):,.2f} | {float(t['pnl']):+,.0f} | {t['reason']} |")
    else:
        L.append("_No trades yet_")

    errs = [(n, r["last_error"]) for n, r in runtime.items() if isinstance(r, dict) and r.get("last_error")]
    if errs:
        L += ["", "## Errors", ""]
        for n, e in errs:
            L += [f"**{n}** at {_ist(e['time'])}", "```", e.get("trace", e["msg"])[-800:], "```"]
    (root / "STATUS.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write("\n".join(L) + "\n")

    # --- dashboard
    series = defaultdict(list)
    for r in equity[-20000:]:
        series[r["strategy"]].append([r["time"], float(r["equity"])])
    data = {"updated": now, "series": series, "trades": trades[-200:],
            "bots": {n: {"initial": pf["initial"], **runtime.get(n, {})} for n, pf in pfs.items()}}
    html = (root / "engine" / "dashboard_template.html").read_text(encoding="utf-8")
    out = root / "dashboard"
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(html.replace("/*__DATA__*/null", json.dumps(data, default=str)),
                                    encoding="utf-8")
