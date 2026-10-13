# 🏆 Bot Leaderboard

_Updated 13 Oct 2026 12:40 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **tv_rating_scalper** | intraday 15m | +1.12% | +561 | +571 | +0.88% | 3 | 67 | 4.84 | -0.5% | 3 | ✅ |
| 🥈 | **gap_and_go** | intraday 15m | +0.66% | +329 | +329 | +0.42% | 0 | – | – | -0.4% | 2 | ✅ |
| 🥉 | **ema_crossover** | intraday 15m | +0.60% | +299 | +299 | +0.36% | 1 | 0 | 0.00 | -0.4% | 3 | ✅ |
| 4 | **vwap_pullback** | intraday 15m | +0.29% | +143 | +143 | +0.05% | 3 | 33 | 1.08 | -0.4% | 3 | ✅ |
| 5 | **nifty_buy_hold** | benchmark 1D | +0.24% | +119 | +119 | +0.00% | 0 | – | – | -0.3% | 1 | ✅ |
| 6 | **supertrend_intraday** | intraday 15m | +0.23% | +114 | +114 | -0.01% | 0 | – | – | -0.4% | 3 | ✅ |
| 7 | **hourly_macd_swing** | swing 1h | +0.14% | +70 | +70 | -0.10% | 0 | – | – | -0.2% | 1 | ✅ |
| 8 | **vwap_reversion** | intraday 15m | +0.11% | +53 | +53 | -0.13% | 3 | 100 | ∞ | -0.1% | 1 | ✅ |
| 9 | **macd_adx** | intraday 15m | +0.05% | +26 | +26 | -0.19% | 1 | 0 | 0.00 | -0.3% | 3 | ✅ |
| 10 | **orb_breakout** | intraday 15m | +0.03% | +17 | +17 | -0.21% | 0 | – | – | -0.6% | 3 | ✅ |
| 11 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -0.24% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -0.24% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **donchian_turtle** | swing 1D | +0.00% | +0 | +0 | -0.24% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -0.24% | 0 | – | – | 0.0% | 0 | ✅ |
| 15 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -0.24% | 0 | – | – | 0.0% | 0 | ✅ |
| 16 | **momentum_rotation** | positional 1D | +0.00% | +0 | +0 | -0.24% | 0 | – | – | 0.0% | 0 | ✅ |
| 17 | **tv_rating_swing** | swing 1D | +0.00% | +0 | +0 | -0.24% | 0 | – | – | 0.0% | 0 | ✅ |
| 18 | **rsi2_scalper** | scalp 15m | -0.10% | -52 | -52 | -0.34% | 3 | 67 | 0.25 | -0.4% | 0 | ✅ |
| 19 | **bb_squeeze** | intraday 15m | -0.11% | -56 | -56 | -0.35% | 1 | 0 | 0.00 | -0.4% | 2 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -2.68% | -1,338 | +263 | -2.92% | 9 | 22 | 0.12 | -3.6% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| tv_rating_scalper | NSE:TCS | 7 | 2,219.94 | 2,201.74 | 2,255.01 | 13 Oct 09:45 |
| tv_rating_scalper | NSE:HDFCBANK | 23 | 711.79 | 705.96 | 723.04 | 13 Oct 10:45 |
| tv_rating_scalper | NSE:RELIANCE | -14 | 1,152.87 | 1,162.32 | 1,134.65 | 13 Oct 12:00 |
| gap_and_go | NSE:INFY | 15 | 1,041.91 | 1,027.00 | 1,070.05 | 13 Oct 10:00 |
| gap_and_go | NSE:TCS | 7 | 2,225.04 | 2,155.00 | 2,373.10 | 13 Oct 10:00 |
| ema_crossover | NSE:INFY | 15 | 1,039.61 | 1,031.00 | 1,053.66 | 13 Oct 09:45 |
| ema_crossover | NSE:TCS | 7 | 2,219.94 | 2,195.32 | 2,264.56 | 13 Oct 09:45 |
| ema_crossover | NSE:KOTAKBANK | -37 | 440.41 | 442.38 | 436.60 | 13 Oct 12:15 |
| vwap_pullback | NSE:INFY | 15 | 1,041.91 | 1,035.82 | 1,052.42 | 13 Oct 10:00 |
| vwap_pullback | NSE:RELIANCE | -14 | 1,159.87 | 1,163.62 | 1,152.77 | 13 Oct 10:45 |
| vwap_pullback | NSE:SUNPHARMA | -9 | 1,757.15 | 1,762.35 | 1,746.31 | 13 Oct 12:30 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| supertrend_intraday | NSE:HDFCBANK | 23 | 714.89 | 701.76 | 740.73 | 13 Oct 09:45 |
| supertrend_intraday | NSE:ICICIBANK | 12 | 1,345.87 | 1,331.26 | 1,374.28 | 13 Oct 09:45 |
| supertrend_intraday | NSE:INFY | 15 | 1,039.61 | 1,017.12 | 1,081.41 | 13 Oct 09:45 |
| hourly_macd_swing | NSE:TCS | 7 | 2,242.15 | 2,182.70 | 2,362.39 | 13 Oct 10:30 |
| vwap_reversion | NSE:KOTAKBANK | 37 | 440.59 | 438.52 | – | 13 Oct 12:15 |
| macd_adx | NSE:TCS | 7 | 2,219.94 | 2,195.32 | 2,264.56 | 13 Oct 09:45 |
| macd_adx | NSE:RELIANCE | -14 | 1,152.87 | 1,158.34 | 1,143.23 | 13 Oct 12:00 |
| macd_adx | NSE:SBIN | -17 | 942.11 | 945.92 | 934.31 | 13 Oct 12:30 |
| orb_breakout | NSE:RELIANCE | 14 | 1,164.63 | 1,152.20 | 1,188.50 | 13 Oct 10:00 |
| orb_breakout | NSE:ICICIBANK | 12 | 1,347.97 | 1,329.40 | 1,381.60 | 13 Oct 10:00 |
| orb_breakout | NSE:INFY | 15 | 1,041.91 | 1,027.00 | 1,070.05 | 13 Oct 10:00 |
| bb_squeeze | NSE:ICICIBANK | 12 | 1,345.87 | 1,339.30 | 1,358.21 | 13 Oct 09:45 |
| bb_squeeze | NSE:KOTAKBANK | -37 | 440.41 | 442.38 | 436.60 | 13 Oct 12:15 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.261364 | 83,345.55 | – | – | 13 Oct 09:30 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.68092 | 2,508.57 | – | – | 13 Oct 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
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
| 13 Oct 12:00 | macd_adx | SELL | 14 | NSE:RELIANCE | 1,152.87 |  | MACD down, ADX 22 |
| 13 Oct 11:55 | tv_rating_scalper | SELL | 16 | NSE:INFY | 1,049.19 | +275 | target |
| 13 Oct 11:30 | vwap_reversion | BUY | 9 | NSE:BHARTIARTL | 1,771.05 |  | -2.3 sigma below VWAP |
| 13 Oct 11:20 | bb_squeeze | SELL | 9 | NSE:BHARTIARTL | 1,773.45 | -109 | stop-loss |
| 13 Oct 10:45 | vwap_pullback | SELL | 14 | NSE:RELIANCE | 1,159.87 |  | rally rejected at VWAP in downtrend |
| 13 Oct 10:45 | tv_rating_scalper | BUY | 23 | NSE:HDFCBANK | 711.79 |  | TV 15m +0.54 / 1h +0.15 |
| 13 Oct 10:45 | rsi2_scalper | BUY | 9 | NSE:BHARTIARTL | 1,782.56 | +4 | time stop (1h) |
| 13 Oct 10:45 | rsi2_scalper | BUY | 17 | NSE:SBIN | 946.74 | -37 | time stop (1h) |
| 13 Oct 10:45 | rsi2_scalper | BUY | 14 | NSE:RELIANCE | 1,160.33 | +5 | RSI2 snapped back (18) |
| 13 Oct 10:35 | vwap_pullback | SELL | 23 | NSE:HDFCBANK | 711.76 | -80 | stop-loss |
| 13 Oct 10:30 | vwap_reversion | BUY | 9 | NSE:BHARTIARTL | 1,783.56 | +30 | back to VWAP |
| 13 Oct 10:30 | vwap_reversion | BUY | 13 | NSE:AXISBANK | 1,253.85 | +41 | back to VWAP |
| 13 Oct 10:30 | tv_rating_scalper | BUY | 4 | NSE:LT | 3,652.93 | -112 | 15m rating faded (+0.05) |
| 13 Oct 10:30 | hourly_macd_swing | BUY | 7 | NSE:TCS | 2,242.15 |  | 1h MACD bull cross above EMA200 |
| 13 Oct 10:00 | vwap_reversion | SELL | 9 | NSE:BHARTIARTL | 1,787.74 |  | 2.7 sigma above VWAP |
| 13 Oct 10:00 | vwap_reversion | SELL | 13 | NSE:AXISBANK | 1,257.65 |  | 2.7 sigma above VWAP |
| 13 Oct 10:00 | vwap_pullback | BUY | 15 | NSE:INFY | 1,041.91 |  | pullback held VWAP in uptrend |
| 13 Oct 10:00 | orb_breakout | BUY | 15 | NSE:INFY | 1,041.91 |  | ORB up > 1040.2 |
| 13 Oct 10:00 | orb_breakout | BUY | 12 | NSE:ICICIBANK | 1,347.97 |  | ORB up > 1346.1 |
| 13 Oct 10:00 | orb_breakout | BUY | 14 | NSE:RELIANCE | 1,164.63 |  | ORB up > 1162.9 |
