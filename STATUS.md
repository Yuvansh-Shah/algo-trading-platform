# 🏆 Bot Leaderboard

_Updated 16 Oct 2026 11:10 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **momentum_rotation** | positional 1D | +4.32% | +2,159 | +415 | +1.80% | 0 | – | – | -1.3% | 3 | ✅ |
| 🥈 | **tv_rating_swing** | swing 1D | +3.66% | +1,828 | +350 | +1.13% | 0 | – | – | -0.4% | 3 | ✅ |
| 🥉 | **hourly_macd_swing** | swing 1h | +2.93% | +1,463 | -76 | +0.40% | 2 | 50 | 6.74 | -0.9% | 3 | ✅ |
| 4 | **nifty_buy_hold** | benchmark 1D | +2.52% | +1,262 | +332 | +0.00% | 0 | – | – | -0.8% | 1 | ✅ |
| 5 | **gap_and_go** | intraday 15m | +1.64% | +818 | -55 | -0.89% | 6 | 83 | 6.87 | -0.9% | 2 | ✅ |
| 6 | **donchian_turtle** | swing 1D | +1.49% | +744 | +205 | -1.03% | 0 | – | – | -0.5% | 3 | ✅ |
| 7 | **tv_rating_scalper** | intraday 15m | +1.42% | +708 | -276 | -1.11% | 23 | 52 | 1.74 | -0.9% | 3 | ✅ |
| 8 | **supertrend_intraday** | intraday 15m | +1.18% | +592 | -406 | -1.34% | 9 | 67 | 5.19 | -1.2% | 3 | ✅ |
| 9 | **ema_crossover** | intraday 15m | +1.04% | +518 | -342 | -1.49% | 18 | 50 | 1.85 | -1.0% | 2 | ✅ |
| 10 | **vwap_pullback** | intraday 15m | +0.89% | +444 | +336 | -1.63% | 27 | 48 | 1.43 | -1.7% | 3 | ✅ |
| 11 | **orb_breakout** | intraday 15m | +0.25% | +127 | -260 | -2.27% | 9 | 67 | 2.02 | -1.3% | 3 | ✅ |
| 12 | **bb_squeeze** | intraday 15m | +0.07% | +34 | -66 | -2.45% | 14 | 43 | 1.00 | -0.6% | 2 | ✅ |
| 13 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -2.52% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -2.52% | 0 | – | – | 0.0% | 0 | ✅ |
| 15 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -2.52% | 0 | – | – | 0.0% | 0 | ✅ |
| 16 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -2.52% | 0 | – | – | 0.0% | 0 | ✅ |
| 17 | **rsi2_scalper** | scalp 15m | -0.26% | -131 | +130 | -2.79% | 26 | 58 | 1.12 | -0.8% | 0 | ✅ |
| 18 | **macd_adx** | intraday 15m | -0.41% | -203 | +181 | -2.93% | 14 | 36 | 0.65 | -1.4% | 3 | ✅ |
| 19 | **vwap_reversion** | intraday 15m | -0.51% | -254 | +56 | -3.03% | 23 | 57 | 0.92 | -1.3% | 2 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -6.89% | -3,445 | +95 | -9.41% | 11 | 18 | 0.06 | -7.4% | 2 | ✅ |

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
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,647.87 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:AXISBANK | 13 | 1,286.66 | 1,200.54 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,297.35 | – | 15 Oct 15:05 |
| hourly_macd_swing | NSE:AXISBANK | 13 | 1,267.25 | 1,254.59 | 1,315.81 | 15 Oct 09:25 |
| hourly_macd_swing | NSE:HDFCBANK | 23 | 720.34 | 710.61 | 738.03 | 15 Oct 10:30 |
| hourly_macd_swing | NSE:ICICIBANK | 12 | 1,364.17 | 1,347.36 | 1,397.28 | 15 Oct 11:30 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| gap_and_go | NSE:INFY | 14 | 1,154.88 | 1,122.00 | 1,218.00 | 16 Oct 10:00 |
| gap_and_go | NSE:TCS | 6 | 2,428.99 | 2,375.70 | 2,537.70 | 16 Oct 10:15 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| donchian_turtle | NSE:ICICIBANK | 11 | 1,384.88 | 1,334.46 | – | 15 Oct 15:10 |
| donchian_turtle | NSE:INFY | 14 | 1,109.87 | 1,049.88 | – | 15 Oct 15:10 |
| tv_rating_scalper | NSE:KOTAKBANK | 37 | 446.69 | 443.03 | 453.75 | 16 Oct 09:30 |
| tv_rating_scalper | NSE:INFY | 14 | 1,154.88 | 1,145.41 | 1,173.12 | 16 Oct 10:00 |
| tv_rating_scalper | NSE:RELIANCE | 13 | 1,212.34 | 1,202.40 | 1,231.49 | 16 Oct 10:45 |
| supertrend_intraday | NSE:RELIANCE | -14 | 1,198.66 | 1,219.64 | 1,157.72 | 16 Oct 09:45 |
| supertrend_intraday | NSE:SBIN | -17 | 952.31 | 964.32 | 928.86 | 16 Oct 09:45 |
| supertrend_intraday | NSE:LT | -4 | 3,613.78 | 3,673.58 | 3,492.75 | 16 Oct 09:45 |
| ema_crossover | NSE:ITC | -63 | 262.75 | 264.35 | 259.69 | 16 Oct 09:45 |
| ema_crossover | NSE:AXISBANK | 12 | 1,287.56 | 1,279.26 | 1,303.98 | 16 Oct 10:45 |
| vwap_pullback | NSE:HDFCBANK | 22 | 729.35 | 726.96 | 734.58 | 16 Oct 09:45 |
| vwap_pullback | NSE:TCS | 6 | 2,413.98 | 2,402.46 | 2,441.29 | 16 Oct 09:45 |
| vwap_pullback | NSE:RELIANCE | 13 | 1,202.84 | 1,197.21 | 1,214.59 | 16 Oct 10:15 |
| orb_breakout | NSE:INFY | 14 | 1,154.88 | 1,122.00 | 1,218.00 | 16 Oct 10:00 |
| orb_breakout | NSE:AXISBANK | -13 | 1,274.65 | 1,293.40 | 1,240.90 | 16 Oct 10:00 |
| orb_breakout | NSE:ITC | -63 | 261.65 | 264.85 | 256.00 | 16 Oct 10:00 |
| bb_squeeze | NSE:HDFCBANK | 22 | 729.35 | 725.69 | 737.13 | 16 Oct 09:45 |
| bb_squeeze | NSE:INFY | 14 | 1,143.23 | 1,132.12 | 1,162.05 | 16 Oct 09:45 |
| macd_adx | NSE:INFY | 14 | 1,143.23 | 1,132.12 | 1,162.05 | 16 Oct 09:45 |
| macd_adx | NSE:TCS | 6 | 2,413.98 | 2,395.98 | 2,454.23 | 16 Oct 09:45 |
| macd_adx | NSE:HDFCBANK | 22 | 731.40 | 727.01 | 738.98 | 16 Oct 10:15 |
| vwap_reversion | NSE:INFY | -14 | 1,154.42 | 1,164.72 | – | 16 Oct 10:00 |
| vwap_reversion | NSE:TCS | -6 | 2,425.91 | 2,443.05 | – | 16 Oct 10:00 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.255042 | 82,042.44 | – | – | 16 Oct 09:00 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.57134 | 2,440.43 | – | – | 16 Oct 09:00 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 16 Oct 11:00 | vwap_reversion | BUY | 36 | NSE:KOTAKBANK | 449.09 | +65 | back to VWAP |
| 16 Oct 10:45 | tv_rating_scalper | BUY | 13 | NSE:RELIANCE | 1,212.34 |  | TV 15m +0.51 / 1h +0.42 |
| 16 Oct 10:45 | tv_rating_scalper | BUY | 4 | NSE:LT | 3,654.13 | -47 | 15m rating faded (+0.11) |
| 16 Oct 10:45 | ema_crossover | BUY | 12 | NSE:AXISBANK | 1,287.56 |  | EMA9>21, RSI 56 |
| 16 Oct 10:45 | ema_crossover | BUY | 13 | NSE:AXISBANK | 1,287.56 | -129 | stop-loss |
| 16 Oct 10:45 | bb_squeeze | BUY | 4 | NSE:LT | 3,654.13 | -47 | back to mid band |
| 16 Oct 10:35 | ema_crossover | BUY | 9 | NSE:SUNPHARMA | 1,761.95 | -128 | stop-loss |
| 16 Oct 10:30 | vwap_reversion | SELL | 36 | NSE:KOTAKBANK | 451.11 |  | 3.3 sigma above VWAP |
| 16 Oct 10:30 | rsi2_scalper | SELL | 12 | NSE:AXISBANK | 1,285.64 | +57 | RSI2 snapped back (79) |
| 16 Oct 10:30 | rsi2_scalper | SELL | 13 | NSE:RELIANCE | 1,206.16 | +89 | RSI2 snapped back (83) |
| 16 Oct 10:15 | vwap_pullback | BUY | 13 | NSE:RELIANCE | 1,202.84 |  | pullback held VWAP in uptrend |
| 16 Oct 10:15 | macd_adx | BUY | 22 | NSE:HDFCBANK | 731.40 |  | MACD up, ADX 41 |
| 16 Oct 10:15 | gap_and_go | BUY | 6 | NSE:TCS | 2,428.99 |  | gap up +1.0% and go |
| 16 Oct 10:15 | ema_crossover | SELL | 13 | NSE:AXISBANK | 1,278.24 |  | EMA9<21, RSI 44 |
| 16 Oct 10:15 | ema_crossover | BUY | 4 | NSE:LT | 3,635.53 | -94 | stop-loss |
| 16 Oct 10:05 | vwap_pullback | SELL | 14 | NSE:INFY | 1,155.37 | +162 | target |
| 16 Oct 10:00 | vwap_reversion | SELL | 6 | NSE:TCS | 2,425.91 |  | 2.3 sigma above VWAP |
| 16 Oct 10:00 | vwap_reversion | SELL | 14 | NSE:INFY | 1,154.42 |  | 3.2 sigma above VWAP |
| 16 Oct 10:00 | tv_rating_scalper | BUY | 14 | NSE:INFY | 1,154.88 |  | TV 15m +0.60 / 1h +0.69 |
| 16 Oct 10:00 | orb_breakout | SELL | 63 | NSE:ITC | 261.65 |  | ORB down < 262.4 |
| 16 Oct 10:00 | orb_breakout | SELL | 13 | NSE:AXISBANK | 1,274.64 |  | ORB down < 1279.4 |
| 16 Oct 10:00 | orb_breakout | BUY | 14 | NSE:INFY | 1,154.88 |  | ORB up > 1145.0 |
| 16 Oct 10:00 | gap_and_go | BUY | 14 | NSE:INFY | 1,154.88 |  | gap up +1.9% and go |
| 16 Oct 10:00 | ema_crossover | SELL | 9 | NSE:SUNPHARMA | 1,748.65 |  | EMA9<21, RSI 39 |
| 16 Oct 09:50 | tv_rating_scalper | SELL | 12 | NSE:ICICIBANK | 1,381.32 | -158 | stop-loss |
| 16 Oct 09:45 | vwap_pullback | BUY | 6 | NSE:TCS | 2,413.98 |  | pullback held VWAP in uptrend |
| 16 Oct 09:45 | vwap_pullback | BUY | 14 | NSE:INFY | 1,143.23 |  | pullback held VWAP in uptrend |
| 16 Oct 09:45 | vwap_pullback | BUY | 22 | NSE:HDFCBANK | 729.35 |  | pullback held VWAP in uptrend |
| 16 Oct 09:45 | supertrend_intraday | SELL | 4 | NSE:LT | 3,613.78 |  | Supertrend flipped down |
| 16 Oct 09:45 | supertrend_intraday | SELL | 17 | NSE:SBIN | 952.31 |  | Supertrend flipped down |
