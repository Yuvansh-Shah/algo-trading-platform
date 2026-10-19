# 🏆 Bot Leaderboard

_Updated 19 Oct 2026 14:20 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **momentum_rotation** | positional 1D | +4.13% | +2,065 | -174 | +2.26% | 0 | – | – | -1.6% | 3 | ✅ |
| 🥈 | **tv_rating_swing** | swing 1D | +2.32% | +1,161 | -591 | +0.45% | 0 | – | – | -2.2% | 3 | ✅ |
| 🥉 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | -490 | +0.36% | 5 | 60 | 4.63 | -0.9% | 0 | ✅ |
| 4 | **nifty_buy_hold** | benchmark 1D | +1.87% | +935 | -453 | +0.00% | 0 | – | – | -1.1% | 1 | ✅ |
| 5 | **gap_and_go** | intraday 15m | +1.39% | +695 | -397 | -0.48% | 8 | 88 | 8.50 | -1.2% | 2 | ✅ |
| 6 | **vwap_pullback** | intraday 15m | +1.03% | +514 | +55 | -0.84% | 38 | 47 | 1.40 | -1.7% | 3 | ✅ |
| 7 | **supertrend_intraday** | intraday 15m | +0.93% | +466 | +111 | -0.94% | 13 | 46 | 1.53 | -1.9% | 3 | ✅ |
| 8 | **tv_rating_scalper** | intraday 15m | +0.71% | +358 | -178 | -1.16% | 32 | 44 | 1.25 | -2.0% | 3 | ✅ |
| 9 | **orb_breakout** | intraday 15m | +0.63% | +314 | +31 | -1.24% | 12 | 58 | 1.64 | -1.5% | 3 | ✅ |
| 10 | **ema_crossover** | intraday 15m | +0.51% | +255 | -106 | -1.36% | 24 | 42 | 1.22 | -1.7% | 3 | ✅ |
| 11 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -1.87% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -1.87% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -1.87% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -1.87% | 0 | – | – | 0.0% | 0 | ✅ |
| 15 | **vwap_reversion** | intraday 15m | -0.39% | -196 | +122 | -2.26% | 32 | 59 | 1.20 | -1.3% | 3 | ✅ |
| 16 | **donchian_turtle** | swing 1D | -0.48% | -240 | -1,001 | -2.35% | 0 | – | – | -2.5% | 3 | ✅ |
| 17 | **bb_squeeze** | intraday 15m | -0.98% | -492 | -413 | -2.85% | 20 | 40 | 0.68 | -1.4% | 0 | ✅ |
| 18 | **macd_adx** | intraday 15m | -1.02% | -512 | -178 | -2.89% | 22 | 32 | 0.71 | -1.4% | 0 | ✅ |
| 19 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | -554 | -3.40% | 35 | 49 | 0.61 | -1.5% | 0 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -6.76% | -3,378 | +141 | -8.63% | 11 | 18 | 0.06 | -7.4% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
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
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,669.26 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:AXISBANK | 13 | 1,286.66 | 1,201.10 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,309.16 | – | 15 Oct 15:05 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| gap_and_go | NSE:INFY | 14 | 1,157.18 | 1,122.00 | 1,245.90 | 19 Oct 09:25 |
| gap_and_go | NSE:TCS | 6 | 2,458.49 | 2,375.70 | 2,650.80 | 19 Oct 09:25 |
| vwap_pullback | NSE:ITC | -63 | 262.05 | 263.07 | 260.17 | 19 Oct 10:15 |
| vwap_pullback | NSE:SUNPHARMA | -9 | 1,751.05 | 1,758.16 | 1,734.58 | 19 Oct 10:15 |
| vwap_pullback | NSE:AXISBANK | -13 | 1,237.15 | 1,244.39 | 1,223.43 | 19 Oct 12:45 |
| supertrend_intraday | NSE:HDFCBANK | -23 | 713.21 | 731.15 | 680.60 | 19 Oct 09:45 |
| supertrend_intraday | NSE:INFY | -14 | 1,137.27 | 1,164.40 | 1,091.05 | 19 Oct 09:45 |
| supertrend_intraday | NSE:SBIN | 17 | 972.54 | 957.80 | 1,004.29 | 19 Oct 09:45 |
| tv_rating_scalper | NSE:TCS | 6 | 2,458.49 | 2,438.34 | 2,497.33 | 19 Oct 09:25 |
| tv_rating_scalper | NSE:AXISBANK | -13 | 1,245.65 | 1,255.87 | 1,225.97 | 19 Oct 09:30 |
| tv_rating_scalper | NSE:HDFCBANK | -23 | 710.46 | 716.28 | 699.23 | 19 Oct 12:31 |
| orb_breakout | NSE:SBIN | 16 | 983.20 | 960.70 | 1,024.60 | 19 Oct 10:00 |
| orb_breakout | NSE:ICICIBANK | -11 | 1,388.62 | 1,411.80 | 1,341.90 | 19 Oct 10:15 |
| orb_breakout | NSE:BHARTIARTL | -8 | 1,896.92 | 1,929.60 | 1,832.10 | 19 Oct 10:15 |
| ema_crossover | NSE:ICICIBANK | -11 | 1,384.52 | 1,395.16 | 1,364.97 | 19 Oct 11:00 |
| ema_crossover | NSE:INFY | -14 | 1,143.32 | 1,153.23 | 1,124.03 | 19 Oct 11:15 |
| ema_crossover | NSE:TCS | -6 | 2,452.31 | 2,466.93 | 2,422.45 | 19 Oct 14:00 |
| vwap_reversion | NSE:HDFCBANK | 23 | 713.19 | 708.18 | – | 19 Oct 11:15 |
| vwap_reversion | NSE:SBIN | 17 | 969.69 | 963.51 | – | 19 Oct 12:00 |
| vwap_reversion | NSE:SUNPHARMA | 9 | 1,747.75 | 1,737.55 | – | 19 Oct 12:00 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| donchian_turtle | NSE:ICICIBANK | 11 | 1,384.88 | 1,334.46 | – | 15 Oct 15:10 |
| donchian_turtle | NSE:INFY | 14 | 1,109.87 | 1,049.88 | – | 15 Oct 15:10 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.255042 | 82,042.44 | – | – | 16 Oct 09:00 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.57134 | 2,440.43 | – | – | 16 Oct 09:00 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 19 Oct 14:00 | ema_crossover | SELL | 6 | NSE:TCS | 2,452.31 |  | EMA9<21, RSI 47 |
| 19 Oct 13:45 | rsi2_scalper | SELL | 6 | NSE:TCS | 2,451.51 | -15 | time stop (1h) |
| 19 Oct 13:45 | rsi2_scalper | SELL | 13 | NSE:RELIANCE | 1,204.56 | -96 | time stop (1h) |
| 19 Oct 13:45 | ema_crossover | SELL | 4 | NSE:LT | 3,652.57 | -60 | opposite EMA cross |
| 19 Oct 12:45 | vwap_pullback | SELL | 13 | NSE:AXISBANK | 1,237.15 |  | rally rejected at VWAP in downtrend |
| 19 Oct 12:45 | rsi2_scalper | BUY | 6 | NSE:TCS | 2,452.79 |  | RSI2 0 in uptrend |
| 19 Oct 12:45 | rsi2_scalper | SELL | 14 | NSE:INFY | 1,131.87 | -125 | time stop (1h) |
| 19 Oct 12:45 | rsi2_scalper | BUY | 13 | NSE:RELIANCE | 1,211.34 |  | RSI2 2 in uptrend |
| 19 Oct 12:45 | rsi2_scalper | SELL | 6 | NSE:TCS | 2,451.81 | -134 | stop-loss |
| 19 Oct 12:45 | rsi2_scalper | SELL | 8 | NSE:BHARTIARTL | 1,877.62 | -146 | stop-loss |
| 19 Oct 12:31 | tv_rating_scalper | SELL | 23 | NSE:HDFCBANK | 710.46 |  | TV 15m -0.51 / 1h -0.45 |
| 19 Oct 12:30 | tv_rating_scalper | SELL | 13 | NSE:RELIANCE | 1,210.76 | -191 | stop-loss |
| 19 Oct 12:20 | vwap_pullback | SELL | 13 | NSE:RELIANCE | 1,214.76 | -139 | stop-loss |
| 19 Oct 12:10 | bb_squeeze | SELL | 16 | NSE:SBIN | 967.46 | -89 | stop-loss |
| 19 Oct 12:00 | vwap_reversion | BUY | 9 | NSE:SUNPHARMA | 1,747.75 |  | -2.1 sigma below VWAP |
| 19 Oct 12:00 | vwap_reversion | BUY | 17 | NSE:SBIN | 969.69 |  | -2.0 sigma below VWAP |
| 19 Oct 12:00 | vwap_reversion | BUY | 13 | NSE:RELIANCE | 1,219.24 | +59 | back to VWAP |
| 19 Oct 12:00 | rsi2_scalper | BUY | 6 | NSE:TCS | 2,472.89 |  | RSI2 7 in uptrend |
| 19 Oct 12:00 | macd_adx | SELL | 16 | NSE:SBIN | 969.31 | -60 | MACD reversed |
| 19 Oct 11:45 | rsi2_scalper | BUY | 8 | NSE:BHARTIARTL | 1,894.98 |  | RSI2 5 in uptrend |
| 19 Oct 11:45 | rsi2_scalper | BUY | 14 | NSE:INFY | 1,140.23 |  | RSI2 4 in uptrend |
| 19 Oct 11:30 | vwap_reversion | BUY | 6 | NSE:TCS | 2,474.99 | +110 | back to VWAP |
| 19 Oct 11:15 | vwap_reversion | BUY | 23 | NSE:HDFCBANK | 713.19 |  | -2.1 sigma below VWAP |
| 19 Oct 11:15 | ema_crossover | SELL | 14 | NSE:INFY | 1,143.32 |  | EMA9<21, RSI 48 |
| 19 Oct 11:00 | vwap_reversion | BUY | 16 | NSE:SBIN | 973.59 | +140 | back to VWAP |
| 19 Oct 11:00 | ema_crossover | SELL | 11 | NSE:ICICIBANK | 1,384.52 |  | EMA9<21, RSI 43 |
| 19 Oct 10:45 | macd_adx | SELL | 6 | NSE:TCS | 2,479.50 | -103 | MACD reversed |
| 19 Oct 10:30 | hourly_macd_swing | SELL | 23 | NSE:HDFCBANK | 712.46 | -190 | 1h MACD bear cross |
| 19 Oct 10:30 | ema_crossover | BUY | 4 | NSE:LT | 3,665.73 |  | EMA9>21, RSI 57 |
| 19 Oct 10:30 | bb_squeeze | BUY | 13 | NSE:AXISBANK | 1,242.55 | -219 | stop-loss |
