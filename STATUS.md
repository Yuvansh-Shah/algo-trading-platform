# 🏆 Bot Leaderboard

_Updated 14 Oct 2026 14:35 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **gap_and_go** | intraday 15m | +1.83% | +914 | +438 | +1.41% | 2 | 100 | ∞ | -0.6% | 2 | ✅ |
| 🥈 | **tv_rating_scalper** | intraday 15m | +1.70% | +851 | +161 | +1.29% | 12 | 50 | 2.11 | -0.9% | 2 | ✅ |
| 🥉 | **orb_breakout** | intraday 15m | +0.96% | +478 | +29 | +0.54% | 4 | 75 | 2.90 | -0.6% | 2 | ✅ |
| 4 | **momentum_rotation** | positional 1D | +0.80% | +398 | +248 | +0.38% | 0 | – | – | -1.3% | 3 | ✅ |
| 5 | **ema_crossover** | intraday 15m | +0.77% | +386 | +44 | +0.36% | 8 | 50 | 1.98 | -0.4% | 2 | ✅ |
| 6 | **supertrend_intraday** | intraday 15m | +0.72% | +360 | -130 | +0.30% | 4 | 50 | 3.18 | -0.5% | 2 | ✅ |
| 7 | **hourly_macd_swing** | swing 1h | +0.52% | +260 | +34 | +0.10% | 1 | 0 | 0.00 | -0.9% | 1 | ✅ |
| 8 | **nifty_buy_hold** | benchmark 1D | +0.41% | +207 | -278 | +0.00% | 0 | – | – | -0.8% | 1 | ✅ |
| 9 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -0.41% | 0 | – | – | 0.0% | 0 | ✅ |
| 10 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -0.41% | 0 | – | – | 0.0% | 0 | ✅ |
| 11 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -0.41% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -0.41% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **tv_rating_swing** | swing 1D | +0.00% | +0 | +0 | -0.41% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **rsi2_scalper** | scalp 15m | -0.12% | -58 | +89 | -0.53% | 16 | 56 | 1.23 | -0.4% | 0 | ✅ |
| 15 | **donchian_turtle** | swing 1D | -0.20% | -98 | +4 | -0.61% | 0 | – | – | -0.5% | 1 | ✅ |
| 16 | **bb_squeeze** | intraday 15m | -0.28% | -142 | -173 | -0.70% | 7 | 43 | 0.93 | -0.6% | 1 | ✅ |
| 17 | **vwap_pullback** | intraday 15m | -0.79% | -393 | -279 | -1.20% | 17 | 24 | 0.67 | -1.7% | 2 | ✅ |
| 18 | **vwap_reversion** | intraday 15m | -0.91% | -457 | -253 | -1.33% | 12 | 50 | 0.51 | -1.1% | 3 | ✅ |
| 19 | **macd_adx** | intraday 15m | -1.08% | -540 | -418 | -1.49% | 8 | 12 | 0.22 | -1.4% | 2 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -3.19% | -1,597 | -136 | -3.61% | 9 | 22 | 0.12 | -3.6% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| gap_and_go | NSE:INFY | 15 | 1,073.91 | 1,027.00 | 1,129.30 | 14 Oct 09:25 |
| gap_and_go | NSE:TCS | 7 | 2,274.45 | 2,155.00 | 2,482.00 | 14 Oct 09:25 |
| tv_rating_scalper | NSE:SUNPHARMA | -9 | 1,749.85 | 1,764.20 | 1,722.20 | 14 Oct 11:45 |
| tv_rating_scalper | NSE:LT | -4 | 3,629.47 | 3,659.24 | 3,572.12 | 14 Oct 13:15 |
| orb_breakout | NSE:RELIANCE | 14 | 1,171.83 | 1,162.70 | 1,186.70 | 14 Oct 10:00 |
| orb_breakout | NSE:INFY | 15 | 1,087.62 | 1,069.45 | 1,122.55 | 14 Oct 10:30 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| ema_crossover | NSE:ICICIBANK | -12 | 1,348.63 | 1,354.75 | 1,338.09 | 14 Oct 11:30 |
| ema_crossover | NSE:HDFCBANK | -23 | 709.61 | 712.52 | 702.42 | 14 Oct 13:30 |
| supertrend_intraday | NSE:AXISBANK | -13 | 1,259.65 | 1,278.69 | 1,222.62 | 14 Oct 09:45 |
| supertrend_intraday | NSE:ICICIBANK | -12 | 1,351.23 | 1,365.86 | 1,322.79 | 14 Oct 10:15 |
| hourly_macd_swing | NSE:TCS | 7 | 2,242.15 | 2,182.70 | 2,362.39 | 13 Oct 10:30 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| bb_squeeze | NSE:INFY | 15 | 1,094.27 | 1,085.28 | 1,108.74 | 14 Oct 14:30 |
| vwap_pullback | NSE:RELIANCE | 13 | 1,178.24 | 1,174.95 | 1,187.40 | 14 Oct 13:50 |
| vwap_pullback | NSE:ITC | 62 | 261.35 | 260.57 | 262.91 | 14 Oct 14:00 |
| vwap_reversion | NSE:HDFCBANK | 23 | 709.89 | 705.78 | – | 14 Oct 13:30 |
| vwap_reversion | NSE:KOTAKBANK | 37 | 439.74 | 437.45 | – | 14 Oct 13:30 |
| vwap_reversion | NSE:SUNPHARMA | 9 | 1,727.15 | 1,717.53 | – | 14 Oct 13:30 |
| macd_adx | NSE:KOTAKBANK | -37 | 441.21 | 443.77 | 437.10 | 14 Oct 13:15 |
| macd_adx | NSE:RELIANCE | 13 | 1,185.64 | 1,179.12 | 1,198.86 | 14 Oct 14:15 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.261364 | 83,345.55 | – | – | 13 Oct 09:30 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.68092 | 2,508.57 | – | – | 13 Oct 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 14 Oct 14:30 | vwap_pullback | SELL | 15 | NSE:INFY | 1,093.83 | +187 | target |
| 14 Oct 14:31 | rsi2_scalper | SELL | 9 | NSE:BHARTIARTL | 1,799.14 | -95 | time stop (1h) |
| 14 Oct 14:30 | bb_squeeze | BUY | 15 | NSE:INFY | 1,094.27 |  | squeeze breakout up |
| 14 Oct 14:15 | supertrend_intraday | SELL | 37 | NSE:KOTAKBANK | 439.11 | -150 | Supertrend reversed |
| 14 Oct 14:15 | rsi2_scalper | SELL | 63 | NSE:ITC | 261.90 | +17 | RSI2 snapped back (90) |
| 14 Oct 14:15 | macd_adx | BUY | 13 | NSE:RELIANCE | 1,185.64 |  | MACD up, ADX 34 |
| 14 Oct 14:10 | macd_adx | BUY | 17 | NSE:SBIN | 951.79 | -83 | stop-loss |
| 14 Oct 14:05 | ema_crossover | BUY | 4 | NSE:LT | 3,627.53 | -93 | stop-loss |
| 14 Oct 14:00 | vwap_pullback | BUY | 62 | NSE:ITC | 261.35 |  | pullback held VWAP in uptrend |
| 14 Oct 13:55 | vwap_pullback | SELL | 7 | NSE:TCS | 2,298.14 | -54 | stop-loss |
| 14 Oct 13:50 | vwap_pullback | BUY | 7 | NSE:TCS | 2,304.66 |  | pullback held VWAP in uptrend |
| 14 Oct 13:50 | vwap_pullback | BUY | 13 | NSE:RELIANCE | 1,178.24 |  | pullback held VWAP in uptrend |
| 14 Oct 13:50 | tv_rating_scalper | SELL | 9 | NSE:BHARTIARTL | 1,802.44 | -129 | 15m rating faded (+0.00) |
| 14 Oct 13:50 | rsi2_scalper | BUY | 63 | NSE:ITC | 261.50 |  | RSI2 5 in uptrend |
| 14 Oct 13:50 | rsi2_scalper | SELL | 7 | NSE:TCS | 2,303.74 | +58 | RSI2 snapped back (91) |
| 14 Oct 13:50 | rsi2_scalper | SELL | 15 | NSE:INFY | 1,084.08 | +49 | RSI2 snapped back (74) |
| 14 Oct 13:30 | vwap_reversion | BUY | 9 | NSE:SUNPHARMA | 1,727.15 |  | -3.2 sigma below VWAP |
| 14 Oct 13:30 | vwap_reversion | BUY | 9 | NSE:BHARTIARTL | 1,809.46 | +43 | back to VWAP |
| 14 Oct 13:30 | vwap_reversion | BUY | 37 | NSE:KOTAKBANK | 439.74 |  | -2.5 sigma below VWAP |
| 14 Oct 13:30 | vwap_reversion | BUY | 23 | NSE:HDFCBANK | 709.89 |  | -2.6 sigma below VWAP |
| 14 Oct 13:30 | vwap_reversion | BUY | 13 | NSE:RELIANCE | 1,176.34 | +103 | back to VWAP |
| 14 Oct 13:30 | rsi2_scalper | BUY | 9 | NSE:BHARTIARTL | 1,808.76 |  | RSI2 5 in uptrend |
| 14 Oct 13:30 | macd_adx | SELL | 17 | NSE:SBIN | 947.41 |  | MACD down, ADX 23 |
| 14 Oct 13:30 | hourly_macd_swing | SELL | 13 | NSE:AXISBANK | 1,254.35 | -129 | 1h MACD bear cross |
| 14 Oct 13:30 | ema_crossover | SELL | 4 | NSE:LT | 3,606.08 |  | EMA9<21, RSI 32 |
| 14 Oct 13:30 | ema_crossover | SELL | 23 | NSE:HDFCBANK | 709.61 |  | EMA9<21, RSI 41 |
| 14 Oct 13:25 | vwap_reversion | SELL | 9 | NSE:SUNPHARMA | 1,726.75 | -82 | stop-loss |
| 14 Oct 13:25 | vwap_pullback | SELL | 17 | NSE:SBIN | 947.06 | -71 | stop-loss |
| 14 Oct 13:25 | macd_adx | SELL | 17 | NSE:SBIN | 947.06 | -132 | stop-loss |
| 14 Oct 13:20 | vwap_pullback | BUY | 9 | NSE:SUNPHARMA | 1,730.35 | +116 | target |
