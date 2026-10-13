# 🏆 Bot Leaderboard

_Updated 13 Oct 2026 14:20 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **tv_rating_scalper** | intraday 15m | +1.13% | +567 | +577 | +0.76% | 5 | 60 | 3.66 | -0.5% | 2 | ✅ |
| 🥈 | **ema_crossover** | intraday 15m | +0.58% | +291 | +291 | +0.21% | 2 | 50 | 1.95 | -0.4% | 3 | ✅ |
| 🥉 | **gap_and_go** | intraday 15m | +0.53% | +267 | +267 | +0.16% | 0 | – | – | -0.5% | 2 | ✅ |
| 4 | **nifty_buy_hold** | benchmark 1D | +0.37% | +186 | +186 | +0.00% | 0 | – | – | -0.3% | 1 | ✅ |
| 5 | **supertrend_intraday** | intraday 15m | +0.32% | +159 | +159 | -0.05% | 0 | – | – | -0.4% | 3 | ✅ |
| 6 | **orb_breakout** | intraday 15m | +0.25% | +125 | +125 | -0.12% | 0 | – | – | -0.6% | 3 | ✅ |
| 7 | **vwap_pullback** | intraday 15m | +0.14% | +69 | +69 | -0.24% | 5 | 40 | 1.63 | -0.4% | 3 | ✅ |
| 8 | **bb_squeeze** | intraday 15m | +0.06% | +28 | +28 | -0.32% | 1 | 0 | 0.00 | -0.4% | 2 | ✅ |
| 9 | **hourly_macd_swing** | swing 1h | +0.04% | +19 | +19 | -0.33% | 0 | – | – | -0.2% | 1 | ✅ |
| 10 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -0.37% | 0 | – | – | 0.0% | 0 | ✅ |
| 11 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -0.37% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **donchian_turtle** | swing 1D | +0.00% | +0 | +0 | -0.37% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -0.37% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -0.37% | 0 | – | – | 0.0% | 0 | ✅ |
| 15 | **momentum_rotation** | positional 1D | +0.00% | +0 | +0 | -0.37% | 0 | – | – | 0.0% | 0 | ✅ |
| 16 | **tv_rating_swing** | swing 1D | +0.00% | +0 | +0 | -0.37% | 0 | – | – | 0.0% | 0 | ✅ |
| 17 | **vwap_reversion** | intraday 15m | -0.19% | -93 | -93 | -0.56% | 4 | 75 | 1.19 | -0.4% | 3 | ✅ |
| 18 | **rsi2_scalper** | scalp 15m | -0.21% | -105 | -105 | -0.58% | 4 | 50 | 0.22 | -0.4% | 2 | ✅ |
| 19 | **macd_adx** | intraday 15m | -0.24% | -121 | -121 | -0.62% | 4 | 25 | 0.63 | -0.5% | 0 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -2.77% | -1,383 | +219 | -3.14% | 9 | 22 | 0.12 | -3.6% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| tv_rating_scalper | NSE:HDFCBANK | 23 | 711.79 | 705.96 | 723.04 | 13 Oct 10:45 |
| tv_rating_scalper | NSE:ICICIBANK | 12 | 1,349.77 | 1,338.70 | 1,371.09 | 13 Oct 13:00 |
| ema_crossover | NSE:TCS | 7 | 2,219.94 | 2,195.32 | 2,264.56 | 13 Oct 09:45 |
| ema_crossover | NSE:KOTAKBANK | -37 | 440.41 | 442.38 | 436.60 | 13 Oct 12:15 |
| ema_crossover | NSE:SUNPHARMA | 9 | 1,762.25 | 1,756.57 | 1,777.37 | 13 Oct 14:00 |
| gap_and_go | NSE:INFY | 15 | 1,041.91 | 1,027.00 | 1,070.05 | 13 Oct 10:00 |
| gap_and_go | NSE:TCS | 7 | 2,225.04 | 2,155.00 | 2,373.10 | 13 Oct 10:00 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| supertrend_intraday | NSE:HDFCBANK | 23 | 714.89 | 701.76 | 740.73 | 13 Oct 09:45 |
| supertrend_intraday | NSE:ICICIBANK | 12 | 1,345.87 | 1,331.26 | 1,374.28 | 13 Oct 09:45 |
| supertrend_intraday | NSE:INFY | 15 | 1,039.61 | 1,017.12 | 1,081.41 | 13 Oct 09:45 |
| orb_breakout | NSE:RELIANCE | 14 | 1,164.63 | 1,152.20 | 1,188.50 | 13 Oct 10:00 |
| orb_breakout | NSE:ICICIBANK | 12 | 1,347.97 | 1,329.40 | 1,381.60 | 13 Oct 10:00 |
| orb_breakout | NSE:INFY | 15 | 1,041.91 | 1,027.00 | 1,070.05 | 13 Oct 10:00 |
| vwap_pullback | NSE:RELIANCE | -14 | 1,159.87 | 1,163.62 | 1,152.77 | 13 Oct 10:45 |
| vwap_pullback | NSE:SUNPHARMA | -9 | 1,757.15 | 1,762.35 | 1,746.31 | 13 Oct 12:30 |
| vwap_pullback | NSE:ITC | -63 | 259.25 | 260.01 | 257.87 | 13 Oct 14:15 |
| bb_squeeze | NSE:ICICIBANK | 12 | 1,345.87 | 1,339.30 | 1,358.21 | 13 Oct 09:45 |
| bb_squeeze | NSE:KOTAKBANK | -37 | 440.41 | 442.38 | 436.60 | 13 Oct 12:15 |
| hourly_macd_swing | NSE:TCS | 7 | 2,242.15 | 2,182.70 | 2,362.39 | 13 Oct 10:30 |
| vwap_reversion | NSE:AXISBANK | -13 | 1,256.85 | 1,263.48 | – | 13 Oct 13:15 |
| vwap_reversion | NSE:KOTAKBANK | 37 | 438.09 | 436.14 | – | 13 Oct 13:45 |
| vwap_reversion | NSE:ICICIBANK | -12 | 1,353.93 | 1,358.90 | – | 13 Oct 14:00 |
| rsi2_scalper | NSE:SBIN | -17 | 943.91 | 951.65 | – | 13 Oct 13:30 |
| rsi2_scalper | NSE:TCS | 7 | 2,243.85 | 2,225.45 | – | 13 Oct 14:00 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.261364 | 83,345.55 | – | – | 13 Oct 09:30 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.68092 | 2,508.57 | – | – | 13 Oct 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
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
| 13 Oct 12:30 | macd_adx | SELL | 17 | NSE:SBIN | 942.11 |  | MACD down, ADX 23 |
| 13 Oct 12:25 | vwap_pullback | SELL | 7 | NSE:TCS | 2,249.25 | +197 | target |
| 13 Oct 12:15 | vwap_reversion | BUY | 37 | NSE:KOTAKBANK | 440.59 |  | -2.2 sigma below VWAP |
| 13 Oct 12:15 | ema_crossover | SELL | 37 | NSE:KOTAKBANK | 440.41 |  | EMA9<21, RSI 41 |
| 13 Oct 12:15 | bb_squeeze | SELL | 37 | NSE:KOTAKBANK | 440.41 |  | squeeze breakout down |
| 13 Oct 12:05 | macd_adx | SELL | 23 | NSE:HDFCBANK | 710.06 | -119 | stop-loss |
| 13 Oct 12:05 | ema_crossover | SELL | 23 | NSE:HDFCBANK | 710.06 | -119 | stop-loss |
| 13 Oct 12:00 | vwap_reversion | SELL | 9 | NSE:BHARTIARTL | 1,778.24 | +57 | back to VWAP |
| 13 Oct 12:00 | tv_rating_scalper | SELL | 14 | NSE:RELIANCE | 1,152.87 |  | TV 15m -0.54 / 1h -0.56 |
