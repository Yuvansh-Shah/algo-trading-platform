# 🏆 Bot Leaderboard

_Updated 16 Oct 2026 13:05 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **tv_rating_swing** | swing 1D | +4.49% | +2,243 | +765 | +1.71% | 0 | – | – | -0.4% | 3 | ✅ |
| 🥈 | **momentum_rotation** | positional 1D | +4.47% | +2,234 | +490 | +1.69% | 0 | – | – | -1.3% | 3 | ✅ |
| 🥉 | **hourly_macd_swing** | swing 1h | +3.18% | +1,590 | +51 | +0.40% | 3 | 67 | 9.78 | -0.9% | 2 | ✅ |
| 4 | **nifty_buy_hold** | benchmark 1D | +2.78% | +1,388 | +459 | +0.00% | 0 | – | – | -0.8% | 1 | ✅ |
| 5 | **gap_and_go** | intraday 15m | +1.88% | +942 | +69 | -0.89% | 6 | 83 | 6.87 | -1.0% | 2 | ✅ |
| 6 | **donchian_turtle** | swing 1D | +1.86% | +932 | +393 | -0.91% | 0 | – | – | -0.5% | 3 | ✅ |
| 7 | **tv_rating_scalper** | intraday 15m | +1.18% | +592 | -392 | -1.59% | 25 | 48 | 1.55 | -1.2% | 2 | ✅ |
| 8 | **vwap_pullback** | intraday 15m | +0.99% | +497 | +390 | -1.78% | 28 | 50 | 1.59 | -1.7% | 3 | ✅ |
| 9 | **ema_crossover** | intraday 15m | +0.89% | +443 | -416 | -1.89% | 18 | 50 | 1.85 | -1.1% | 3 | ✅ |
| 10 | **supertrend_intraday** | intraday 15m | +0.87% | +434 | -565 | -1.91% | 10 | 60 | 2.77 | -1.3% | 3 | ✅ |
| 11 | **bb_squeeze** | intraday 15m | +0.16% | +80 | -20 | -2.62% | 14 | 43 | 1.00 | -0.6% | 3 | ✅ |
| 12 | **orb_breakout** | intraday 15m | +0.10% | +52 | -335 | -2.67% | 9 | 67 | 2.02 | -1.4% | 3 | ✅ |
| 13 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -2.78% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -2.78% | 0 | – | – | 0.0% | 0 | ✅ |
| 15 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -2.78% | 0 | – | – | 0.0% | 0 | ✅ |
| 16 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -2.78% | 0 | – | – | 0.0% | 0 | ✅ |
| 17 | **macd_adx** | intraday 15m | -0.24% | -122 | +262 | -3.02% | 16 | 38 | 0.76 | -1.4% | 3 | ✅ |
| 18 | **rsi2_scalper** | scalp 15m | -0.31% | -156 | +105 | -3.09% | 26 | 58 | 1.12 | -0.8% | 3 | ✅ |
| 19 | **vwap_reversion** | intraday 15m | -0.56% | -282 | +28 | -3.34% | 25 | 56 | 0.87 | -1.3% | 2 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -6.81% | -3,407 | +133 | -9.59% | 11 | 18 | 0.06 | -7.4% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,665.63 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:AXISBANK | 13 | 1,286.66 | 1,201.10 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,300.33 | – | 15 Oct 15:05 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| hourly_macd_swing | NSE:AXISBANK | 13 | 1,267.25 | 1,254.59 | 1,315.81 | 15 Oct 09:25 |
| hourly_macd_swing | NSE:HDFCBANK | 23 | 720.34 | 710.61 | 738.03 | 15 Oct 10:30 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| gap_and_go | NSE:INFY | 14 | 1,154.88 | 1,122.00 | 1,218.00 | 16 Oct 10:00 |
| gap_and_go | NSE:TCS | 6 | 2,428.99 | 2,375.70 | 2,537.70 | 16 Oct 10:15 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| donchian_turtle | NSE:ICICIBANK | 11 | 1,384.88 | 1,334.46 | – | 15 Oct 15:10 |
| donchian_turtle | NSE:INFY | 14 | 1,109.87 | 1,049.88 | – | 15 Oct 15:10 |
| tv_rating_scalper | NSE:INFY | 14 | 1,154.88 | 1,145.41 | 1,173.12 | 16 Oct 10:00 |
| tv_rating_scalper | NSE:SUNPHARMA | -9 | 1,752.65 | 1,767.02 | 1,724.95 | 16 Oct 12:30 |
| vwap_pullback | NSE:HDFCBANK | 22 | 729.35 | 726.96 | 734.58 | 16 Oct 09:45 |
| vwap_pullback | NSE:RELIANCE | 13 | 1,202.84 | 1,197.21 | 1,214.59 | 16 Oct 10:15 |
| vwap_pullback | NSE:AXISBANK | 12 | 1,287.46 | 1,282.20 | 1,296.60 | 16 Oct 12:45 |
| ema_crossover | NSE:ITC | -63 | 262.75 | 264.35 | 259.69 | 16 Oct 09:45 |
| ema_crossover | NSE:AXISBANK | 12 | 1,287.56 | 1,279.26 | 1,303.98 | 16 Oct 10:45 |
| ema_crossover | NSE:LT | 4 | 3,664.63 | 3,637.93 | 3,699.93 | 16 Oct 11:45 |
| supertrend_intraday | NSE:RELIANCE | -14 | 1,198.66 | 1,219.64 | 1,157.72 | 16 Oct 09:45 |
| supertrend_intraday | NSE:SBIN | -17 | 952.31 | 964.32 | 928.86 | 16 Oct 09:45 |
| supertrend_intraday | NSE:KOTAKBANK | -37 | 444.71 | 450.51 | 433.37 | 16 Oct 12:45 |
| bb_squeeze | NSE:HDFCBANK | 22 | 729.35 | 725.69 | 737.13 | 16 Oct 09:45 |
| bb_squeeze | NSE:INFY | 14 | 1,143.23 | 1,132.12 | 1,162.05 | 16 Oct 09:45 |
| bb_squeeze | NSE:ICICIBANK | 11 | 1,390.58 | 1,382.79 | 1,404.43 | 16 Oct 11:45 |
| orb_breakout | NSE:INFY | 14 | 1,154.88 | 1,122.00 | 1,218.00 | 16 Oct 10:00 |
| orb_breakout | NSE:AXISBANK | -13 | 1,274.65 | 1,293.40 | 1,240.90 | 16 Oct 10:00 |
| orb_breakout | NSE:ITC | -63 | 261.65 | 264.85 | 256.00 | 16 Oct 10:00 |
| macd_adx | NSE:TCS | 6 | 2,413.98 | 2,395.98 | 2,454.23 | 16 Oct 09:45 |
| macd_adx | NSE:ICICIBANK | 11 | 1,396.38 | 1,389.25 | 1,409.79 | 16 Oct 12:45 |
| macd_adx | NSE:SBIN | 17 | 961.54 | 956.24 | 971.27 | 16 Oct 13:00 |
| rsi2_scalper | NSE:HDFCBANK | 22 | 729.95 | 723.96 | – | 16 Oct 12:15 |
| rsi2_scalper | NSE:KOTAKBANK | 36 | 445.29 | 441.64 | – | 16 Oct 12:30 |
| rsi2_scalper | NSE:RELIANCE | 13 | 1,206.44 | 1,196.55 | – | 16 Oct 13:00 |
| vwap_reversion | NSE:LT | -4 | 3,666.27 | 3,688.51 | – | 16 Oct 12:00 |
| vwap_reversion | NSE:TCS | -6 | 2,450.01 | 2,469.41 | – | 16 Oct 12:45 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.255042 | 82,042.44 | – | – | 16 Oct 09:00 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.57134 | 2,440.43 | – | – | 16 Oct 09:00 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 16 Oct 13:00 | tv_rating_scalper | SELL | 13 | NSE:RELIANCE | 1,205.96 | -91 | 15m rating faded (-0.05) |
| 16 Oct 13:00 | rsi2_scalper | BUY | 13 | NSE:RELIANCE | 1,206.44 |  | RSI2 8 in uptrend |
| 16 Oct 13:00 | macd_adx | BUY | 17 | NSE:SBIN | 961.54 |  | MACD up, ADX 24 |
| 16 Oct 12:55 | hourly_macd_swing | SELL | 12 | NSE:ICICIBANK | 1,397.62 | +393 | target |
| 16 Oct 12:45 | vwap_reversion | SELL | 6 | NSE:TCS | 2,450.01 |  | 2.7 sigma above VWAP |
| 16 Oct 12:45 | vwap_pullback | BUY | 12 | NSE:AXISBANK | 1,287.46 |  | pullback held VWAP in uptrend |
| 16 Oct 12:45 | supertrend_intraday | SELL | 37 | NSE:KOTAKBANK | 444.71 |  | Supertrend flipped down |
| 16 Oct 12:45 | macd_adx | SELL | 14 | NSE:INFY | 1,151.57 | +109 | MACD reversed |
| 16 Oct 12:45 | macd_adx | BUY | 11 | NSE:ICICIBANK | 1,396.38 |  | MACD up, ADX 51 |
| 16 Oct 12:35 | vwap_reversion | BUY | 6 | NSE:TCS | 2,444.39 | -118 | stop-loss |
| 16 Oct 12:35 | vwap_pullback | SELL | 6 | NSE:TCS | 2,443.41 | +169 | target |
| 16 Oct 12:30 | tv_rating_scalper | SELL | 9 | NSE:SUNPHARMA | 1,752.65 |  | TV 15m -0.56 / 1h -0.45 |
| 16 Oct 12:30 | tv_rating_scalper | SELL | 37 | NSE:KOTAKBANK | 445.11 | -67 | 15m rating faded (-0.05) |
| 16 Oct 12:30 | rsi2_scalper | BUY | 36 | NSE:KOTAKBANK | 445.29 |  | RSI2 10 in uptrend |
| 16 Oct 12:15 | vwap_reversion | BUY | 14 | NSE:INFY | 1,149.38 | +62 | back to VWAP |
| 16 Oct 12:15 | rsi2_scalper | BUY | 22 | NSE:HDFCBANK | 729.95 |  | RSI2 4 in uptrend |
| 16 Oct 12:00 | vwap_reversion | SELL | 4 | NSE:LT | 3,666.27 |  | 2.3 sigma above VWAP |
| 16 Oct 12:00 | supertrend_intraday | BUY | 4 | NSE:LT | 3,667.73 | -223 | Supertrend reversed |
| 16 Oct 11:45 | macd_adx | SELL | 22 | NSE:HDFCBANK | 730.35 | -31 | MACD reversed |
| 16 Oct 11:45 | ema_crossover | BUY | 4 | NSE:LT | 3,664.63 |  | EMA9>21, RSI 55 |
| 16 Oct 11:45 | bb_squeeze | BUY | 11 | NSE:ICICIBANK | 1,390.58 |  | squeeze breakout up |
| 16 Oct 11:00 | vwap_reversion | BUY | 36 | NSE:KOTAKBANK | 449.09 | +65 | back to VWAP |
| 16 Oct 10:45 | tv_rating_scalper | BUY | 13 | NSE:RELIANCE | 1,212.34 |  | TV 15m +0.51 / 1h +0.42 |
| 16 Oct 10:45 | tv_rating_scalper | BUY | 4 | NSE:LT | 3,654.13 | -47 | 15m rating faded (+0.11) |
| 16 Oct 10:45 | ema_crossover | BUY | 12 | NSE:AXISBANK | 1,287.56 |  | EMA9>21, RSI 56 |
| 16 Oct 10:45 | ema_crossover | BUY | 13 | NSE:AXISBANK | 1,287.56 | -129 | stop-loss |
| 16 Oct 10:45 | bb_squeeze | BUY | 4 | NSE:LT | 3,654.13 | -47 | back to mid band |
| 16 Oct 10:35 | ema_crossover | BUY | 9 | NSE:SUNPHARMA | 1,761.95 | -128 | stop-loss |
| 16 Oct 10:30 | vwap_reversion | SELL | 36 | NSE:KOTAKBANK | 451.11 |  | 3.3 sigma above VWAP |
| 16 Oct 10:30 | rsi2_scalper | SELL | 12 | NSE:AXISBANK | 1,285.64 | +57 | RSI2 snapped back (79) |
