# Bot leaderboard

_Updated 04 Nov 2026 09:05 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **momentum_rotation** | positional 1D | +7.71% | +3,854 | -352 | +2.53% | 0 | – | – | -4.4% | 3 | ok |
| 2 | **tv_rating_swing** | swing 1D | +6.48% | +3,241 | +69 | +1.31% | 1 | 0 | 0.00 | -2.3% | 3 | ok |
| 3 | **nifty_buy_hold** | benchmark 1D | +5.18% | +2,588 | +816 | +0.00% | 0 | – | – | -3.0% | 1 | ok |
| 4 | **dual_momentum** | positional 1D | +0.71% | +353 | +454 | -4.47% | 0 | – | – | -0.4% | 1 | ok |
| 5 | **supertrend_intraday** | intraday 15m | +0.14% | +71 | +27 | -5.03% | 30 | 40 | 1.16 | -2.5% | 0 | ok |
| 6 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -5.18% | 0 | – | – | 0.0% | 0 | ok |
| 7 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -5.18% | 0 | – | – | 0.0% | 0 | ok |
| 8 | **ema_crossover** | intraday 15m | -0.32% | -159 | +476 | -5.49% | 46 | 37 | 1.07 | -3.6% | 0 | ok |
| 9 | **tv_rating_scalper** | intraday 15m | -1.78% | -889 | +526 | -6.95% | 67 | 39 | 0.92 | -5.8% | 0 | ok |
| 10 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | -490 | -2.95% | 5 | 60 | 4.63 | -0.9% | 0 | retired |
| 11 | **gap_and_go** | intraday 15m | +1.40% | +701 | -391 | -3.77% | 10 | 80 | 2.36 | -1.2% | 0 | retired |
| 12 | **vwap_pullback** | intraday 15m | +0.98% | +491 | +32 | -4.19% | 41 | 51 | 1.48 | -1.7% | 0 | retired |
| 13 | **donchian_turtle** | swing 1D | +0.79% | +395 | +0 | -4.39% | 3 | 67 | 2.04 | -2.5% | 0 | retired |
| 14 | **orb_breakout** | intraday 15m | +0.54% | +272 | -11 | -4.63% | 15 | 60 | 1.51 | -1.5% | 0 | retired |
| 15 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -5.18% | 0 | – | – | 0.0% | 0 | retired |
| 16 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -5.18% | 0 | – | – | 0.0% | 0 | retired |
| 17 | **vwap_reversion** | intraday 15m | -0.33% | -166 | +151 | -5.51% | 35 | 57 | 1.09 | -1.3% | 0 | retired |
| 18 | **bb_squeeze** | intraday 15m | -0.98% | -492 | -413 | -6.16% | 20 | 40 | 0.68 | -1.4% | 0 | retired |
| 19 | **macd_adx** | intraday 15m | -1.02% | -512 | -178 | -6.20% | 22 | 32 | 0.71 | -1.4% | 0 | retired |
| 20 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | -554 | -6.71% | 35 | 49 | 0.61 | -1.5% | 0 | retired |
| 21 | **crypto_supertrend** | crypto 1h | -8.03% | -4,014 | -495 | -13.20% | 13 | 15 | 0.05 | -8.1% | 0 | retired |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
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
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,712.22 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,329.81 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:DRREDDY | 13 | 1,241.85 | 1,267.50 | – | 19 Oct 15:05 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| dual_momentum | NSE:BANKBEES | 86 | 569.32 | – | – | 02 Nov 15:10 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
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
| 03 Nov 09:25 | tv_rating_scalper | BUY | 12 | NSE:RELIANCE | 1,288.16 |  | TV 15m +0.51 / 1h +0.40 |
| 02 Nov 15:15 | supertrend_intraday | SELL | 8 | NSE:BHARTIARTL | 1,981.50 | -100 | intraday square-off |
| 02 Nov 15:15 | supertrend_intraday | SELL | 13 | NSE:RELIANCE | 1,259.65 | +399 | intraday square-off |
| 02 Nov 15:10 | dual_momentum | BUY | 86 | NSE:BANKBEES | 569.32 |  | strongest 6M return +0.6% |
| 02 Nov 14:45 | tv_rating_scalper | SELL | 8 | NSE:BHARTIARTL | 1,980.30 | -101 | 15m rating faded (+0.00) |
| 02 Nov 14:25 | ema_crossover | SELL | 8 | NSE:BHARTIARTL | 1,981.20 | -102 | stop-loss |
| 02 Nov 13:45 | supertrend_intraday | SELL | 16 | NSE:SBIN | 970.31 | -124 | Supertrend reversed |
| 02 Nov 13:45 | ema_crossover | SELL | 16 | NSE:SBIN | 970.31 | -124 | stop-loss |
| 02 Nov 12:30 | ema_crossover | SELL | 13 | NSE:RELIANCE | 1,258.95 | +390 | target |
| 02 Nov 12:00 | tv_rating_scalper | SELL | 23 | NSE:HDFCBANK | 690.76 | -109 | 15m rating faded (-0.11) |
| 02 Nov 11:20 | tv_rating_scalper | SELL | 60 | NSE:ITC | 266.75 | -152 | stop-loss |
