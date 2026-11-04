# Bot leaderboard

_Updated 04 Nov 2026 14:50 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **tv_rating_swing** | swing 1D | +6.51% | +3,253 | -157 | +0.47% | 1 | 0 | 0.00 | -2.3% | 3 | ok |
| 2 | **nifty_buy_hold** | benchmark 1D | +6.04% | +3,020 | +438 | +0.00% | 0 | – | – | -3.0% | 1 | ok |
| 3 | **momentum_rotation** | positional 1D | +6.00% | +2,999 | -831 | -0.04% | 0 | – | – | -4.4% | 3 | ok |
| 4 | **dual_momentum** | positional 1D | +1.49% | +746 | +385 | -4.55% | 0 | – | – | -0.6% | 1 | ok |
| 5 | **supertrend_intraday** | intraday 15m | +0.14% | +71 | +0 | -5.90% | 30 | 40 | 1.16 | -2.5% | 0 | ok |
| 6 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -6.04% | 0 | – | – | 0.0% | 0 | ok |
| 7 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -6.04% | 0 | – | – | 0.0% | 0 | ok |
| 8 | **ema_crossover** | intraday 15m | -0.59% | -296 | -137 | -6.63% | 47 | 36 | 1.03 | -3.6% | 0 | ok |
| 9 | **tv_rating_scalper** | intraday 15m | -0.83% | -414 | +508 | -6.87% | 71 | 39 | 1.01 | -5.8% | 1 | ok |
| 10 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | -490 | -3.81% | 5 | 60 | 4.63 | -0.9% | 0 | retired |
| 11 | **gap_and_go** | intraday 15m | +1.40% | +701 | -391 | -4.64% | 10 | 80 | 2.36 | -1.2% | 0 | retired |
| 12 | **vwap_pullback** | intraday 15m | +0.98% | +491 | +32 | -5.06% | 41 | 51 | 1.48 | -1.7% | 0 | retired |
| 13 | **donchian_turtle** | swing 1D | +0.79% | +395 | +0 | -5.25% | 3 | 67 | 2.04 | -2.5% | 0 | retired |
| 14 | **orb_breakout** | intraday 15m | +0.54% | +272 | -11 | -5.50% | 15 | 60 | 1.51 | -1.5% | 0 | retired |
| 15 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -6.04% | 0 | – | – | 0.0% | 0 | retired |
| 16 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -6.04% | 0 | – | – | 0.0% | 0 | retired |
| 17 | **vwap_reversion** | intraday 15m | -0.33% | -166 | +151 | -6.37% | 35 | 57 | 1.09 | -1.3% | 0 | retired |
| 18 | **bb_squeeze** | intraday 15m | -0.98% | -492 | -413 | -7.02% | 20 | 40 | 0.68 | -1.4% | 0 | retired |
| 19 | **macd_adx** | intraday 15m | -1.02% | -512 | -178 | -7.06% | 22 | 32 | 0.71 | -1.4% | 0 | retired |
| 20 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | -554 | -7.57% | 35 | 49 | 0.61 | -1.5% | 0 | retired |
| 21 | **crypto_supertrend** | crypto 1h | -8.03% | -4,014 | -495 | -14.07% | 13 | 15 | 0.05 | -8.1% | 0 | retired |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| dual_momentum | Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash |
| supertrend_intraday | Supertrend 10/3 flips on 15m with the NIFTY trend, entries before 11:00; 2R |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
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
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,712.22 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,335.76 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:DRREDDY | 13 | 1,241.85 | 1,279.40 | – | 19 Oct 15:05 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| dual_momentum | NSE:BANKBEES | 86 | 569.32 | – | – | 02 Nov 15:10 |
| tv_rating_scalper | NSE:RELIANCE | 12 | 1,302.16 | 1,291.48 | 1,322.73 | 04 Nov 09:25 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 04 Nov 12:15 | tv_rating_scalper | SELL | 9 | NSE:SUNPHARMA | 1,786.64 | -168 | stop-loss |
| 04 Nov 11:20 | tv_rating_scalper | SELL | 4 | NSE:LT | 3,935.31 | -146 | stop-loss |
| 04 Nov 11:15 | ema_crossover | SELL | 4 | NSE:LT | 3,939.41 | -129 | stop-loss |
| 04 Nov 11:00 | tv_rating_scalper | BUY | 9 | NSE:SUNPHARMA | 1,804.36 |  | TV 15m +0.51 / 1h +0.56 |
| 04 Nov 11:00 | tv_rating_scalper | SELL | 9 | NSE:SUNPHARMA | 1,803.64 | +292 | target |
| 04 Nov 09:45 | tv_rating_scalper | BUY | 4 | NSE:LT | 3,969.79 |  | TV 15m +0.65 / 1h +0.51 |
| 04 Nov 09:45 | ema_crossover | BUY | 4 | NSE:LT | 3,969.79 |  | EMA9>21, RSI 70 |
| 04 Nov 09:35 | tv_rating_scalper | SELL | 59 | NSE:ITC | 280.19 | +419 | target |
| 04 Nov 09:25 | tv_rating_scalper | BUY | 9 | NSE:SUNPHARMA | 1,770.25 |  | TV 15m +0.56 / 1h +0.27 |
| 04 Nov 09:25 | tv_rating_scalper | BUY | 59 | NSE:ITC | 272.95 |  | TV 15m +0.56 / 1h +0.60 |
| 04 Nov 09:25 | tv_rating_scalper | BUY | 12 | NSE:RELIANCE | 1,302.16 |  | TV 15m +0.56 / 1h +0.51 |
| 03 Nov 15:15 | tv_rating_scalper | SELL | 12 | NSE:RELIANCE | 1,297.44 | +104 | intraday square-off |
| 03 Nov 15:15 | tv_rating_scalper | SELL | 60 | NSE:ITC | 271.95 | +327 | target |
| 03 Nov 15:15 | supertrend_intraday | SELL | 13 | NSE:AXISBANK | 1,229.65 | +47 | intraday square-off |
| 03 Nov 15:15 | supertrend_intraday | SELL | 11 | NSE:ICICIBANK | 1,422.92 | +225 | intraday square-off |
| 03 Nov 14:55 | tv_rating_scalper | SELL | 22 | NSE:HDFCBANK | 724.36 | +246 | target |
| 03 Nov 13:35 | ema_crossover | SELL | 13 | NSE:AXISBANK | 1,239.15 | +177 | target |
| 03 Nov 12:45 | ema_crossover | SELL | 11 | NSE:ICICIBANK | 1,420.52 | +170 | target |
| 03 Nov 11:45 | ema_crossover | SELL | 8 | NSE:BHARTIARTL | 2,024.60 | +153 | target |
| 03 Nov 11:15 | supertrend_intraday | SELL | 6 | NSE:TCS | 2,486.50 | -221 | Supertrend reversed |
| 03 Nov 10:30 | tv_rating_scalper | BUY | 60 | NSE:ITC | 266.35 |  | TV 15m +0.56 / 1h +0.42 |
| 03 Nov 10:00 | tv_rating_scalper | SELL | 4 | NSE:LT | 3,926.21 | -142 | stop-loss |
| 03 Nov 10:00 | ema_crossover | BUY | 13 | NSE:AXISBANK | 1,224.94 |  | EMA9>21, RSI 69 |
| 03 Nov 10:00 | ema_crossover | BUY | 11 | NSE:ICICIBANK | 1,404.38 |  | EMA9>21, RSI 74 |
| 03 Nov 09:45 | supertrend_intraday | BUY | 13 | NSE:AXISBANK | 1,225.44 |  | Supertrend flipped up |
| 03 Nov 09:45 | supertrend_intraday | BUY | 6 | NSE:TCS | 2,522.10 |  | Supertrend flipped up |
| 03 Nov 09:45 | supertrend_intraday | BUY | 11 | NSE:ICICIBANK | 1,401.78 |  | Supertrend flipped up |
| 03 Nov 09:45 | ema_crossover | BUY | 8 | NSE:BHARTIARTL | 2,004.40 |  | EMA9>21, RSI 70 |
| 03 Nov 09:30 | tv_rating_scalper | BUY | 22 | NSE:HDFCBANK | 712.79 |  | TV 15m +0.65 / 1h +0.60 |
| 03 Nov 09:25 | tv_rating_scalper | BUY | 4 | NSE:LT | 3,959.69 |  | TV 15m +0.51 / 1h +0.49 |
