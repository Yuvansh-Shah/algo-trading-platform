# Algo trading platform — notes for Claude

Free, always-on paper-trading engine. cron-job.org (user's account, job "Algo trading bots") calls the workflow's dispatch API every 5 min,
09:00-15:55 IST Mon-Fri; each call runs `python -m engine.run` once on GitHub Actions (crypto bots ride on those runs).
GitHub's own `schedule` trigger is not used (it fired hours late). The call needs the user's fine-grained GitHub token
(Actions: write on this repo) in the cron-job.org Authorization header; if runs stop, check that token first.
Public repo = unlimited minutes. State lives in `state/` and is committed back by the bot.
`STATUS.md` and `dashboard/index.html` are regenerated every run.

- Bots: one file per bot in `strategies/` (copy `strategies/_template.py`). API is documented
  at the top of that template and in `engine/strategy.py`.
- Backtest before enabling: `python -m engine.backtest <bot_name> --days 280`. Judge on a window the
  change was not tuned on (`engine.backtest.run(..., overrides=..., start=..., end=...)`), never on one live week.
  Set `TV_CACHE_DIR` when running many tests, or TradingView rate-limits (HTTP 429).
- `BACKTESTS.md` is the hand-written strategy review (last: 19 Oct 2026). Retired bots are `enabled: false`
  in `config.yaml`; they stay on the leaderboard and any open positions are closed at the next open.
- Enable/disable/override bots in `config.yaml` → `strategies:`.
- Data: `engine/tv.py` calls TradingView's public logged-out endpoints (same ones the
  TradingView MCP uses). NSE/BSE data is ~15 min delayed; crypto is real-time.
- Don't hand-edit `state/` unless asked. The bot commits it; pull before pushing.

## TradingView MCP — STRICTLY READ-ONLY (hard rule)

The TradingView account behind the MCP belongs to the user's brother and holds his full setup
(indicators, layouts, alerts, watchlists). **Never change anything on it.**

Allowed (read-only): get-ohlcv, get-technicals-rating, get-symbol-data, get-symbol-data-batch,
run-screener, get-screener-columns, search-symbols, get-news, get-news-story, get-financials,
get-financial-history, get-forecasts, get-earnings-calendar, get-dividends-calendar,
get-economic-calendar, get-economic-data, get-economic-symbols, get-documents,
get-document-view, get-alerts, get-alerts-log, list-alerts, list-watchlists, get-watchlist,
get-active-watchlist.

NEVER call: create-alert, update-alert, delete-alert, restart-alerts, stop-alerts,
create-watchlist, update-watchlist, delete-watchlist, add-to-watchlist, remove-from-watchlist.
Not even "temporarily". If a strategy seems to need one of these, stop and tell the user.
These are also denied in `.claude/settings.json`.

## MCP-driven strategies (optional, uses Claude usage)

`claude/mcp_strategies/*.md` are plain-English strategies that need the MCP itself (news,
earnings, forecasts, judgement). To run them: follow `claude/RUN_MCP_STRATEGIES.md`. Output is
signal files in `signals/inbox/`, which the free engine executes via `strategies/external_signals.py`.
