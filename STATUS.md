# 🏆 Bot Leaderboard

_Updated 05 Oct 2026 15:49 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 🥈 | **bb_squeeze** | intraday 15m | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 🥉 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 4 | **donchian_turtle** | swing 1D | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 5 | **ema_crossover** | intraday 15m | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 6 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 7 | **external_signals** | claude 15m | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 8 | **gap_and_go** | intraday 15m | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 9 | **hourly_macd_swing** | swing 1h | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 10 | **macd_adx** | intraday 15m | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 11 | **momentum_rotation** | positional 1D | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **nifty_buy_hold** | benchmark 1D | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **orb_breakout** | intraday 15m | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **rsi2_scalper** | scalp 15m | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 15 | **supertrend_intraday** | intraday 15m | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 16 | **tv_rating_scalper** | intraday 15m | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 17 | **tv_rating_swing** | swing 1D | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 18 | **vwap_pullback** | intraday 15m | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 19 | **vwap_reversion** | intraday 15m | +0.00% | +0 | +0 | +0.00% | 0 | – | – | 0.0% | 0 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -2.15% | -1,077 | +0 | -2.15% | 5 | 20 | 0.07 | -2.6% | 1 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| crypto_supertrend | BINANCE:ETHUSDT | 8.1009 | 2,719.02 | – | – | 05 Oct 15:49 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 05 Oct 15:49 | crypto_supertrend | BUY | 8.1009 | BINANCE:ETHUSDT | 2,719.02 |  | Supertrend up |
| 03 Oct 10:25 | crypto_supertrend | SELL | 8.20884 | BINANCE:ETHUSDT | 2,675.26 | -106 | Supertrend turned down |
| 03 Oct 10:25 | crypto_supertrend | SELL | 0.263638 | BINANCE:BTCUSDT | 84,570.36 | +80 | Supertrend turned down |
| 30 Sep 21:44 | crypto_supertrend | BUY | 8.20884 | BINANCE:ETHUSDT | 2,686.86 |  | Supertrend up |
| 29 Sep 21:48 | crypto_supertrend | SELL | 8.20668 | BINANCE:ETHUSDT | 2,677.52 | -165 | Supertrend turned down |
| 29 Sep 15:39 | crypto_supertrend | BUY | 0.263638 | BINANCE:BTCUSDT | 84,224.85 |  | Supertrend up |
| 28 Sep 23:36 | crypto_supertrend | BUY | 8.20668 | BINANCE:ETHUSDT | 2,696.28 |  | Supertrend up |
| 28 Sep 15:41 | crypto_supertrend | SELL | 0.264796 | BINANCE:BTCUSDT | 82,705.38 | -615 | Supertrend turned down |
| 27 Sep 23:42 | crypto_supertrend | SELL | 8.28893 | BINANCE:ETHUSDT | 2,691.40 | -200 | Supertrend turned down |
| 27 Sep 18:22 | crypto_supertrend | BUY | 8.28893 | BINANCE:ETHUSDT | 2,714.15 |  | Supertrend up |
| 27 Sep 18:22 | crypto_supertrend | BUY | 0.264796 | BINANCE:BTCUSDT | 84,988.00 |  | Supertrend up |
