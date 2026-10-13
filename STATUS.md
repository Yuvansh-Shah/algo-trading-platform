# 🏆 Bot Leaderboard

_Updated 13 Oct 2026 15:40 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **tv_rating_scalper** | intraday 15m | +1.45% | +723 | +734 | +0.52% | 7 | 71 | 4.53 | -0.5% | 0 | ✅ |
| 🥈 | **gap_and_go** | intraday 15m | +1.00% | +498 | +498 | +0.07% | 2 | 100 | ∞ | -0.5% | 0 | ✅ |
| 🥉 | **supertrend_intraday** | intraday 15m | +0.98% | +490 | +490 | +0.05% | 3 | 67 | 31.05 | -0.4% | 0 | ✅ |
| 4 | **nifty_buy_hold** | benchmark 1D | +0.93% | +465 | +465 | +0.00% | 0 | – | – | -0.3% | 1 | ✅ |
| 5 | **orb_breakout** | intraday 15m | +0.90% | +449 | +449 | -0.03% | 3 | 100 | ∞ | -0.6% | 0 | ✅ |
| 6 | **ema_crossover** | intraday 15m | +0.68% | +342 | +342 | -0.25% | 5 | 60 | 3.53 | -0.4% | 0 | ✅ |
| 7 | **hourly_macd_swing** | swing 1h | +0.43% | +216 | +216 | -0.50% | 0 | – | – | -0.2% | 2 | ✅ |
| 8 | **bb_squeeze** | intraday 15m | +0.11% | +54 | +54 | -0.82% | 3 | 67 | 1.72 | -0.4% | 0 | ✅ |
| 9 | **momentum_rotation** | positional 1D | +0.08% | +41 | +41 | -0.85% | 0 | – | – | -0.1% | 3 | ✅ |
| 10 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -0.93% | 0 | – | – | 0.0% | 0 | ✅ |
| 11 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -0.93% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -0.93% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -0.93% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **tv_rating_swing** | swing 1D | +0.00% | +0 | +0 | -0.93% | 0 | – | – | 0.0% | 0 | ✅ |
| 15 | **donchian_turtle** | swing 1D | -0.03% | -13 | -13 | -0.96% | 0 | – | – | -0.1% | 1 | ✅ |
| 16 | **vwap_pullback** | intraday 15m | -0.23% | -114 | -114 | -1.16% | 8 | 25 | 0.89 | -0.6% | 0 | ✅ |
| 17 | **macd_adx** | intraday 15m | -0.24% | -121 | -121 | -1.17% | 4 | 25 | 0.63 | -0.5% | 0 | ✅ |
| 18 | **rsi2_scalper** | scalp 15m | -0.29% | -147 | -147 | -1.22% | 7 | 43 | 0.43 | -0.4% | 0 | ✅ |
| 19 | **vwap_reversion** | intraday 15m | -0.41% | -204 | -204 | -1.34% | 7 | 57 | 0.50 | -0.6% | 0 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -3.06% | -1,530 | +72 | -3.99% | 9 | 22 | 0.12 | -3.6% | 2 | ✅ |

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
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| hourly_macd_swing | NSE:TCS | 7 | 2,242.15 | 2,182.70 | 2,362.39 | 13 Oct 10:30 |
| hourly_macd_swing | NSE:AXISBANK | 13 | 1,263.65 | 1,245.45 | 1,299.89 | 13 Oct 14:30 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.261364 | 83,345.55 | – | – | 13 Oct 09:30 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.68092 | 2,508.57 | – | – | 13 Oct 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 13 Oct 15:15 | vwap_reversion | SELL | 37 | NSE:KOTAKBANK | 438.81 | +19 | intraday square-off |
| 13 Oct 15:15 | tv_rating_scalper | SELL | 12 | NSE:ICICIBANK | 1,362.03 | +139 | intraday square-off |
| 13 Oct 15:15 | tv_rating_scalper | SELL | 23 | NSE:HDFCBANK | 714.51 | +54 | intraday square-off |
| 13 Oct 15:15 | supertrend_intraday | SELL | 15 | NSE:INFY | 1,063.14 | +345 | intraday square-off |
| 13 Oct 15:15 | supertrend_intraday | SELL | 12 | NSE:ICICIBANK | 1,362.03 | +186 | intraday square-off |
| 13 Oct 15:15 | supertrend_intraday | SELL | 23 | NSE:HDFCBANK | 714.51 | -17 | intraday square-off |
| 13 Oct 15:15 | rsi2_scalper | BUY | 14 | NSE:RELIANCE | 1,165.13 | -59 | intraday square-off |
| 13 Oct 15:15 | orb_breakout | SELL | 15 | NSE:INFY | 1,063.14 | +310 | intraday square-off |
| 13 Oct 15:15 | orb_breakout | SELL | 12 | NSE:ICICIBANK | 1,362.03 | +161 | intraday square-off |
| 13 Oct 15:15 | orb_breakout | SELL | 14 | NSE:RELIANCE | 1,165.37 | +2 | intraday square-off |
| 13 Oct 15:15 | gap_and_go | SELL | 7 | NSE:TCS | 2,257.45 | +219 | intraday square-off |
| 13 Oct 15:15 | gap_and_go | SELL | 15 | NSE:INFY | 1,062.09 | +295 | intraday square-off |
| 13 Oct 15:15 | ema_crossover | BUY | 37 | NSE:KOTAKBANK | 438.99 | +45 | intraday square-off |
| 13 Oct 15:15 | ema_crossover | SELL | 7 | NSE:TCS | 2,257.45 | +255 | intraday square-off |
| 13 Oct 15:15 | bb_squeeze | BUY | 37 | NSE:KOTAKBANK | 438.99 | +45 | intraday square-off |
| 13 Oct 15:10 | vwap_pullback | BUY | 63 | NSE:ITC | 260.20 | -68 | stop-loss |
| 13 Oct 15:10 | momentum_rotation | BUY | 7 | NSE:TCS | 2,256.35 |  | 3M perf +3.8% |
| 13 Oct 15:10 | momentum_rotation | BUY | 12 | NSE:HCLTECH | 1,314.16 |  | 3M perf +13.6% |
| 13 Oct 15:10 | momentum_rotation | BUY | 37 | NSE:KOTAKBANK | 439.54 |  | 3M perf +15.8% |
| 13 Oct 15:10 | donchian_turtle | BUY | 12 | NSE:AXISBANK | 1,272.95 |  | 20-day breakout > 1266.0 |
| 13 Oct 15:00 | vwap_pullback | BUY | 14 | NSE:RELIANCE | 1,164.43 | -72 | stop-loss |
| 13 Oct 14:55 | vwap_reversion | BUY | 12 | NSE:ICICIBANK | 1,360.27 | -84 | stop-loss |
| 13 Oct 14:55 | vwap_pullback | BUY | 9 | NSE:SUNPHARMA | 1,763.25 | -63 | stop-loss |
| 13 Oct 14:50 | bb_squeeze | SELL | 12 | NSE:ICICIBANK | 1,358.43 | +143 | target |
| 13 Oct 14:45 | rsi2_scalper | SELL | 14 | NSE:RELIANCE | 1,161.47 |  | RSI2 96 in downtrend |
| 13 Oct 14:45 | ema_crossover | SELL | 9 | NSE:SUNPHARMA | 1,759.65 | -31 | opposite EMA cross |
| 13 Oct 14:35 | vwap_reversion | BUY | 13 | NSE:AXISBANK | 1,264.05 | -102 | stop-loss |
| 13 Oct 14:30 | rsi2_scalper | BUY | 17 | NSE:SBIN | 946.69 | -55 | time stop (1h) |
| 13 Oct 14:30 | rsi2_scalper | SELL | 7 | NSE:TCS | 2,253.25 | +58 | RSI2 snapped back (80) |
| 13 Oct 14:30 | hourly_macd_swing | BUY | 13 | NSE:AXISBANK | 1,263.65 |  | 1h MACD bull cross above EMA200 |
