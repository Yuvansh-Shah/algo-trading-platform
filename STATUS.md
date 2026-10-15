# 🏆 Bot Leaderboard

_Updated 15 Oct 2026 15:25 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **momentum_rotation** | positional 1D | +3.09% | +1,545 | +559 | +1.23% | 0 | – | – | -1.3% | 3 | ✅ |
| 🥈 | **hourly_macd_swing** | swing 1h | +2.65% | +1,326 | +747 | +0.80% | 2 | 50 | 6.74 | -0.9% | 3 | ✅ |
| 🥉 | **supertrend_intraday** | intraday 15m | +2.00% | +998 | +705 | +0.14% | 9 | 67 | 5.19 | -0.5% | 0 | ✅ |
| 4 | **tv_rating_scalper** | intraday 15m | +1.99% | +994 | +184 | +0.13% | 21 | 57 | 2.07 | -0.9% | 0 | ✅ |
| 5 | **nifty_buy_hold** | benchmark 1D | +1.85% | +927 | +714 | +0.00% | 0 | – | – | -0.8% | 1 | ✅ |
| 6 | **gap_and_go** | intraday 15m | +1.75% | +873 | -23 | -0.11% | 6 | 83 | 6.87 | -0.8% | 0 | ✅ |
| 7 | **ema_crossover** | intraday 15m | +1.72% | +860 | +585 | -0.14% | 15 | 60 | 3.53 | -0.4% | 0 | ✅ |
| 8 | **tv_rating_swing** | swing 1D | +1.36% | +680 | +481 | -0.50% | 0 | – | – | -0.3% | 3 | ✅ |
| 9 | **orb_breakout** | intraday 15m | +0.77% | +387 | -58 | -1.08% | 9 | 67 | 2.02 | -0.8% | 0 | ✅ |
| 10 | **bb_squeeze** | intraday 15m | +0.24% | +121 | +245 | -1.61% | 11 | 55 | 1.55 | -0.6% | 0 | ✅ |
| 11 | **donchian_turtle** | swing 1D | +0.22% | +110 | +189 | -1.63% | 0 | – | – | -0.5% | 3 | ✅ |
| 12 | **vwap_pullback** | intraday 15m | +0.22% | +108 | +533 | -1.64% | 26 | 46 | 1.29 | -1.7% | 0 | ✅ |
| 13 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -1.85% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -1.85% | 0 | – | – | 0.0% | 0 | ✅ |
| 15 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -1.85% | 0 | – | – | 0.0% | 0 | ✅ |
| 16 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -1.85% | 0 | – | – | 0.0% | 0 | ✅ |
| 17 | **rsi2_scalper** | scalp 15m | -0.52% | -261 | -203 | -2.38% | 24 | 54 | 0.89 | -0.5% | 0 | ✅ |
| 18 | **vwap_reversion** | intraday 15m | -0.62% | -310 | +175 | -2.47% | 22 | 55 | 0.85 | -1.3% | 0 | ✅ |
| 19 | **macd_adx** | intraday 15m | -0.77% | -384 | +168 | -2.62% | 14 | 36 | 0.65 | -1.4% | 0 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -7.02% | -3,511 | +0 | -8.88% | 11 | 18 | 0.06 | -7.1% | 0 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
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
| hourly_macd_swing | NSE:AXISBANK | 13 | 1,267.25 | 1,254.59 | 1,315.81 | 15 Oct 09:25 |
| hourly_macd_swing | NSE:HDFCBANK | 23 | 720.34 | 710.61 | 738.03 | 15 Oct 10:30 |
| hourly_macd_swing | NSE:ICICIBANK | 12 | 1,364.17 | 1,347.36 | 1,397.28 | 15 Oct 11:30 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,532.36 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:AXISBANK | 13 | 1,286.66 | 1,196.91 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,289.26 | – | 15 Oct 15:05 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| donchian_turtle | NSE:ICICIBANK | 11 | 1,384.88 | 1,334.46 | – | 15 Oct 15:10 |
| donchian_turtle | NSE:INFY | 14 | 1,109.87 | 1,049.88 | – | 15 Oct 15:10 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 15 Oct 15:15 | vwap_reversion | BUY | 13 | NSE:RELIANCE | 1,206.34 | +141 | intraday square-off |
| 15 Oct 15:15 | vwap_reversion | BUY | 22 | NSE:HDFCBANK | 725.55 | +23 | intraday square-off |
| 15 Oct 15:15 | vwap_pullback | SELL | 12 | NSE:AXISBANK | 1,286.54 | -57 | intraday square-off |
| 15 Oct 15:15 | vwap_pullback | SELL | 17 | NSE:SBIN | 959.66 | +41 | intraday square-off |
| 15 Oct 15:15 | vwap_pullback | SELL | 6 | NSE:TCS | 2,359.13 | +28 | intraday square-off |
| 15 Oct 15:15 | tv_rating_scalper | SELL | 23 | NSE:HDFCBANK | 725.25 | -54 | intraday square-off |
| 15 Oct 15:15 | tv_rating_scalper | SELL | 37 | NSE:KOTAKBANK | 445.46 | +52 | intraday square-off |
| 15 Oct 15:15 | tv_rating_scalper | SELL | 63 | NSE:ITC | 264.20 | +95 | intraday square-off |
| 15 Oct 15:15 | supertrend_intraday | SELL | 12 | NSE:ICICIBANK | 1,384.82 | +295 | intraday square-off |
| 15 Oct 15:15 | supertrend_intraday | SELL | 23 | NSE:HDFCBANK | 725.25 | +181 | intraday square-off |
| 15 Oct 15:15 | supertrend_intraday | SELL | 13 | NSE:AXISBANK | 1,286.54 | +242 | intraday square-off |
| 15 Oct 15:15 | rsi2_scalper | SELL | 9 | NSE:SUNPHARMA | 1,761.65 | -41 | intraday square-off |
| 15 Oct 15:15 | rsi2_scalper | SELL | 8 | NSE:BHARTIARTL | 1,847.93 | -103 | intraday square-off |
| 15 Oct 15:15 | orb_breakout | SELL | 15 | NSE:INFY | 1,109.03 | -85 | intraday square-off |
| 15 Oct 15:15 | orb_breakout | SELL | 13 | NSE:AXISBANK | 1,286.54 | +242 | intraday square-off |
| 15 Oct 15:15 | gap_and_go | SELL | 7 | NSE:TCS | 2,359.13 | -157 | intraday square-off |
| 15 Oct 15:15 | gap_and_go | SELL | 15 | NSE:INFY | 1,109.03 | +139 | intraday square-off |
| 15 Oct 15:15 | ema_crossover | SELL | 9 | NSE:SUNPHARMA | 1,762.25 | +30 | intraday square-off |
| 15 Oct 15:15 | bb_squeeze | SELL | 17 | NSE:SBIN | 959.66 | +59 | intraday square-off |
| 15 Oct 15:10 | donchian_turtle | BUY | 14 | NSE:INFY | 1,109.87 |  | 20-day breakout > 1096.4 |
| 15 Oct 15:10 | donchian_turtle | BUY | 11 | NSE:ICICIBANK | 1,384.88 |  | 20-day breakout > 1364.6 |
| 15 Oct 15:05 | tv_rating_swing | BUY | 12 | NSE:ICICIBANK | 1,383.98 |  | TV STRONG BUY +0.54, RSI 57 |
| 15 Oct 15:05 | tv_rating_swing | BUY | 13 | NSE:AXISBANK | 1,286.66 |  | TV STRONG BUY +0.56, RSI 62 |
| 15 Oct 14:45 | rsi2_scalper | BUY | 9 | NSE:SUNPHARMA | 1,765.35 |  | RSI2 10 in uptrend |
| 15 Oct 14:30 | vwap_reversion | BUY | 8 | NSE:BHARTIARTL | 1,854.87 | +43 | back to VWAP |
| 15 Oct 14:15 | vwap_reversion | SELL | 13 | NSE:RELIANCE | 1,217.76 |  | 3.2 sigma above VWAP |
| 15 Oct 14:15 | rsi2_scalper | BUY | 8 | NSE:BHARTIARTL | 1,859.87 |  | RSI2 5 in uptrend |
| 15 Oct 14:15 | rsi2_scalper | SELL | 6 | NSE:TCS | 2,361.03 | +14 | RSI2 snapped back (71) |
| 15 Oct 14:15 | macd_adx | SELL | 61 | NSE:ITC | 264.85 | -42 | MACD reversed |
| 15 Oct 14:10 | vwap_reversion | BUY | 13 | NSE:RELIANCE | 1,215.94 | -138 | stop-loss |
