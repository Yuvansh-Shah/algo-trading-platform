"""Writes STATUS.md (leaderboard, readable in the GitHub app) and dashboard/index.html."""
from __future__ import annotations

import csv
import json
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

MEDALS = {1: "🥇", 2: "🥈", 3: "🥉"}


def _read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _ist(ts: str) -> str:
    try:
        return datetime.fromisoformat(ts).astimezone(ZoneInfo("Asia/Kolkata")).strftime("%d %b %H:%M")
    except Exception:
        return ts or "–"


def leaderboard(state: Path) -> list[dict]:
    runtime = json.loads((state / "runtime.json").read_text(encoding="utf-8")) \
        if (state / "runtime.json").exists() else {}
    trades = _read_csv(state / "trades.csv")
    equity = _read_csv(state / "equity.csv")
    curves = defaultdict(list)
    for r in equity:
        curves[r["strategy"]].append(float(r["equity"]))
    closes = defaultdict(list)
    for t in trades:
        if t.get("kind") == "close" or (not t.get("kind") and float(t["pnl"]) != -float(t["fee"])):
            closes[t["strategy"]].append(float(t["pnl"]))

    rows = []
    for f in sorted((state / "portfolios").glob("*.json")):
        pf = json.loads(f.read_text(encoding="utf-8"))
        name, rt = f.stem, runtime.get(f.stem, {})
        eq = rt.get("equity", pf["cash"])
        start = (rt.get("day") or {}).get("start_equity", eq)
        pnls = closes.get(name, [])
        wins = [p for p in pnls if p > 0]
        losses = [-p for p in pnls if p <= 0]
        peak, mdd = pf["initial"], 0.0
        for v in curves.get(name, []):
            peak = max(peak, v)
            mdd = min(mdd, v / peak - 1)
        rows.append({
            "bot": name, "style": rt.get("style", ""), "market": rt.get("market", ""),
            "interval": rt.get("interval", ""), "description": rt.get("description", ""),
            "initial": pf["initial"], "equity": eq, "pnl": eq - pf["initial"],
            "ret": 100 * (eq / pf["initial"] - 1), "today": eq - start,
            "trades": len(pnls), "win": 100 * len(wins) / len(pnls) if pnls else None,
            "pf": sum(wins) / sum(losses) if losses and sum(losses) else (None if not wins else float("inf")),
            "avg": sum(pnls) / len(pnls) if pnls else None, "mdd": 100 * mdd,
            "open": len(pf["positions"]), "last_run": rt.get("last_run"),
            "error": (rt.get("last_error") or {}).get("msg"), "positions": pf["positions"],
        })
    rows.sort(key=lambda r: (r["ret"], r["trades"] > 0), reverse=True)
    bench = next((r["ret"] for r in rows if r["style"] == "benchmark"), None)
    for i, r in enumerate(rows, 1):
        r["rank"] = i
        r["vs_bench"] = r["ret"] - bench if bench is not None else None
    return rows


def build(state: Path, root: Path):
    rows = leaderboard(state)
    trades = _read_csv(state / "trades.csv")
    equity = _read_csv(state / "equity.csv")
    now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%d %b %Y %H:%M IST")
    f2 = lambda v, fmt: "–" if v is None else ("∞" if v == float("inf") else format(v, fmt))

    L = ["# 🏆 Bot Leaderboard", "",
         f"_Updated {now} · paper trading · every bot started with ₹50,000 (crypto in USDT)_", "",
         "| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |",
         "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    for r in rows:
        health = "❌ " + r["error"][:50] if r["error"] else "✅"
        L.append(f"| {MEDALS.get(r['rank'], r['rank'])} | **{r['bot']}** | {r['style']} {r['interval']} | "
                 f"{r['ret']:+.2f}% | {r['pnl']:+,.0f} | {r['today']:+,.0f} | "
                 f"{f2(r['vs_bench'], '+.2f')}{'%' if r['vs_bench'] is not None else ''} | {r['trades']} | "
                 f"{f2(r['win'], '.0f')} | {f2(r['pf'], '.2f')} | {r['mdd']:.1f}% | {r['open']} | {health} |")

    L += ["", "<details><summary>What each bot does</summary>", "",
          "| Bot | Strategy |", "|---|---|"]
    L += [f"| {r['bot']} | {r['description']} |" for r in rows]
    L += ["", "</details>", "", "## Open positions", ""]
    pos = [(r["bot"], s, p) for r in rows for s, p in r["positions"].items()]
    if pos:
        L += ["| Bot | Symbol | Qty | Avg | Stop | Target | Opened |", "|---|---|---:|---:|---:|---:|---|"]
        fmt = lambda v: f"{v:,.2f}" if v else "–"
        for n, s, p in pos:
            L.append(f"| {n} | {s} | {p['qty']:g} | {p['avg']:,.2f} | {fmt(p.get('sl'))} | {fmt(p.get('tp'))} | "
                     f"{_ist(p.get('opened', ''))} |")
    else:
        L.append("_None_")

    L += ["", "## Last 30 fills", ""]
    if trades:
        L += ["| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |",
              "|---|---|---|---:|---|---:|---:|---|"]
        for t in trades[-30:][::-1]:
            pnl = f"{float(t['pnl']):+,.0f}" if t.get("kind") == "close" else ""
            L.append(f"| {_ist(t['time'])} | {t['strategy']} | {t['side']} | {float(t['qty']):g} | {t['symbol']} | "
                     f"{float(t['price']):,.2f} | {pnl} | {t['reason']} |")
    else:
        L.append("_No trades yet — bots start at the next market open._")

    runtime = json.loads((state / "runtime.json").read_text(encoding="utf-8")) \
        if (state / "runtime.json").exists() else {}
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

    series = defaultdict(list)
    for r in equity[-40000:]:
        series[r["strategy"]].append([r["time"], float(r["equity"])])
    clean = [{k: v for k, v in r.items() if k != "positions"} for r in rows]
    for r in clean:
        if r["pf"] == float("inf"):
            r["pf"] = None
    data = {"updated": now, "series": series, "trades": trades[-300:], "board": clean}
    html = (root / "engine" / "dashboard_template.html").read_text(encoding="utf-8")
    out = root / "dashboard"
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(html.replace("/*__DATA__*/null", json.dumps(data, default=str)),
                                    encoding="utf-8")
