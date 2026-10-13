# 🏆 Bot Leaderboard

_Updated 13 Oct 2026 09:45 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **tv_rating_scalper** | intraday 15m | +0.79% | +393 | +404 | +0.86% | 1 | 100 | ∞ | -0.0% | 3 | ✅ |
| 🥈 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | +0.07% | 0 | – | – | 0.0% | 0 | ✅ |
| 🥉 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | +0.07% | 0 | – | – | 0.0% | 0 | ✅ |
| 4 | **donchian_turtle** | swing 1D | +0.00% | +0 | +0 | +0.07% | 0 | – | – | 0.0% | 0 | ✅ |
| 5 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | +0.07% | 0 | – | – | 0.0% | 0 | ✅ |
| 6 | **external_signals** | claude 15m | +0.00% | +0 | +0 | +0.07% | 0 | – | – | 0.0% | 0 | ✅ |
| 7 | **gap_and_go** | intraday 15m | +0.00% | +0 | +0 | +0.07% | 0 | – | – | 0.0% | 0 | ✅ |
| 8 | **hourly_macd_swing** | swing 1h | +0.00% | +0 | +0 | +0.07% | 0 | – | – | 0.0% | 0 | ✅ |
| 9 | **momentum_rotation** | positional 1D | +0.00% | +0 | +0 | +0.07% | 0 | – | – | 0.0% | 0 | ✅ |
| 10 | **orb_breakout** | intraday 15m | +0.00% | +0 | +0 | +0.07% | 0 | – | – | 0.0% | 0 | ✅ |
| 11 | **tv_rating_swing** | swing 1D | +0.00% | +0 | +0 | +0.07% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **vwap_reversion** | intraday 15m | +0.00% | +0 | +0 | +0.07% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **macd_adx** | intraday 15m | -0.04% | -22 | -22 | +0.02% | 0 | – | – | -0.0% | 2 | ✅ |
| 14 | **bb_squeeze** | intraday 15m | -0.05% | -23 | -23 | +0.02% | 0 | – | – | -0.0% | 2 | ✅ |
| 15 | **ema_crossover** | intraday 15m | -0.07% | -33 | -33 | +0.00% | 0 | – | – | -0.1% | 3 | ✅ |
| 16 | **vwap_pullback** | intraday 15m | -0.07% | -33 | -33 | +0.00% | 0 | – | – | -0.1% | 3 | ✅ |
| 17 | **supertrend_intraday** | intraday 15m | -0.07% | -34 | -34 | +0.00% | 0 | – | – | -0.1% | 3 | ✅ |
| 18 | **rsi2_scalper** | scalp 15m | -0.07% | -34 | -34 | +0.00% | 0 | – | – | -0.1% | 3 | ✅ |
| 19 | **nifty_buy_hold** | benchmark 1D | -0.07% | -34 | -34 | +0.00% | 0 | – | – | -0.1% | 1 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -3.24% | -1,622 | -20 | -3.17% | 9 | 22 | 0.12 | -3.6% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| tv_rating_scalper | NSE:LT | -4 | 3,626.77 | 3,656.52 | 3,569.46 | 13 Oct 09:25 |
| tv_rating_scalper | NSE:INFY | 16 | 1,031.46 | 1,023.00 | 1,047.75 | 13 Oct 09:30 |
| tv_rating_scalper | NSE:TCS | 7 | 2,219.94 | 2,201.74 | 2,255.01 | 13 Oct 09:45 |
| macd_adx | NSE:HDFCBANK | 23 | 714.89 | 710.75 | 722.76 | 13 Oct 09:45 |
| macd_adx | NSE:TCS | 7 | 2,219.94 | 2,195.32 | 2,264.56 | 13 Oct 09:45 |
| bb_squeeze | NSE:ICICIBANK | 12 | 1,345.87 | 1,339.30 | 1,358.21 | 13 Oct 09:45 |
| bb_squeeze | NSE:BHARTIARTL | 9 | 1,784.66 | 1,774.88 | 1,800.73 | 13 Oct 09:45 |
| ema_crossover | NSE:HDFCBANK | 23 | 714.89 | 710.75 | 722.76 | 13 Oct 09:45 |
| ema_crossover | NSE:INFY | 15 | 1,039.61 | 1,031.00 | 1,053.66 | 13 Oct 09:45 |
| ema_crossover | NSE:TCS | 7 | 2,219.94 | 2,195.32 | 2,264.56 | 13 Oct 09:45 |
| vwap_pullback | NSE:HDFCBANK | 23 | 714.89 | 712.08 | 720.09 | 13 Oct 09:45 |
| vwap_pullback | NSE:INFY | 15 | 1,039.61 | 1,033.51 | 1,048.62 | 13 Oct 09:45 |
| vwap_pullback | NSE:TCS | 7 | 2,219.94 | 2,203.01 | 2,249.18 | 13 Oct 09:45 |
| supertrend_intraday | NSE:HDFCBANK | 23 | 714.89 | 701.76 | 740.73 | 13 Oct 09:45 |
| supertrend_intraday | NSE:ICICIBANK | 12 | 1,345.87 | 1,331.26 | 1,374.28 | 13 Oct 09:45 |
| supertrend_intraday | NSE:INFY | 15 | 1,039.61 | 1,017.12 | 1,081.41 | 13 Oct 09:45 |
| rsi2_scalper | NSE:RELIANCE | -14 | 1,161.27 | 1,170.79 | – | 13 Oct 09:45 |
| rsi2_scalper | NSE:SBIN | -17 | 945.01 | 952.76 | – | 13 Oct 09:45 |
| rsi2_scalper | NSE:BHARTIARTL | -9 | 1,783.94 | 1,798.57 | – | 13 Oct 09:45 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.261364 | 83,345.55 | – | – | 13 Oct 09:30 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.68092 | 2,508.57 | – | – | 13 Oct 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 13 Oct 09:45 | vwap_pullback | BUY | 7 | NSE:TCS | 2,219.94 |  | pullback held VWAP in uptrend |
| 13 Oct 09:45 | vwap_pullback | BUY | 15 | NSE:INFY | 1,039.61 |  | pullback held VWAP in uptrend |
| 13 Oct 09:45 | vwap_pullback | BUY | 23 | NSE:HDFCBANK | 714.89 |  | pullback held VWAP in uptrend |
| 13 Oct 09:45 | tv_rating_scalper | BUY | 7 | NSE:TCS | 2,219.94 |  | TV 15m +0.60 / 1h +0.65 |
| 13 Oct 09:45 | tv_rating_scalper | SELL | 7 | NSE:TCS | 2,219.06 | +267 | target |
| 13 Oct 09:45 | supertrend_intraday | BUY | 15 | NSE:INFY | 1,039.61 |  | Supertrend flipped up |
| 13 Oct 09:45 | supertrend_intraday | BUY | 12 | NSE:ICICIBANK | 1,345.87 |  | Supertrend flipped up |
| 13 Oct 09:45 | supertrend_intraday | BUY | 23 | NSE:HDFCBANK | 714.89 |  | Supertrend flipped up |
| 13 Oct 09:45 | rsi2_scalper | SELL | 9 | NSE:BHARTIARTL | 1,783.94 |  | RSI2 98 in downtrend |
| 13 Oct 09:45 | rsi2_scalper | SELL | 17 | NSE:SBIN | 945.01 |  | RSI2 95 in downtrend |
| 13 Oct 09:45 | rsi2_scalper | SELL | 14 | NSE:RELIANCE | 1,161.27 |  | RSI2 97 in downtrend |
| 13 Oct 09:45 | nifty_buy_hold | BUY | 192 | NSE:NIFTYBEES | 256.54 |  | benchmark buy & hold |
| 13 Oct 09:45 | macd_adx | BUY | 7 | NSE:TCS | 2,219.94 |  | MACD up, ADX 22 |
| 13 Oct 09:45 | macd_adx | BUY | 23 | NSE:HDFCBANK | 714.89 |  | MACD up, ADX 25 |
| 13 Oct 09:45 | ema_crossover | BUY | 7 | NSE:TCS | 2,219.94 |  | EMA9>21, RSI 75 |
| 13 Oct 09:45 | ema_crossover | BUY | 15 | NSE:INFY | 1,039.61 |  | EMA9>21, RSI 74 |
| 13 Oct 09:45 | ema_crossover | BUY | 23 | NSE:HDFCBANK | 714.89 |  | EMA9>21, RSI 72 |
| 13 Oct 09:45 | bb_squeeze | BUY | 9 | NSE:BHARTIARTL | 1,784.66 |  | squeeze breakout up |
| 13 Oct 09:45 | bb_squeeze | BUY | 12 | NSE:ICICIBANK | 1,345.87 |  | squeeze breakout up |
| 13 Oct 09:30 | tv_rating_scalper | BUY | 16 | NSE:INFY | 1,031.46 |  | TV 15m +0.56 / 1h +0.52 |
| 13 Oct 09:30 | tv_rating_scalper | BUY | 7 | NSE:TCS | 2,179.84 |  | TV 15m +0.60 / 1h +0.45 |
| 13 Oct 09:30 | crypto_supertrend | BUY | 8.68092 | BINANCE:ETHUSDT | 2,508.57 |  | Supertrend up |
| 13 Oct 09:30 | crypto_supertrend | BUY | 0.261364 | BINANCE:BTCUSDT | 83,345.55 |  | Supertrend up |
| 13 Oct 09:25 | tv_rating_scalper | SELL | 4 | NSE:LT | 3,626.77 |  | TV 15m -0.54 / 1h -0.54 |
| 12 Oct 22:53 | crypto_supertrend | SELL | 8.69791 | BINANCE:ETHUSDT | 2,515.51 | +120 | Supertrend turned down |
| 12 Oct 22:53 | crypto_supertrend | SELL | 0.263176 | BINANCE:BTCUSDT | 82,569.48 | -36 | Supertrend turned down |
| 09 Oct 15:56 | crypto_supertrend | BUY | 8.69791 | BINANCE:ETHUSDT | 2,500.49 |  | Supertrend up |
| 09 Oct 15:56 | crypto_supertrend | BUY | 0.263176 | BINANCE:BTCUSDT | 82,666.53 |  | Supertrend up |
| 07 Oct 15:39 | crypto_supertrend | SELL | 0.256707 | BINANCE:BTCUSDT | 83,745.25 | -497 | Supertrend turned down |
| 06 Oct 22:27 | crypto_supertrend | BUY | 0.256707 | BINANCE:BTCUSDT | 85,641.13 |  | Supertrend up |
