# Run the MCP strategies

Say to Claude (desktop app, in this folder): **"run my MCP strategies"**, or paste this file
as the prompt of a scheduled task / routine.

## Instructions for Claude

1. `git pull` so you have the latest bot state.
2. For each file in `claude/mcp_strategies/` whose front-matter says `enabled: true`:
   - Read it and follow its rules using ONLY the read-only TradingView MCP tools listed in
     `CLAUDE.md`. Never create/update/delete alerts or watchlists — that TradingView account
     is the user's brother's personal setup.
   - Check current holdings of the target bot in `state/portfolios/<bot>.json` so you don't
     re-buy what's already held, and so exits refer to real positions.
3. Write all resulting signals to ONE file `signals/inbox/<YYYYMMDD-HHMM>-<strategy>.json`
   (a JSON list). Format:
   ```json
   {"strategy": "external_signals", "symbol": "NSE:TCS", "action": "buy",
    "pct": 20, "sl_pct": 3, "tp_pct": 6,
    "reason": "one line why, citing the MCP data", "expires": "<ISO UTC, ~1 trading day ahead>"}
   ```
   `action` is buy / sell / close. Size with `qty`, `value` (₹) or `pct` (of bot equity).
   If nothing qualifies, write no file.
4. Commit only that file and push to `main`
   (`git add signals/inbox && git commit -m "mcp signals" && git pull --rebase && git push`).
   The running market session pulls it within 5 minutes and executes the signals while NSE is open.
5. Reply with a 3-5 line summary: what was scanned, what was signalled, and why.
