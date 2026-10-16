# 🏆 Bot Leaderboard

_Updated 16 Oct 2026 14:50 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **momentum_rotation** | positional 1D | +4.67% | +2,334 | +590 | +2.00% | 0 | – | – | -1.3% | 3 | ✅ |
| 🥈 | **tv_rating_swing** | swing 1D | +4.04% | +2,019 | +541 | +1.37% | 0 | – | – | -0.4% | 3 | ✅ |
| 🥉 | **hourly_macd_swing** | swing 1h | +2.88% | +1,438 | -102 | +0.21% | 4 | 75 | 11.42 | -0.9% | 1 | ✅ |
| 4 | **nifty_buy_hold** | benchmark 1D | +2.67% | +1,333 | +403 | +0.00% | 0 | – | – | -0.8% | 1 | ✅ |
| 5 | **gap_and_go** | intraday 15m | +1.92% | +960 | +86 | -0.75% | 6 | 83 | 6.87 | -1.0% | 2 | ✅ |
| 6 | **donchian_turtle** | swing 1D | +1.53% | +765 | +226 | -1.13% | 0 | – | – | -0.5% | 3 | ✅ |
| 7 | **tv_rating_scalper** | intraday 15m | +0.89% | +444 | -540 | -1.78% | 26 | 46 | 1.51 | -1.4% | 2 | ✅ |
| 8 | **supertrend_intraday** | intraday 15m | +0.72% | +359 | -640 | -1.95% | 10 | 60 | 2.77 | -1.6% | 3 | ✅ |
| 9 | **vwap_pullback** | intraday 15m | +0.67% | +335 | +228 | -1.99% | 31 | 48 | 1.51 | -1.7% | 2 | ✅ |
| 10 | **ema_crossover** | intraday 15m | +0.65% | +326 | -534 | -2.01% | 20 | 45 | 1.54 | -1.3% | 1 | ✅ |
| 11 | **orb_breakout** | intraday 15m | +0.36% | +182 | -205 | -2.30% | 9 | 67 | 2.02 | -1.5% | 3 | ✅ |
| 12 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -2.67% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -2.67% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -2.67% | 0 | – | – | 0.0% | 0 | ✅ |
| 15 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -2.67% | 0 | – | – | 0.0% | 0 | ✅ |
| 16 | **bb_squeeze** | intraday 15m | -0.11% | -55 | -155 | -2.77% | 16 | 44 | 1.04 | -0.6% | 1 | ✅ |
| 17 | **rsi2_scalper** | scalp 15m | -0.42% | -211 | +50 | -3.09% | 30 | 57 | 1.04 | -0.8% | 0 | ✅ |
| 18 | **vwap_reversion** | intraday 15m | -0.46% | -230 | +80 | -3.13% | 27 | 59 | 1.01 | -1.3% | 2 | ✅ |
| 19 | **macd_adx** | intraday 15m | -0.55% | -275 | +108 | -3.22% | 19 | 37 | 0.89 | -1.4% | 1 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -6.76% | -3,379 | +161 | -9.42% | 11 | 18 | 0.06 | -7.4% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
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
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,665.63 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:AXISBANK | 13 | 1,286.66 | 1,201.10 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,300.33 | – | 15 Oct 15:05 |
| hourly_macd_swing | NSE:HDFCBANK | 23 | 720.34 | 710.61 | 738.03 | 15 Oct 10:30 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| gap_and_go | NSE:INFY | 14 | 1,154.88 | 1,122.00 | 1,218.00 | 16 Oct 10:00 |
| gap_and_go | NSE:TCS | 6 | 2,428.99 | 2,375.70 | 2,537.70 | 16 Oct 10:15 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| donchian_turtle | NSE:ICICIBANK | 11 | 1,384.88 | 1,334.46 | – | 15 Oct 15:10 |
| donchian_turtle | NSE:INFY | 14 | 1,109.87 | 1,049.88 | – | 15 Oct 15:10 |
| tv_rating_scalper | NSE:INFY | 14 | 1,154.88 | 1,145.41 | 1,173.12 | 16 Oct 10:00 |
| tv_rating_scalper | NSE:SBIN | 17 | 960.19 | 952.32 | 975.36 | 16 Oct 13:45 |
| supertrend_intraday | NSE:RELIANCE | -14 | 1,198.66 | 1,219.64 | 1,157.72 | 16 Oct 09:45 |
| supertrend_intraday | NSE:SBIN | -17 | 952.31 | 964.32 | 928.86 | 16 Oct 09:45 |
| supertrend_intraday | NSE:KOTAKBANK | -37 | 444.71 | 450.51 | 433.37 | 16 Oct 12:45 |
| vwap_pullback | NSE:SBIN | 17 | 959.89 | 956.65 | 966.10 | 16 Oct 13:30 |
| vwap_pullback | NSE:INFY | 14 | 1,151.93 | 1,146.27 | 1,161.67 | 16 Oct 14:00 |
| ema_crossover | NSE:ITC | -63 | 262.75 | 264.35 | 259.69 | 16 Oct 09:45 |
| orb_breakout | NSE:INFY | 14 | 1,154.88 | 1,122.00 | 1,218.00 | 16 Oct 10:00 |
| orb_breakout | NSE:AXISBANK | -13 | 1,274.65 | 1,293.40 | 1,240.90 | 16 Oct 10:00 |
| orb_breakout | NSE:ITC | -63 | 261.65 | 264.85 | 256.00 | 16 Oct 10:00 |
| bb_squeeze | NSE:ICICIBANK | 11 | 1,390.58 | 1,382.79 | 1,404.43 | 16 Oct 11:45 |
| vwap_reversion | NSE:TCS | -6 | 2,450.01 | 2,469.41 | – | 16 Oct 12:45 |
| vwap_reversion | NSE:HDFCBANK | 22 | 725.95 | 722.72 | – | 16 Oct 14:30 |
| macd_adx | NSE:ITC | 62 | 262.85 | 261.76 | 265.34 | 16 Oct 13:15 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.255042 | 82,042.44 | – | – | 16 Oct 09:00 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.57134 | 2,440.43 | – | – | 16 Oct 09:00 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 16 Oct 14:45 | bb_squeeze | SELL | 14 | NSE:INFY | 1,151.27 | +105 | back to mid band |
| 16 Oct 14:35 | vwap_pullback | SELL | 12 | NSE:AXISBANK | 1,281.84 | -75 | stop-loss |
| 16 Oct 14:30 | vwap_reversion | BUY | 4 | NSE:LT | 3,643.03 | +86 | back to VWAP |
| 16 Oct 14:30 | vwap_reversion | BUY | 22 | NSE:HDFCBANK | 725.95 |  | -2.3 sigma below VWAP |
| 16 Oct 14:30 | hourly_macd_swing | SELL | 13 | NSE:AXISBANK | 1,284.14 | +211 | 1h MACD bear cross |
| 16 Oct 14:30 | ema_crossover | SELL | 4 | NSE:LT | 3,641.57 | -100 | opposite EMA cross |
| 16 Oct 14:30 | ema_crossover | SELL | 12 | NSE:AXISBANK | 1,284.14 | -49 | opposite EMA cross |
| 16 Oct 14:00 | vwap_pullback | BUY | 14 | NSE:INFY | 1,151.93 |  | pullback held VWAP in uptrend |
| 16 Oct 14:00 | rsi2_scalper | SELL | 4 | NSE:LT | 3,655.77 | +2 | RSI2 snapped back (86) |
| 16 Oct 13:45 | vwap_reversion | SELL | 9 | NSE:SUNPHARMA | 1,755.95 | +56 | back to VWAP |
| 16 Oct 13:45 | tv_rating_scalper | BUY | 17 | NSE:SBIN | 960.19 |  | TV 15m +0.51 / 1h +0.25 |
| 16 Oct 13:45 | tv_rating_scalper | BUY | 9 | NSE:SUNPHARMA | 1,756.65 | -44 | 15m rating faded (+0.20) |
| 16 Oct 13:45 | macd_adx | SELL | 6 | NSE:TCS | 2,448.31 | +199 | MACD reversed |
| 16 Oct 13:35 | vwap_pullback | SELL | 13 | NSE:RELIANCE | 1,214.56 | +144 | target |
| 16 Oct 13:30 | vwap_pullback | BUY | 17 | NSE:SBIN | 959.89 |  | pullback held VWAP in uptrend |
| 16 Oct 13:30 | rsi2_scalper | SELL | 36 | NSE:KOTAKBANK | 444.81 | -25 | time stop (1h) |
| 16 Oct 13:30 | rsi2_scalper | SELL | 13 | NSE:RELIANCE | 1,211.96 | +64 | RSI2 snapped back (87) |
| 16 Oct 13:30 | macd_adx | SELL | 17 | NSE:SBIN | 959.36 | -45 | MACD reversed |
| 16 Oct 13:15 | vwap_reversion | BUY | 9 | NSE:SUNPHARMA | 1,748.85 |  | -2.0 sigma below VWAP |
| 16 Oct 13:15 | vwap_pullback | SELL | 22 | NSE:HDFCBANK | 726.25 | -76 | stop-loss |
| 16 Oct 13:15 | rsi2_scalper | BUY | 4 | NSE:LT | 3,653.43 |  | RSI2 8 in uptrend |
| 16 Oct 13:15 | rsi2_scalper | SELL | 22 | NSE:HDFCBANK | 726.25 | -89 | time stop (1h) |
| 16 Oct 13:15 | macd_adx | BUY | 62 | NSE:ITC | 262.85 |  | MACD up, ADX 22 |
| 16 Oct 13:15 | macd_adx | SELL | 11 | NSE:ICICIBANK | 1,391.92 | -57 | MACD reversed |
| 16 Oct 13:15 | bb_squeeze | SELL | 22 | NSE:HDFCBANK | 726.25 | -76 | back to mid band |
| 16 Oct 13:00 | tv_rating_scalper | SELL | 13 | NSE:RELIANCE | 1,205.96 | -91 | 15m rating faded (-0.05) |
| 16 Oct 13:00 | rsi2_scalper | BUY | 13 | NSE:RELIANCE | 1,206.44 |  | RSI2 8 in uptrend |
| 16 Oct 13:00 | macd_adx | BUY | 17 | NSE:SBIN | 961.54 |  | MACD up, ADX 24 |
| 16 Oct 12:55 | hourly_macd_swing | SELL | 12 | NSE:ICICIBANK | 1,397.62 | +393 | target |
| 16 Oct 12:45 | vwap_reversion | SELL | 6 | NSE:TCS | 2,450.01 |  | 2.7 sigma above VWAP |
