# 🏆 Bot Leaderboard

_Updated 13 Oct 2026 14:55 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **tv_rating_scalper** | intraday 15m | +1.39% | +695 | +705 | +0.64% | 5 | 60 | 3.66 | -0.5% | 2 | ✅ |
| 🥈 | **gap_and_go** | intraday 15m | +0.86% | +428 | +428 | +0.11% | 0 | – | – | -0.5% | 2 | ✅ |
| 🥉 | **supertrend_intraday** | intraday 15m | +0.81% | +403 | +403 | +0.06% | 0 | – | – | -0.4% | 3 | ✅ |
| 4 | **nifty_buy_hold** | benchmark 1D | +0.75% | +373 | +373 | +0.00% | 0 | – | – | -0.3% | 1 | ✅ |
| 5 | **orb_breakout** | intraday 15m | +0.71% | +357 | +357 | -0.03% | 0 | – | – | -0.6% | 3 | ✅ |
| 6 | **ema_crossover** | intraday 15m | +0.62% | +308 | +308 | -0.13% | 3 | 33 | 1.55 | -0.4% | 2 | ✅ |
| 7 | **hourly_macd_swing** | swing 1h | +0.24% | +121 | +121 | -0.50% | 0 | – | – | -0.2% | 2 | ✅ |
| 8 | **bb_squeeze** | intraday 15m | +0.10% | +49 | +49 | -0.65% | 2 | 50 | 1.31 | -0.4% | 1 | ✅ |
| 9 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -0.75% | 0 | – | – | 0.0% | 0 | ✅ |
| 10 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -0.75% | 0 | – | – | 0.0% | 0 | ✅ |
| 11 | **donchian_turtle** | swing 1D | +0.00% | +0 | +0 | -0.75% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -0.75% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -0.75% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **momentum_rotation** | positional 1D | +0.00% | +0 | +0 | -0.75% | 0 | – | – | 0.0% | 0 | ✅ |
| 15 | **tv_rating_swing** | swing 1D | +0.00% | +0 | +0 | -0.75% | 0 | – | – | 0.0% | 0 | ✅ |
| 16 | **vwap_pullback** | intraday 15m | -0.09% | -47 | -47 | -0.84% | 6 | 33 | 1.29 | -0.5% | 2 | ✅ |
| 17 | **rsi2_scalper** | scalp 15m | -0.23% | -116 | -116 | -0.98% | 6 | 50 | 0.68 | -0.4% | 1 | ✅ |
| 18 | **macd_adx** | intraday 15m | -0.24% | -121 | -121 | -0.99% | 4 | 25 | 0.63 | -0.5% | 0 | ✅ |
| 19 | **vwap_reversion** | intraday 15m | -0.35% | -176 | -176 | -1.10% | 6 | 50 | 0.44 | -0.6% | 1 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -3.09% | -1,547 | +55 | -3.84% | 9 | 22 | 0.12 | -3.6% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| tv_rating_scalper | NSE:HDFCBANK | 23 | 711.79 | 705.96 | 723.04 | 13 Oct 10:45 |
| tv_rating_scalper | NSE:ICICIBANK | 12 | 1,349.77 | 1,338.70 | 1,371.09 | 13 Oct 13:00 |
| gap_and_go | NSE:INFY | 15 | 1,041.91 | 1,027.00 | 1,070.05 | 13 Oct 10:00 |
| gap_and_go | NSE:TCS | 7 | 2,225.04 | 2,155.00 | 2,373.10 | 13 Oct 10:00 |
| supertrend_intraday | NSE:HDFCBANK | 23 | 714.89 | 701.76 | 740.73 | 13 Oct 09:45 |
| supertrend_intraday | NSE:ICICIBANK | 12 | 1,345.87 | 1,331.26 | 1,374.28 | 13 Oct 09:45 |
| supertrend_intraday | NSE:INFY | 15 | 1,039.61 | 1,017.12 | 1,081.41 | 13 Oct 09:45 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| orb_breakout | NSE:RELIANCE | 14 | 1,164.63 | 1,152.20 | 1,188.50 | 13 Oct 10:00 |
| orb_breakout | NSE:ICICIBANK | 12 | 1,347.97 | 1,329.40 | 1,381.60 | 13 Oct 10:00 |
| orb_breakout | NSE:INFY | 15 | 1,041.91 | 1,027.00 | 1,070.05 | 13 Oct 10:00 |
| ema_crossover | NSE:TCS | 7 | 2,219.94 | 2,195.32 | 2,264.56 | 13 Oct 09:45 |
| ema_crossover | NSE:KOTAKBANK | -37 | 440.41 | 442.38 | 436.60 | 13 Oct 12:15 |
| hourly_macd_swing | NSE:TCS | 7 | 2,242.15 | 2,182.70 | 2,362.39 | 13 Oct 10:30 |
| hourly_macd_swing | NSE:AXISBANK | 13 | 1,263.65 | 1,245.45 | 1,299.89 | 13 Oct 14:30 |
| bb_squeeze | NSE:KOTAKBANK | -37 | 440.41 | 442.38 | 436.60 | 13 Oct 12:15 |
| vwap_pullback | NSE:RELIANCE | -14 | 1,159.87 | 1,163.62 | 1,152.77 | 13 Oct 10:45 |
| vwap_pullback | NSE:ITC | -63 | 259.25 | 260.01 | 257.87 | 13 Oct 14:15 |
| rsi2_scalper | NSE:RELIANCE | -14 | 1,161.47 | 1,170.99 | – | 13 Oct 14:45 |
| vwap_reversion | NSE:KOTAKBANK | 37 | 438.09 | 436.14 | – | 13 Oct 13:45 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.261364 | 83,345.55 | – | – | 13 Oct 09:30 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.68092 | 2,508.57 | – | – | 13 Oct 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 13 Oct 14:55 | vwap_reversion | BUY | 12 | NSE:ICICIBANK | 1,360.27 | -84 | stop-loss |
| 13 Oct 14:55 | vwap_pullback | BUY | 9 | NSE:SUNPHARMA | 1,763.25 | -63 | stop-loss |
| 13 Oct 14:50 | bb_squeeze | SELL | 12 | NSE:ICICIBANK | 1,358.43 | +143 | target |
| 13 Oct 14:45 | rsi2_scalper | SELL | 14 | NSE:RELIANCE | 1,161.47 |  | RSI2 96 in downtrend |
| 13 Oct 14:45 | ema_crossover | SELL | 9 | NSE:SUNPHARMA | 1,759.65 | -31 | opposite EMA cross |
| 13 Oct 14:35 | vwap_reversion | BUY | 13 | NSE:AXISBANK | 1,264.05 | -102 | stop-loss |
| 13 Oct 14:30 | rsi2_scalper | BUY | 17 | NSE:SBIN | 946.69 | -55 | time stop (1h) |
| 13 Oct 14:30 | rsi2_scalper | SELL | 7 | NSE:TCS | 2,253.25 | +58 | RSI2 snapped back (80) |
| 13 Oct 14:30 | hourly_macd_swing | BUY | 13 | NSE:AXISBANK | 1,263.65 |  | 1h MACD bull cross above EMA200 |
| 13 Oct 14:15 | vwap_pullback | SELL | 63 | NSE:ITC | 259.25 |  | rally rejected at VWAP in downtrend |
| 13 Oct 14:00 | vwap_reversion | SELL | 12 | NSE:ICICIBANK | 1,353.93 |  | 2.4 sigma above VWAP |
| 13 Oct 14:00 | vwap_pullback | BUY | 17 | NSE:SBIN | 945.69 | -60 | stop-loss |
| 13 Oct 14:00 | tv_rating_scalper | BUY | 14 | NSE:RELIANCE | 1,160.03 | -108 | 15m rating faded (+0.07) |
| 13 Oct 14:00 | rsi2_scalper | BUY | 7 | NSE:TCS | 2,243.85 |  | RSI2 5 in uptrend |
| 13 Oct 14:00 | macd_adx | SELL | 7 | NSE:TCS | 2,242.95 | +153 | MACD reversed |
| 13 Oct 14:00 | ema_crossover | BUY | 9 | NSE:SUNPHARMA | 1,762.25 |  | EMA9>21, RSI 55 |
| 13 Oct 13:45 | vwap_reversion | BUY | 37 | NSE:KOTAKBANK | 438.09 |  | -2.0 sigma below VWAP |
| 13 Oct 13:45 | vwap_reversion | SELL | 37 | NSE:KOTAKBANK | 437.91 | -107 | stop-loss |
| 13 Oct 13:45 | rsi2_scalper | BUY | 14 | NSE:RELIANCE | 1,157.33 | -6 | time stop (1h) |
| 13 Oct 13:45 | macd_adx | BUY | 17 | NSE:SBIN | 944.24 | -44 | MACD reversed |
| 13 Oct 13:30 | rsi2_scalper | SELL | 17 | NSE:SBIN | 943.91 |  | RSI2 95 in downtrend |
| 13 Oct 13:15 | vwap_reversion | SELL | 13 | NSE:AXISBANK | 1,256.85 |  | 2.4 sigma above VWAP |
| 13 Oct 13:00 | vwap_pullback | SELL | 17 | NSE:SBIN | 942.61 |  | rally rejected at VWAP in downtrend |
| 13 Oct 13:00 | tv_rating_scalper | BUY | 12 | NSE:ICICIBANK | 1,349.77 |  | TV 15m +0.56 / 1h +0.31 |
| 13 Oct 12:45 | vwap_pullback | SELL | 15 | NSE:INFY | 1,055.69 | +199 | target |
| 13 Oct 12:45 | tv_rating_scalper | SELL | 7 | NSE:TCS | 2,258.75 | +264 | target |
| 13 Oct 12:45 | rsi2_scalper | SELL | 14 | NSE:RELIANCE | 1,157.47 |  | RSI2 91 in downtrend |
| 13 Oct 12:45 | macd_adx | BUY | 14 | NSE:RELIANCE | 1,157.93 | -79 | MACD reversed |
| 13 Oct 12:45 | ema_crossover | SELL | 15 | NSE:INFY | 1,055.69 | +233 | target |
| 13 Oct 12:30 | vwap_pullback | SELL | 9 | NSE:SUNPHARMA | 1,757.15 |  | rally rejected at VWAP in downtrend |
