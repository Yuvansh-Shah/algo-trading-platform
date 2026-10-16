# 🏆 Bot Leaderboard

_Updated 16 Oct 2026 09:45 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **momentum_rotation** | positional 1D | +3.65% | +1,823 | +79 | +1.73% | 0 | – | – | -1.3% | 3 | ✅ |
| 🥈 | **tv_rating_swing** | swing 1D | +2.60% | +1,301 | -177 | +0.68% | 0 | – | – | -0.4% | 3 | ✅ |
| 🥉 | **hourly_macd_swing** | swing 1h | +2.58% | +1,291 | -249 | +0.66% | 2 | 50 | 6.74 | -0.9% | 3 | ✅ |
| 4 | **supertrend_intraday** | intraday 15m | +1.93% | +965 | -33 | +0.01% | 9 | 67 | 5.19 | -0.5% | 3 | ✅ |
| 5 | **nifty_buy_hold** | benchmark 1D | +1.92% | +960 | +31 | +0.00% | 0 | – | – | -0.8% | 1 | ✅ |
| 6 | **tv_rating_scalper** | intraday 15m | +1.77% | +885 | -99 | -0.15% | 21 | 57 | 2.07 | -0.9% | 3 | ✅ |
| 7 | **gap_and_go** | intraday 15m | +1.75% | +873 | +0 | -0.17% | 6 | 83 | 6.87 | -0.8% | 0 | ✅ |
| 8 | **ema_crossover** | intraday 15m | +1.68% | +838 | -22 | -0.24% | 15 | 60 | 3.53 | -0.4% | 2 | ✅ |
| 9 | **donchian_turtle** | swing 1D | +1.00% | +500 | -39 | -0.92% | 0 | – | – | -0.5% | 3 | ✅ |
| 10 | **orb_breakout** | intraday 15m | +0.77% | +387 | +0 | -1.15% | 9 | 67 | 2.02 | -0.8% | 0 | ✅ |
| 11 | **vwap_pullback** | intraday 15m | +0.15% | +75 | -33 | -1.77% | 26 | 46 | 1.29 | -1.7% | 3 | ✅ |
| 12 | **bb_squeeze** | intraday 15m | +0.07% | +34 | -66 | -1.85% | 13 | 46 | 1.09 | -0.6% | 3 | ✅ |
| 13 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -1.92% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -1.92% | 0 | – | – | 0.0% | 0 | ✅ |
| 15 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -1.92% | 0 | – | – | 0.0% | 0 | ✅ |
| 16 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -1.92% | 0 | – | – | 0.0% | 0 | ✅ |
| 17 | **rsi2_scalper** | scalp 15m | -0.57% | -283 | -22 | -2.49% | 24 | 54 | 0.89 | -0.6% | 2 | ✅ |
| 18 | **vwap_reversion** | intraday 15m | -0.62% | -310 | +0 | -2.54% | 22 | 55 | 0.85 | -1.3% | 0 | ✅ |
| 19 | **macd_adx** | intraday 15m | -0.81% | -405 | -21 | -2.73% | 14 | 36 | 0.65 | -1.4% | 2 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -7.07% | -3,534 | +6 | -8.99% | 11 | 18 | 0.06 | -7.4% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
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
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,601.65 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:AXISBANK | 13 | 1,286.66 | 1,199.98 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,297.35 | – | 15 Oct 15:05 |
| hourly_macd_swing | NSE:AXISBANK | 13 | 1,267.25 | 1,254.59 | 1,315.81 | 15 Oct 09:25 |
| hourly_macd_swing | NSE:HDFCBANK | 23 | 720.34 | 710.61 | 738.03 | 15 Oct 10:30 |
| hourly_macd_swing | NSE:ICICIBANK | 12 | 1,364.17 | 1,347.36 | 1,397.28 | 15 Oct 11:30 |
| supertrend_intraday | NSE:RELIANCE | -14 | 1,198.66 | 1,219.64 | 1,157.72 | 16 Oct 09:45 |
| supertrend_intraday | NSE:SBIN | -17 | 952.31 | 964.32 | 928.86 | 16 Oct 09:45 |
| supertrend_intraday | NSE:LT | -4 | 3,613.78 | 3,673.58 | 3,492.75 | 16 Oct 09:45 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| tv_rating_scalper | NSE:LT | -4 | 3,644.27 | 3,674.16 | 3,586.68 | 16 Oct 09:25 |
| tv_rating_scalper | NSE:ICICIBANK | 12 | 1,393.78 | 1,382.35 | 1,415.80 | 16 Oct 09:30 |
| tv_rating_scalper | NSE:KOTAKBANK | 37 | 446.69 | 443.03 | 453.75 | 16 Oct 09:30 |
| ema_crossover | NSE:LT | -4 | 3,613.78 | 3,633.80 | 3,572.30 | 16 Oct 09:45 |
| ema_crossover | NSE:ITC | -63 | 262.75 | 264.35 | 259.69 | 16 Oct 09:45 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| donchian_turtle | NSE:ICICIBANK | 11 | 1,384.88 | 1,334.46 | – | 15 Oct 15:10 |
| donchian_turtle | NSE:INFY | 14 | 1,109.87 | 1,049.88 | – | 15 Oct 15:10 |
| vwap_pullback | NSE:HDFCBANK | 22 | 729.35 | 726.96 | 734.58 | 16 Oct 09:45 |
| vwap_pullback | NSE:INFY | 14 | 1,143.23 | 1,135.45 | 1,155.40 | 16 Oct 09:45 |
| vwap_pullback | NSE:TCS | 6 | 2,413.98 | 2,402.46 | 2,441.29 | 16 Oct 09:45 |
| bb_squeeze | NSE:LT | -4 | 3,644.27 | 3,658.70 | 3,606.80 | 16 Oct 09:25 |
| bb_squeeze | NSE:HDFCBANK | 22 | 729.35 | 725.69 | 737.13 | 16 Oct 09:45 |
| bb_squeeze | NSE:INFY | 14 | 1,143.23 | 1,132.12 | 1,162.05 | 16 Oct 09:45 |
| rsi2_scalper | NSE:RELIANCE | 13 | 1,198.74 | 1,188.91 | – | 16 Oct 09:45 |
| rsi2_scalper | NSE:AXISBANK | 12 | 1,280.26 | 1,269.76 | – | 16 Oct 09:45 |
| macd_adx | NSE:INFY | 14 | 1,143.23 | 1,132.12 | 1,162.05 | 16 Oct 09:45 |
| macd_adx | NSE:TCS | 6 | 2,413.98 | 2,395.98 | 2,454.23 | 16 Oct 09:45 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.255042 | 82,042.44 | – | – | 16 Oct 09:00 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.57134 | 2,440.43 | – | – | 16 Oct 09:00 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 16 Oct 09:45 | vwap_pullback | BUY | 6 | NSE:TCS | 2,413.98 |  | pullback held VWAP in uptrend |
| 16 Oct 09:45 | vwap_pullback | BUY | 14 | NSE:INFY | 1,143.23 |  | pullback held VWAP in uptrend |
| 16 Oct 09:45 | vwap_pullback | BUY | 22 | NSE:HDFCBANK | 729.35 |  | pullback held VWAP in uptrend |
| 16 Oct 09:45 | supertrend_intraday | SELL | 4 | NSE:LT | 3,613.78 |  | Supertrend flipped down |
| 16 Oct 09:45 | supertrend_intraday | SELL | 17 | NSE:SBIN | 952.31 |  | Supertrend flipped down |
| 16 Oct 09:45 | supertrend_intraday | SELL | 14 | NSE:RELIANCE | 1,198.66 |  | Supertrend flipped down |
| 16 Oct 09:45 | rsi2_scalper | BUY | 12 | NSE:AXISBANK | 1,280.26 |  | RSI2 1 in uptrend |
| 16 Oct 09:45 | rsi2_scalper | BUY | 13 | NSE:RELIANCE | 1,198.74 |  | RSI2 1 in uptrend |
| 16 Oct 09:45 | macd_adx | BUY | 6 | NSE:TCS | 2,413.98 |  | MACD up, ADX 45 |
| 16 Oct 09:45 | macd_adx | BUY | 14 | NSE:INFY | 1,143.23 |  | MACD up, ADX 40 |
| 16 Oct 09:45 | ema_crossover | SELL | 63 | NSE:ITC | 262.75 |  | EMA9<21, RSI 41 |
| 16 Oct 09:45 | ema_crossover | SELL | 4 | NSE:LT | 3,613.78 |  | EMA9<21, RSI 30 |
| 16 Oct 09:45 | bb_squeeze | BUY | 14 | NSE:INFY | 1,143.23 |  | squeeze breakout up |
| 16 Oct 09:45 | bb_squeeze | BUY | 22 | NSE:HDFCBANK | 729.35 |  | squeeze breakout up |
| 16 Oct 09:35 | bb_squeeze | BUY | 14 | NSE:INFY | 1,137.18 | -150 | stop-loss |
| 16 Oct 09:30 | tv_rating_scalper | BUY | 37 | NSE:KOTAKBANK | 446.69 |  | TV 15m +0.60 / 1h +0.49 |
| 16 Oct 09:30 | tv_rating_scalper | BUY | 12 | NSE:ICICIBANK | 1,393.78 |  | TV 15m +0.65 / 1h +0.45 |
| 16 Oct 09:30 | bb_squeeze | SELL | 14 | NSE:INFY | 1,127.02 |  | squeeze breakout down |
| 16 Oct 09:30 | bb_squeeze | BUY | 14 | NSE:INFY | 1,127.48 | -11 | stop-loss |
| 16 Oct 09:25 | tv_rating_scalper | SELL | 4 | NSE:LT | 3,644.27 |  | TV 15m -0.51 / 1h -0.47 |
| 16 Oct 09:25 | bb_squeeze | SELL | 4 | NSE:LT | 3,644.27 |  | squeeze breakout down |
| 16 Oct 09:25 | bb_squeeze | SELL | 14 | NSE:INFY | 1,127.27 |  | squeeze breakout down |
| 16 Oct 09:00 | crypto_supertrend | BUY | 8.57134 | BINANCE:ETHUSDT | 2,440.43 |  | Supertrend up |
| 16 Oct 09:00 | crypto_supertrend | BUY | 0.255042 | BINANCE:BTCUSDT | 82,042.44 |  | Supertrend up |
| 15 Oct 15:15 | vwap_reversion | BUY | 13 | NSE:RELIANCE | 1,206.34 | +141 | intraday square-off |
| 15 Oct 15:15 | vwap_reversion | BUY | 22 | NSE:HDFCBANK | 725.55 | +23 | intraday square-off |
| 15 Oct 15:15 | vwap_pullback | SELL | 12 | NSE:AXISBANK | 1,286.54 | -57 | intraday square-off |
| 15 Oct 15:15 | vwap_pullback | SELL | 17 | NSE:SBIN | 959.66 | +41 | intraday square-off |
| 15 Oct 15:15 | vwap_pullback | SELL | 6 | NSE:TCS | 2,359.13 | +28 | intraday square-off |
| 15 Oct 15:15 | tv_rating_scalper | SELL | 23 | NSE:HDFCBANK | 725.25 | -54 | intraday square-off |
