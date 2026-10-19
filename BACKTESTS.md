# Strategy review, 19 Oct 2026

Inputs: the first live paper week (13 to 19 Oct, 5 sessions, 540 fills) and walk-forward backtests on
TradingView history. Each idea was tuned on an earlier window and judged on a later one it never saw.

| Bot type | Tuning window | Unseen window | NIFTY buy and hold (unseen) |
|---|---|---|---|
| Intraday (15m bars) | 20 Jan to 30 Jun 2026 | 1 Jul to 19 Oct 2026 | about flat |
| Daily swing and positional | Jul 2019 to Dec 2023 | Jan 2024 to Oct 2026 | +8.2% |
| Hourly swing | Jan 2024 to Jun 2025 | Jul 2025 to Oct 2026 | |

Costs per side: 0.05% intraday, 0.11% held overnight (0.1% STT on buy and sell), 0.02% slippage.
Stock universes are today's NIFTY 50 names, so long-term stock results are flattered by survivorship.

## What the live week showed

| | Trades | Net (Rs) |
|---|---:|---:|
| Intraday longs | 170 | +2,675 |
| Intraday shorts | 86 | -2,221 |
| Entries 09:00 to 11:00 | 157 | +3,247 |
| Entries after 11:00 | 99 | -2,791 |
| Intraday gross before costs | 256 | +4,521 |
| Intraday costs | | -4,067 |

96% of trades closed by a stop-loss later traded back above their entry the same day. One rising
week, so each of these was tested on history before acting on it.

## Intraday: no edge before costs

Over Jan to Oct 2026 none of the nine indicator bots made money in the tuning window under any variant.
Before costs, results averaged between -0.09% and +0.03% per fill, so costs are not hiding a profitable
strategy: on 15-minute-delayed data these setups do not predict the next move. Two filters cut losses in
every bot: entries only before 11:00, and trading only in the direction of the NIFTY trend (NIFTY above
or below its 20-day EMA). Wider stops did not help on history, so the live-week stop pattern was the
rising market.

Unseen-window return, Jul to Oct 2026, Rs 50,000 account:

| Bot | As built | Mornings + NIFTY trend | Decision |
|---|---:|---:|---|
| ema_crossover | -11.5% | -0.9% | kept, with both filters |
| supertrend_intraday | -7.3% | +1.3% | kept, with both filters (tuning window -14.2%) |
| orb_breakout | -9.3% | -9.2% | retired |
| gap_and_go | -3.3% | 0.0% (9 trades) | retired |
| bb_squeeze | -12.2% | -4.5% | retired |
| macd_adx | -14.7% | -5.5% | retired |
| rsi2_scalper | -22.7% | -3.2% | retired |
| vwap_reversion | -25.8% | -2.4% | retired |
| vwap_pullback | -27.7% | -16.3% | retired |

The two kept intraday bots are near breakeven, not proven earners. They stay so the live leaderboard keeps
an intraday comparison. `tv_rating_scalper` uses live TradingView ratings, which have no history; it gets
the same two filters.

## Swing and positional

| Bot | Tuning 2019 to 2023 | Unseen 2024 to Oct 2026 | Decision |
|---|---:|---:|---|
| dual_momentum (new) | +52.1% | +112.5% | added |
| bb_reversion_daily | +22.5% | +2.0% | kept |
| turn_of_month (candidate) | +39.5% | -1.1% | not added |
| high52_momentum (candidate) | +94.7% | -11.7% | not added |
| ema_trend_swing | +46.1% | -7.5% | retired |
| connors_rsi2 | +8.5% | -15.2% | retired |
| donchian_turtle | -3.3% | -17.5% | retired |
| hourly_macd_swing | -13.5% (2024 to mid 2025) | -23.1% | retired |
| nifty_buy_hold | +90.2% | +8.2% | benchmark |

`dual_momentum` made about 5 decisions in the unseen window: it held Nifty Next 50 through 2024, then gold
from Jan 2025 to Jul 2026 while gold rose 78%. The result is real but rests on one gold trend; from 2019 to
2023 it trailed buy and hold (+52% against +90%). It is in the arena as a low-cost diversifier.

`tv_rating_swing` and `momentum_rotation` use the live screener, so they cannot be backtested. Both were
up in the live week (+2.2% and +4.4%) and stay on.

`crypto_supertrend` lost 7% in the live week and is only checked during NSE hours, so it cannot manage
its positions overnight. Retired; NSE is the priority.

## What would actually make more money

1. Hold longer. Every strategy with an edge in these tests trades a few times a month or less; costs
   swamp anything that trades several times a day.
2. Real-time data. Intraday signals here arrive 15 minutes late. A broker data feed (with a static IP,
   see README) is the precondition for any intraday edge.
3. Judge on months, not days. One week of live results ranked `hourly_macd_swing` first; on two years
   of history it lost 23%.

Re-run any test: `python -m engine.backtest <bot> --days 280`.
