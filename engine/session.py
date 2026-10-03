"""Market-session loop: `python -m engine.session`.

GitHub's cron is best-effort and drops most daytime triggers, so instead ONE job starts
before the NSE open and stays awake for the whole session:

    every 5 min: git pull -> python -m engine.run -> commit + push state

GitHub-hosted jobs are capped at 6 hours, so after ~5h40m the job dispatches its own successor
(workflow_dispatch is allowed with GITHUB_TOKEN) and exits; the successor picks up where it left off.
Exits for the day after the close (final run sends the leaderboard summary) or on a holiday.
"""
from __future__ import annotations

import os
import subprocess
import sys
import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from . import markets

IST = ZoneInfo("Asia/Kolkata")
EVERY_MIN = 5
JOB_BUDGET = timedelta(minutes=340)   # hand over before GitHub's 360-min job limit
OPEN, END = (9, 15), (15, 40)          # loop window (IST); 15:40 run sends the daily summary


def sh(*cmd: str, check: bool = False) -> int:
    print("$", " ".join(cmd), flush=True)
    return subprocess.run(cmd, check=check).returncode


def save_state(label: str):
    sh("git", "add", "-A", "state", "signals", "STATUS.md", "dashboard")
    if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode == 0:
        return
    sh("git", "commit", "-q", "-m", f"engine run {label}")
    for _ in range(4):
        if sh("git", "pull", "--rebase", "-q", "-X", "theirs", "origin", "main") == 0 and sh("git", "push", "-q") == 0:
            return
        time.sleep(5)
    print("WARNING: could not push state this round", flush=True)


def run_engine(final: bool = False):
    env = dict(os.environ)
    if not final:
        env.pop("GITHUB_STEP_SUMMARY", None)  # only the last run writes the job summary
    sh("git", "pull", "--rebase", "-q", "-X", "theirs", "origin", "main")  # pick up new bots / signals
    rc = subprocess.run([sys.executable, "-m", "engine.run"], env=env).returncode
    if rc:
        print(f"engine exited {rc}", flush=True)
    save_state(datetime.now(IST).strftime("%Y-%m-%d %H:%M IST"))


def dispatch_successor():
    rc = sh("gh", "workflow", "run", "engine.yml", "--ref", "main", "-f", "mode=session")
    print("successor dispatched" if rc == 0 else "successor dispatch FAILED (backup crons will retry)", flush=True)


def main():
    started = datetime.now(IST)
    if started.weekday() >= 5:
        print("weekend - nothing to do")
        return
    holiday_checked = False
    while True:
        now = datetime.now(IST)
        hm = (now.hour, now.minute)
        if hm >= END:
            run_engine(final=True)  # daily leaderboard summary (deduplicated by the engine)
            print("session over for today")
            return
        if hm < OPEN:
            wait = (now.replace(hour=OPEN[0], minute=OPEN[1], second=30) - now).total_seconds()
            print(f"pre-open, sleeping {wait / 60:.0f} min", flush=True)
            time.sleep(max(wait, 1))
            continue
        if not holiday_checked and hm >= (9, 50):
            holiday_checked = True
            if not markets.is_open("NSE"):
                print("NSE has no bars today - holiday. Exiting.")
                run_engine(final=True)
                return
        run_engine()
        if datetime.now(IST) - started > JOB_BUDGET:
            dispatch_successor()
            return
        now = datetime.now(IST)
        nxt = now.replace(second=20, microsecond=0) + timedelta(minutes=EVERY_MIN - now.minute % EVERY_MIN)
        time.sleep(max((nxt - now).total_seconds(), 5))


if __name__ == "__main__":
    main()
