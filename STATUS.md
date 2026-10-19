# 🏆 Bot Leaderboard

_Updated 19 Oct 2026 09:10 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **momentum_rotation** | positional 1D | +5.02% | +2,512 | +767 | +2.29% | 0 | – | – | -1.3% | 3 | ✅ |
| 🥈 | **tv_rating_swing** | swing 1D | +4.26% | +2,130 | +652 | +1.53% | 0 | – | – | -0.4% | 3 | ✅ |
| 🥉 | **hourly_macd_swing** | swing 1h | +2.86% | +1,428 | -112 | +0.12% | 4 | 75 | 11.42 | -0.9% | 1 | ✅ |
| 4 | **nifty_buy_hold** | benchmark 1D | +2.73% | +1,367 | +438 | +0.00% | 0 | – | – | -0.8% | 1 | ✅ |
| 5 | **gap_and_go** | intraday 15m | +2.23% | +1,114 | +240 | -0.51% | 8 | 88 | 8.50 | -1.0% | 0 | ✅ |
| 6 | **donchian_turtle** | swing 1D | +2.00% | +1,000 | +461 | -0.73% | 0 | – | – | -0.5% | 3 | ✅ |
| 7 | **tv_rating_scalper** | intraday 15m | +1.14% | +568 | -416 | -1.60% | 28 | 46 | 1.52 | -1.4% | 0 | ✅ |
| 8 | **vwap_pullback** | intraday 15m | +0.92% | +459 | +351 | -1.82% | 33 | 48 | 1.57 | -1.7% | 0 | ✅ |
| 9 | **ema_crossover** | intraday 15m | +0.72% | +361 | -498 | -2.01% | 21 | 48 | 1.60 | -1.3% | 0 | ✅ |
| 10 | **supertrend_intraday** | intraday 15m | +0.71% | +355 | -643 | -2.02% | 13 | 46 | 1.53 | -1.6% | 0 | ✅ |
| 11 | **orb_breakout** | intraday 15m | +0.57% | +283 | -104 | -2.17% | 12 | 58 | 1.64 | -1.5% | 0 | ✅ |
| 12 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -2.73% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -2.73% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -2.73% | 0 | – | – | 0.0% | 0 | ✅ |
| 15 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -2.73% | 0 | – | – | 0.0% | 0 | ✅ |
| 16 | **bb_squeeze** | intraday 15m | -0.16% | -79 | -179 | -2.89% | 17 | 47 | 1.08 | -0.6% | 0 | ✅ |
| 17 | **rsi2_scalper** | scalp 15m | -0.42% | -211 | +50 | -3.16% | 30 | 57 | 1.04 | -0.8% | 0 | ✅ |
| 18 | **vwap_reversion** | intraday 15m | -0.63% | -317 | -7 | -3.37% | 29 | 55 | 0.92 | -1.3% | 0 | ✅ |
| 19 | **macd_adx** | intraday 15m | -0.67% | -333 | +50 | -3.40% | 20 | 35 | 0.82 | -1.4% | 0 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -7.05% | -3,524 | -5 | -9.78% | 11 | 18 | 0.06 | -7.4% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,665.63 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:AXISBANK | 13 | 1,286.66 | 1,201.10 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,300.33 | – | 15 Oct 15:05 |
| hourly_macd_swing | NSE:HDFCBANK | 23 | 720.34 | 710.61 | 738.03 | 15 Oct 10:30 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| donchian_turtle | NSE:ICICIBANK | 11 | 1,384.88 | 1,334.46 | – | 15 Oct 15:10 |
| donchian_turtle | NSE:INFY | 14 | 1,109.87 | 1,049.88 | – | 15 Oct 15:10 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.255042 | 82,042.44 | – | – | 16 Oct 09:00 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.57134 | 2,440.43 | – | – | 16 Oct 09:00 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 16 Oct 15:15 | vwap_reversion | SELL | 22 | NSE:HDFCBANK | 725.35 | -21 | intraday square-off |
| 16 Oct 15:15 | vwap_reversion | BUY | 6 | NSE:TCS | 2,462.59 | -83 | intraday square-off |
| 16 Oct 15:15 | vwap_pullback | SELL | 14 | NSE:INFY | 1,160.27 | +109 | intraday square-off |
| 16 Oct 15:15 | vwap_pullback | SELL | 17 | NSE:SBIN | 958.81 | -27 | intraday square-off |
| 16 Oct 15:15 | tv_rating_scalper | SELL | 17 | NSE:SBIN | 958.81 | -32 | intraday square-off |
| 16 Oct 15:15 | tv_rating_scalper | SELL | 14 | NSE:INFY | 1,160.27 | +67 | intraday square-off |
| 16 Oct 15:15 | supertrend_intraday | BUY | 37 | NSE:KOTAKBANK | 447.44 | -109 | intraday square-off |
| 16 Oct 15:15 | supertrend_intraday | BUY | 17 | NSE:SBIN | 959.19 | -125 | intraday square-off |
| 16 Oct 15:15 | supertrend_intraday | BUY | 14 | NSE:RELIANCE | 1,209.04 | -154 | intraday square-off |
| 16 Oct 15:15 | orb_breakout | BUY | 63 | NSE:ITC | 261.85 | -21 | intraday square-off |
| 16 Oct 15:15 | orb_breakout | BUY | 13 | NSE:AXISBANK | 1,283.66 | -126 | intraday square-off |
| 16 Oct 15:15 | orb_breakout | SELL | 14 | NSE:INFY | 1,160.27 | +67 | intraday square-off |
| 16 Oct 15:15 | macd_adx | SELL | 62 | NSE:ITC | 261.75 | -77 | intraday square-off |
| 16 Oct 15:15 | gap_and_go | SELL | 6 | NSE:TCS | 2,461.61 | +188 | intraday square-off |
| 16 Oct 15:15 | gap_and_go | SELL | 14 | NSE:INFY | 1,160.27 | +67 | intraday square-off |
| 16 Oct 15:15 | ema_crossover | BUY | 63 | NSE:ITC | 261.85 | +48 | intraday square-off |
| 16 Oct 15:15 | bb_squeeze | SELL | 11 | NSE:ICICIBANK | 1,393.62 | +26 | intraday square-off |
| 16 Oct 14:45 | bb_squeeze | SELL | 14 | NSE:INFY | 1,151.27 | +105 | back to mid band |
| 16 Oct 14:35 | vwap_pullback | SELL | 12 | NSE:AXISBANK | 1,281.84 | -75 | stop-loss |
| 16 Oct 14:30 | vwap_reversion | BUY | 4 | NSE:LT | 3,643.03 | +86 | back to VWAP |
| 16 Oct 14:30 | vwap_reversion | BUY | 22 | NSE:HDFCBANK | 725.95 |  | -2.3 sigma below VWAP |
| 16 Oct 14:30 | hourly_macd_swing | SELL | 13 | NSE:AXISBANK | 1,284.14 | +211 | 1h MACD bear cross |
| 16 Oct 14:30 | ema_crossover | SELL | 4 | NSE:LT | 3,641.57 | -100 | opposite EMA cross |
| 16 Oct 14:30 | ema_crossover | SELL | 12 | NSE:AXISBANK | 1,284.14 | -49 | opposite EMA cross |
| 16 Oct 14:00 | vwap_pullback | BUY | 14 | NSE:INFY | 1,151.93 |  | pullback held VWAP in uptrend |
| 16 Oct 14:00 | rsi2_scalper | SELL | 4 | NSE:LT | 3,655.77 | +2 | RSI2 snapped back (86) |
| 16 Oct 13:45 | vwap_reversion | SELL | 9 | NSE:SUNPHARMA | 1,755.95 | +56 | back to VWAP |
| 16 Oct 13:45 | tv_rating_scalper | BUY | 17 | NSE:SBIN | 960.19 |  | TV 15m +0.51 / 1h +0.25 |
| 16 Oct 13:45 | tv_rating_scalper | BUY | 9 | NSE:SUNPHARMA | 1,756.65 | -44 | 15m rating faded (+0.20) |
| 16 Oct 13:45 | macd_adx | SELL | 6 | NSE:TCS | 2,448.31 | +199 | MACD reversed |
