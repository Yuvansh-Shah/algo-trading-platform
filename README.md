# Algo Trading Platform

Runs your trading bots in the cloud **for free**. Your computer can be off.

```
 GitHub Actions (free, every 15 min in NSE hours + hourly 24/7)
   └─ engine/run.py
        ├─ loads every bot in strategies/*.py
        ├─ data: TradingView public endpoints (same source as the TradingView MCP)
        ├─ paper broker per bot: stops, targets, trailing stops, intraday square-off
        ├─ phone notifications (ntfy / Telegram)
        └─ commits state/ + STATUS.md + dashboard/ back to the repo
 Claude + TradingView MCP (optional)
   └─ claude/mcp_strategies/*.md -> signals/inbox/*.json -> executed by strategies/external_signals.py
```

## Daily use

| I want to… | Do this |
|---|---|
| See how bots are doing | Open **STATUS.md** in the repo (GitHub app works) or download `dashboard/index.html` |
| Get trade alerts on my phone | Install the **ntfy** app → subscribe to your topic (see below) |
| Add a bot | Copy `strategies/_template.py` → `strategies/my_bot.py`, edit, push |
| Test a bot on history first | `python -m engine.backtest my_bot` |
| Pause a bot | `config.yaml` → `my_bot: {enabled: false}` → push |
| Run now / debug | GitHub → Actions → trading-engine → Run workflow (tick *force*) |
| Use Claude + TradingView MCP | In Claude desktop in this folder: "run my MCP strategies" |

Or just ask Claude: *"turn this idea into a bot and backtest it"*.

## Writing a bot

```python
from engine import Strategy, ta

class RsiBounce(Strategy):
    symbols = ["NSE:SBIN", "NSE:ITC"]
    interval = "15m"
    capital = 100_000
    intraday = True

    def on_bar(self, ctx):
        for sym in self.symbols:
            df = ctx.data(sym)                                  # OHLCV from TradingView
            tvr = ctx.technicals(sym, "1h")                     # TradingView rating/indicators (= MCP)
            if ta.crossover(ta.rsi(df.close), 30) and tvr["rating"] in ("BUY", "STRONG_BUY"):
                ctx.buy(sym, pct=25, sl_pct=1, tp_pct=2, reason="RSI bounce + TV buy")
```

Full `ctx` reference is at the top of `strategies/_template.py`.
Any TradingView screener column works through `ctx.tv(sym, [...])`, e.g. `"RSI|15"`,
`"Recommend.All|240"`, `"MACD.macd|60"`, `"price_earnings_ttm"`, `"market_cap_basic"`.

**About custom Pine indicators:** your own TradingView indicators run only inside TradingView and
can't be read by any API. To use one in a bot, port its logic to Python (Claude can do that from the
Pine source) using `engine/ta.py`. Built-in TradingView indicators and ratings are available directly.

## TradingView safety

The engine never logs in to TradingView. It only uses public, logged-out data endpoints, so it
**cannot see or change any account**: layouts, indicators, alerts and watchlists stay exactly as they are.
The Claude side is limited to read-only MCP tools (`CLAUDE.md` + deny rules in `.claude/settings.json`).

## Notifications

`NTFY_TOPIC` is already set as a repo secret. On your phone: install **ntfy** (Play Store / App
Store) → + → subscribe to the topic name you were given. Telegram is optional: add
`TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` secrets.

## Limits to know

- **Paper trading only.** Nothing is sent to a broker. `config.yaml → live` can forward orders
  to a webhook later, but in India SEBI's retail-algo rules need broker-registered API access from a
  static IP, which GitHub's servers don't have. See "Going live" below.
- **NSE/BSE prices are ~15 min delayed** (TradingView logged-out feed). Fine for swing and slower
  intraday bots, not for scalping. Crypto is real-time.
- **Cadence:** fastest is every 15 min (GitHub cron can also start runs 5-15 min late at busy times).
  Budget is ~1,300 of the 2,000 free Actions minutes/month on a private repo.
- **Holidays** are detected automatically (if NIFTY has no bar today, the market is shut).

## Going live later (still free)

Oracle Cloud "Always Free" VM (4 CPU / 24 GB, free static IP): `git clone`, `pip install -r
requirements.txt`, crontab `*/5 * * * * cd ~/algo && python -m engine.run && git add -A && git commit -qm run && git push`.
A static IP there lets you register with a broker API (Dhan, Angel One SmartAPI, Fyers, Upstox and
Zerodha all have free personal APIs). Add a broker adapter next to `LiveForwarder` in `engine/broker.py`.
