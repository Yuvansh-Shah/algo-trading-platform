# Backtest leaderboard

_Last 120 days of TradingView data · ₹50,000 per bot · fees 0.05% + slippage 0.02% per side · generated 27 Sep 2026 18:18 IST_

Past performance on a few months of data says little about the future — this is a sanity check, the live paper leaderboard in STATUS.md is the real test.

| # | Bot | Style | Period | Return | Max DD | Trades | Win % | Profit factor | Avg trade | Fees |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 🥇 | **crypto_supertrend** | crypto 1h | 30 May 2026 → 27 Sep 2026 | +8.90% | -16.4% | 71 | 38.0 | 1.34 | 74 | 1,588 |
| 🥈 | **nifty_buy_hold** | benchmark 1D | 01 Jun 2026 → 25 Sep 2026 | -0.35% | -5.8% | 0 | – | – | – | 25 |
| 🥉 | **gap_and_go** | intraday 15m | 01 Jun 2026 → 25 Sep 2026 | -0.51% | -2.6% | 35 | 54.3 | 1.01 | 1 | 551 |
| 4 | **bb_reversion_daily** | swing 1D | 01 Jun 2026 → 25 Sep 2026 | -1.64% | -2.4% | 3 | 66.7 | 1.02 | 7 | 70 |
| 5 | **connors_rsi2** | swing 1D | 01 Jun 2026 → 25 Sep 2026 | -2.65% | -4.2% | 12 | 50.0 | 0.56 | -92 | 197 |
| 6 | **donchian_turtle** | swing 1D | 01 Jun 2026 → 25 Sep 2026 | -5.76% | -6.7% | 12 | 16.7 | 0.26 | -233 | 168 |
| 7 | **hourly_macd_swing** | swing 1h | 01 Jun 2026 → 25 Sep 2026 | -6.53% | -10.9% | 84 | 29.8 | 0.68 | -31 | 1,276 |
| 8 | **supertrend_intraday** | intraday 15m | 01 Jun 2026 → 25 Sep 2026 | -7.20% | -12.7% | 306 | 45.1 | 0.91 | -4 | 4,575 |
| 9 | **ema_trend_swing** | swing 1D | 01 Jun 2026 → 25 Sep 2026 | -7.48% | -8.8% | 8 | 25.0 | 0.16 | -484 | 132 |
| 10 | **bb_squeeze** | intraday 15m | 01 Jun 2026 → 25 Sep 2026 | -10.10% | -11.2% | 302 | 36.1 | 0.78 | -9 | 4,469 |
| 11 | **ema_crossover** | intraday 15m | 01 Jun 2026 → 25 Sep 2026 | -10.76% | -14.1% | 467 | 40.0 | 0.89 | -4 | 6,747 |
| 12 | **orb_breakout** | intraday 15m | 01 Jun 2026 → 25 Sep 2026 | -13.49% | -14.6% | 335 | 40.9 | 0.75 | -13 | 4,734 |
| 13 | **macd_adx** | intraday 15m | 01 Jun 2026 → 25 Sep 2026 | -16.92% | -17.8% | 414 | 31.6 | 0.64 | -13 | 5,846 |
| 14 | **rsi2_scalper** | scalp 15m | 01 Jun 2026 → 25 Sep 2026 | -24.48% | -24.5% | 616 | 42.0 | 0.43 | -13 | 8,130 |
| 15 | **vwap_reversion** | intraday 15m | 01 Jun 2026 → 25 Sep 2026 | -25.25% | -25.4% | 773 | 48.6 | 0.68 | -10 | 10,029 |
| 16 | **vwap_pullback** | intraday 15m | 01 Jun 2026 → 25 Sep 2026 | -28.44% | -30.0% | 926 | 35.9 | 0.73 | -9 | 12,358 |

**Not backtestable** (they use live TradingView snapshots — ratings/screener — which have no history):

- external_signals — live-only (uses the live screener)
- momentum_rotation — live-only (uses the live screener)
- tv_rating_scalper — live-only (ctx.tv_many uses live TradingView snapshots and can't be backtested)
- tv_rating_swing — live-only (uses the live screener)
