# 🏆 Bot Leaderboard

_Updated 15 Oct 2026 14:00 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **momentum_rotation** | positional 1D | +3.12% | +1,561 | +575 | +0.88% | 0 | – | – | -1.3% | 3 | ✅ |
| 🥈 | **hourly_macd_swing** | swing 1h | +2.78% | +1,389 | +810 | +0.54% | 2 | 50 | 6.74 | -0.9% | 3 | ✅ |
| 🥉 | **tv_rating_scalper** | intraday 15m | +2.27% | +1,137 | +327 | +0.04% | 18 | 56 | 2.03 | -0.9% | 3 | ✅ |
| 4 | **nifty_buy_hold** | benchmark 1D | +2.24% | +1,119 | +906 | +0.00% | 0 | – | – | -0.8% | 1 | ✅ |
| 5 | **supertrend_intraday** | intraday 15m | +2.20% | +1,100 | +807 | -0.04% | 6 | 50 | 2.38 | -0.5% | 3 | ✅ |
| 6 | **ema_crossover** | intraday 15m | +2.00% | +1,000 | +726 | -0.24% | 14 | 57 | 3.46 | -0.4% | 1 | ✅ |
| 7 | **gap_and_go** | intraday 15m | +1.83% | +916 | +19 | -0.41% | 4 | 100 | ∞ | -0.7% | 2 | ✅ |
| 8 | **tv_rating_swing** | swing 1D | +1.13% | +564 | +365 | -1.11% | 0 | – | – | -0.3% | 1 | ✅ |
| 9 | **orb_breakout** | intraday 15m | +0.99% | +494 | +49 | -1.25% | 7 | 71 | 1.83 | -0.6% | 2 | ✅ |
| 10 | **vwap_pullback** | intraday 15m | +0.41% | +206 | +632 | -1.83% | 23 | 43 | 1.29 | -1.7% | 3 | ✅ |
| 11 | **donchian_turtle** | swing 1D | +0.41% | +204 | +283 | -1.83% | 0 | – | – | -0.5% | 1 | ✅ |
| 12 | **bb_squeeze** | intraday 15m | +0.32% | +162 | +286 | -1.91% | 9 | 44 | 0.88 | -0.6% | 2 | ✅ |
| 13 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -2.24% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -2.24% | 0 | – | – | 0.0% | 0 | ✅ |
| 15 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -2.24% | 0 | – | – | 0.0% | 0 | ✅ |
| 16 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -2.24% | 0 | – | – | 0.0% | 0 | ✅ |
| 17 | **rsi2_scalper** | scalp 15m | -0.23% | -116 | -58 | -2.47% | 21 | 57 | 1.12 | -0.5% | 1 | ✅ |
| 18 | **macd_adx** | intraday 15m | -0.69% | -345 | +207 | -2.93% | 13 | 38 | 0.69 | -1.4% | 1 | ✅ |
| 19 | **vwap_reversion** | intraday 15m | -0.98% | -489 | -3 | -3.22% | 18 | 50 | 0.73 | -1.3% | 3 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -7.02% | -3,511 | +0 | -9.26% | 11 | 18 | 0.06 | -7.1% | 0 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| hourly_macd_swing | NSE:AXISBANK | 13 | 1,267.25 | 1,254.59 | 1,315.81 | 15 Oct 09:25 |
| hourly_macd_swing | NSE:HDFCBANK | 23 | 720.34 | 710.61 | 738.03 | 15 Oct 10:30 |
| hourly_macd_swing | NSE:ICICIBANK | 12 | 1,364.17 | 1,347.36 | 1,397.28 | 15 Oct 11:30 |
| tv_rating_scalper | NSE:ITC | 63 | 262.55 | 260.40 | 266.70 | 15 Oct 09:30 |
| tv_rating_scalper | NSE:KOTAKBANK | 37 | 443.84 | 440.20 | 450.85 | 15 Oct 11:00 |
| tv_rating_scalper | NSE:HDFCBANK | 23 | 727.25 | 721.28 | 738.73 | 15 Oct 13:45 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| supertrend_intraday | NSE:AXISBANK | 13 | 1,267.25 | 1,255.50 | 1,314.00 | 15 Oct 09:25 |
| supertrend_intraday | NSE:HDFCBANK | 23 | 717.04 | 706.73 | 736.80 | 15 Oct 09:45 |
| supertrend_intraday | NSE:ICICIBANK | 12 | 1,359.57 | 1,339.86 | 1,395.18 | 15 Oct 09:45 |
| ema_crossover | NSE:SUNPHARMA | 9 | 1,758.05 | 1,747.36 | 1,778.08 | 15 Oct 10:30 |
| gap_and_go | NSE:INFY | 15 | 1,099.22 | 1,069.45 | 1,131.85 | 15 Oct 09:25 |
| gap_and_go | NSE:TCS | 7 | 2,380.38 | 2,335.00 | 2,468.20 | 15 Oct 10:15 |
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,526.69 | – | 14 Oct 15:05 |
| orb_breakout | NSE:AXISBANK | 13 | 1,267.25 | 1,259.30 | 1,306.40 | 15 Oct 09:25 |
| orb_breakout | NSE:INFY | 15 | 1,114.17 | 1,095.80 | 1,150.25 | 15 Oct 10:00 |
| vwap_pullback | NSE:TCS | 6 | 2,353.27 | 2,344.24 | 2,387.01 | 15 Oct 09:45 |
| vwap_pullback | NSE:SBIN | 17 | 956.79 | 953.43 | 963.70 | 15 Oct 11:45 |
| vwap_pullback | NSE:AXISBANK | 12 | 1,290.66 | 1,284.89 | 1,300.51 | 15 Oct 13:00 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| bb_squeeze | NSE:RELIANCE | 13 | 1,199.74 | 1,190.27 | 1,214.96 | 15 Oct 10:30 |
| bb_squeeze | NSE:SBIN | 17 | 955.69 | 950.71 | 965.98 | 15 Oct 10:45 |
| rsi2_scalper | NSE:TCS | 6 | 2,357.47 | 2,338.14 | – | 15 Oct 13:45 |
| macd_adx | NSE:ITC | 61 | 265.40 | 263.99 | 268.22 | 15 Oct 13:15 |
| vwap_reversion | NSE:BHARTIARTL | -8 | 1,861.13 | 1,876.70 | – | 15 Oct 10:15 |
| vwap_reversion | NSE:RELIANCE | -13 | 1,205.96 | 1,215.41 | – | 15 Oct 11:30 |
| vwap_reversion | NSE:HDFCBANK | -22 | 726.95 | 730.44 | – | 15 Oct 13:45 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 15 Oct 14:00 | bb_squeeze | SELL | 6 | NSE:TCS | 2,356.53 | +12 | back to mid band |
| 15 Oct 13:45 | vwap_reversion | SELL | 22 | NSE:HDFCBANK | 726.95 |  | 2.1 sigma above VWAP |
| 15 Oct 13:45 | vwap_reversion | BUY | 11 | NSE:ICICIBANK | 1,383.38 | -81 | stop-loss |
| 15 Oct 13:45 | tv_rating_scalper | BUY | 23 | NSE:HDFCBANK | 727.25 |  | TV 15m +0.56 / 1h +0.49 |
| 15 Oct 13:45 | rsi2_scalper | BUY | 6 | NSE:TCS | 2,357.47 |  | RSI2 6 in uptrend |
| 15 Oct 13:20 | tv_rating_scalper | SELL | 12 | NSE:ICICIBANK | 1,381.02 | +249 | target |
| 15 Oct 13:15 | macd_adx | BUY | 61 | NSE:ITC | 265.40 |  | MACD up, ADX 33 |
| 15 Oct 13:00 | vwap_pullback | BUY | 12 | NSE:AXISBANK | 1,290.66 |  | pullback held VWAP in uptrend |
| 15 Oct 13:00 | rsi2_scalper | SELL | 9 | NSE:SUNPHARMA | 1,767.65 | +69 | RSI2 snapped back (77) |
| 15 Oct 13:00 | rsi2_scalper | SELL | 37 | NSE:KOTAKBANK | 444.71 | +89 | RSI2 snapped back (82) |
| 15 Oct 12:55 | orb_breakout | BUY | 17 | NSE:SBIN | 959.74 | -202 | stop-loss |
| 15 Oct 12:50 | vwap_pullback | SELL | 13 | NSE:RELIANCE | 1,210.16 | +128 | target |
| 15 Oct 12:45 | vwap_reversion | SELL | 11 | NSE:ICICIBANK | 1,376.72 |  | 2.0 sigma above VWAP |
| 15 Oct 12:45 | rsi2_scalper | BUY | 9 | NSE:SUNPHARMA | 1,759.05 |  | RSI2 7 in uptrend |
| 15 Oct 12:35 | ema_crossover | SELL | 12 | NSE:ICICIBANK | 1,374.72 | +153 | target |
| 15 Oct 12:30 | macd_adx | SELL | 6 | NSE:TCS | 2,362.53 | +48 | MACD reversed |
| 15 Oct 12:25 | macd_adx | SELL | 12 | NSE:ICICIBANK | 1,372.63 | +148 | target |
| 15 Oct 12:15 | rsi2_scalper | BUY | 37 | NSE:KOTAKBANK | 442.09 |  | RSI2 8 in uptrend |
| 15 Oct 12:05 | ema_crossover | SELL | 23 | NSE:HDFCBANK | 724.21 | +152 | target |
| 15 Oct 11:45 | vwap_pullback | BUY | 17 | NSE:SBIN | 956.79 |  | pullback held VWAP in uptrend |
| 15 Oct 11:45 | macd_adx | SELL | 14 | NSE:INFY | 1,112.83 | +44 | MACD reversed |
| 15 Oct 11:30 | vwap_reversion | BUY | 6 | NSE:TCS | 2,365.17 | +78 | back to VWAP |
| 15 Oct 11:30 | vwap_reversion | SELL | 13 | NSE:RELIANCE | 1,205.96 |  | 2.5 sigma above VWAP |
| 15 Oct 11:30 | hourly_macd_swing | BUY | 12 | NSE:ICICIBANK | 1,364.17 |  | 1h MACD bull cross above EMA200 |
| 15 Oct 11:20 | vwap_pullback | SELL | 22 | NSE:HDFCBANK | 721.66 | +94 | target |
| 15 Oct 11:15 | vwap_reversion | BUY | 14 | NSE:INFY | 1,111.92 | +163 | back to VWAP |
| 15 Oct 11:00 | tv_rating_scalper | BUY | 37 | NSE:KOTAKBANK | 443.84 |  | TV 15m +0.60 / 1h +0.47 |
| 15 Oct 10:55 | tv_rating_scalper | SELL | 9 | NSE:BHARTIARTL | 1,846.03 | -151 | stop-loss |
| 15 Oct 10:45 | rsi2_scalper | BUY | 9 | NSE:SUNPHARMA | 1,758.75 | -133 | time stop (1h) |
| 15 Oct 10:45 | rsi2_scalper | BUY | 37 | NSE:KOTAKBANK | 441.49 | -54 | time stop (1h) |
