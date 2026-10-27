# Bot leaderboard

_Updated 27 Oct 2026 12:50 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **momentum_rotation** | positional 1D | +5.79% | +2,896 | -105 | +4.57% | 0 | – | – | -3.0% | 3 | ok |
| 2 | **tv_rating_swing** | swing 1D | +4.77% | +2,383 | -6 | +3.54% | 1 | 0 | 0.00 | -2.3% | 3 | ok |
| 3 | **nifty_buy_hold** | benchmark 1D | +1.22% | +611 | +86 | +0.00% | 0 | – | – | -3.0% | 1 | ok |
| 4 | **supertrend_intraday** | intraday 15m | +0.85% | +427 | -103 | -0.37% | 19 | 47 | 1.71 | -1.9% | 1 | ok |
| 5 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -1.22% | 0 | – | – | 0.0% | 0 | ok |
| 6 | **dual_momentum** | positional 1D | +0.00% | +0 | +0 | -1.22% | 0 | – | – | 0.0% | 0 | ok |
| 7 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -1.22% | 0 | – | – | 0.0% | 0 | ok |
| 8 | **ema_crossover** | intraday 15m | -0.70% | -349 | -366 | -1.92% | 33 | 36 | 1.04 | -2.6% | 2 | ok |
| 9 | **tv_rating_scalper** | intraday 15m | -2.04% | -1,018 | -227 | -3.26% | 49 | 37 | 0.82 | -4.3% | 0 | ok |
| 10 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | -490 | +1.01% | 5 | 60 | 4.63 | -0.9% | 0 | retired |
| 11 | **gap_and_go** | intraday 15m | +1.40% | +701 | -391 | +0.18% | 10 | 80 | 2.36 | -1.2% | 0 | retired |
| 12 | **vwap_pullback** | intraday 15m | +0.98% | +491 | +32 | -0.24% | 41 | 51 | 1.48 | -1.7% | 0 | retired |
| 13 | **donchian_turtle** | swing 1D | +0.79% | +395 | +0 | -0.43% | 3 | 67 | 2.04 | -2.5% | 0 | retired |
| 14 | **orb_breakout** | intraday 15m | +0.54% | +272 | -11 | -0.68% | 15 | 60 | 1.51 | -1.5% | 0 | retired |
| 15 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -1.22% | 0 | – | – | 0.0% | 0 | retired |
| 16 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -1.22% | 0 | – | – | 0.0% | 0 | retired |
| 17 | **vwap_reversion** | intraday 15m | -0.33% | -166 | +151 | -1.55% | 35 | 57 | 1.09 | -1.3% | 0 | retired |
| 18 | **bb_squeeze** | intraday 15m | -0.98% | -492 | -413 | -2.20% | 20 | 40 | 0.68 | -1.4% | 0 | retired |
| 19 | **macd_adx** | intraday 15m | -1.02% | -512 | -178 | -2.24% | 22 | 32 | 0.71 | -1.4% | 0 | retired |
| 20 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | -554 | -2.75% | 35 | 49 | 0.61 | -1.5% | 0 | retired |
| 21 | **crypto_supertrend** | crypto 1h | -8.03% | -4,014 | -495 | -9.25% | 13 | 15 | 0.05 | -8.1% | 0 | retired |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| supertrend_intraday | Supertrend 10/3 flips on 15m with the NIFTY trend, entries before 11:00; 2R |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| dual_momentum | Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| ema_crossover | EMA 9/21 cross + RSI + VWAP, with the NIFTY trend, entries before 11:00; 1.5/3 ATR |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement, with the NIFTY trend, entries before 11:00 |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,712.22 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,309.72 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:DRREDDY | 13 | 1,241.85 | 1,230.11 | – | 19 Oct 15:05 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| supertrend_intraday | NSE:RELIANCE | -14 | 1,187.96 | 1,204.52 | 1,154.96 | 27 Oct 10:45 |
| ema_crossover | NSE:TCS | -6 | 2,492.60 | 2,515.65 | 2,453.71 | 27 Oct 09:45 |
| ema_crossover | NSE:RELIANCE | -13 | 1,187.96 | 1,195.65 | 1,172.71 | 27 Oct 10:45 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 27 Oct 12:15 | tv_rating_scalper | BUY | 23 | NSE:HDFCBANK | 688.24 | -61 | 15m rating faded (+0.00) |
| 27 Oct 11:45 | ema_crossover | BUY | 14 | NSE:INFY | 1,148.63 | -202 | stop-loss |
| 27 Oct 11:40 | tv_rating_scalper | BUY | 14 | NSE:INFY | 1,144.88 | -150 | stop-loss |
| 27 Oct 10:45 | tv_rating_scalper | SELL | 23 | NSE:HDFCBANK | 685.91 |  | TV 15m -0.51 / 1h -0.51 |
| 27 Oct 10:45 | supertrend_intraday | SELL | 14 | NSE:RELIANCE | 1,187.96 |  | Supertrend flipped down |
| 27 Oct 10:45 | ema_crossover | SELL | 13 | NSE:RELIANCE | 1,187.96 |  | EMA9<21, RSI 38 |
| 27 Oct 10:00 | tv_rating_scalper | SELL | 14 | NSE:INFY | 1,134.77 |  | TV 15m -0.54 / 1h -0.22 |
| 27 Oct 10:00 | ema_crossover | SELL | 14 | NSE:INFY | 1,134.77 |  | EMA9<21, RSI 39 |
| 27 Oct 09:45 | ema_crossover | SELL | 6 | NSE:TCS | 2,492.60 |  | EMA9<21, RSI 34 |
| 26 Oct 15:15 | tv_rating_scalper | BUY | 23 | NSE:HDFCBANK | 688.29 | +18 | intraday square-off |
| 26 Oct 13:15 | ema_crossover | BUY | 11 | NSE:ICICIBANK | 1,389.58 | -65 | opposite EMA cross |
| 26 Oct 12:45 | tv_rating_scalper | BUY | 17 | NSE:SBIN | 955.69 | -137 | 15m rating faded (+0.02) |
| 26 Oct 11:00 | ema_crossover | SELL | 11 | NSE:ICICIBANK | 1,384.32 |  | EMA9<21, RSI 45 |
| 26 Oct 10:20 | tv_rating_scalper | BUY | 14 | NSE:INFY | 1,142.28 | -146 | stop-loss |
| 26 Oct 09:45 | tv_rating_scalper | SELL | 17 | NSE:SBIN | 948.11 |  | TV 15m -0.51 / 1h -0.56 |
| 26 Oct 09:35 | ema_crossover | BUY | 14 | NSE:INFY | 1,115.32 | -15 | target |
| 26 Oct 09:30 | tv_rating_scalper | SELL | 14 | NSE:INFY | 1,132.42 |  | TV 15m -0.52 / 1h -0.16 |
| 26 Oct 09:30 | tv_rating_scalper | SELL | 23 | NSE:HDFCBANK | 689.41 |  | TV 15m -0.60 / 1h -0.47 |
| 26 Oct 09:30 | tv_rating_scalper | BUY | 9 | NSE:SUNPHARMA | 1,757.95 | -61 | 15m rating faded (+0.60) |
| 26 Oct 09:25 | tv_rating_scalper | SELL | 9 | NSE:SUNPHARMA | 1,752.05 |  | TV 15m -0.51 / 1h -0.31 |
| 26 Oct 09:25 | ema_crossover | SELL | 14 | NSE:INFY | 1,114.78 |  | EMA9<21, RSI 44 |
| 23 Oct 15:15 | supertrend_intraday | BUY | 14 | NSE:INFY | 1,159.33 | -16 | intraday square-off |
| 23 Oct 15:15 | supertrend_intraday | BUY | 4 | NSE:LT | 3,636.23 | -64 | intraday square-off |
| 23 Oct 15:15 | supertrend_intraday | BUY | 38 | NSE:KOTAKBANK | 429.59 | +171 | intraday square-off |
| 23 Oct 14:30 | ema_crossover | BUY | 4 | NSE:LT | 3,651.13 | -27 | opposite EMA cross |
| 23 Oct 14:00 | tv_rating_scalper | BUY | 4 | NSE:LT | 3,646.83 | -107 | 15m rating faded (+0.38) |
| 23 Oct 14:00 | tv_rating_scalper | BUY | 14 | NSE:RELIANCE | 1,185.14 | -144 | 15m rating faded (+0.07) |
| 23 Oct 14:00 | tv_rating_scalper | BUY | 13 | NSE:AXISBANK | 1,211.94 | -155 | stop-loss |
| 23 Oct 14:00 | ema_crossover | BUY | 13 | NSE:AXISBANK | 1,211.94 | -155 | stop-loss |
| 23 Oct 12:45 | ema_crossover | BUY | 17 | NSE:SBIN | 951.79 | +186 | target |
