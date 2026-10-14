# 🏆 Bot Leaderboard

_Updated 14 Oct 2026 10:35 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **gap_and_go** | intraday 15m | +1.98% | +989 | +513 | +1.21% | 2 | 100 | ∞ | -0.5% | 2 | ✅ |
| 🥈 | **tv_rating_scalper** | intraday 15m | +1.96% | +982 | +293 | +1.20% | 8 | 75 | 6.33 | -0.5% | 3 | ✅ |
| 🥉 | **momentum_rotation** | positional 1D | +1.68% | +841 | +692 | +0.91% | 0 | – | – | -0.8% | 3 | ✅ |
| 4 | **hourly_macd_swing** | swing 1h | +1.15% | +575 | +349 | +0.38% | 0 | – | – | -0.5% | 2 | ✅ |
| 5 | **ema_crossover** | intraday 15m | +0.83% | +413 | +71 | +0.06% | 5 | 60 | 3.53 | -0.4% | 2 | ✅ |
| 6 | **supertrend_intraday** | intraday 15m | +0.81% | +405 | -84 | +0.04% | 3 | 67 | 31.05 | -0.4% | 3 | ✅ |
| 7 | **nifty_buy_hold** | benchmark 1D | +0.77% | +384 | -102 | +0.00% | 0 | – | – | -0.3% | 1 | ✅ |
| 8 | **orb_breakout** | intraday 15m | +0.69% | +343 | -106 | -0.08% | 3 | 100 | ∞ | -0.6% | 3 | ✅ |
| 9 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -0.77% | 0 | – | – | 0.0% | 0 | ✅ |
| 10 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -0.77% | 0 | – | – | 0.0% | 0 | ✅ |
| 11 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -0.77% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -0.77% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **tv_rating_swing** | swing 1D | +0.00% | +0 | +0 | -0.77% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **donchian_turtle** | swing 1D | -0.11% | -56 | +46 | -0.88% | 0 | – | – | -0.3% | 1 | ✅ |
| 15 | **rsi2_scalper** | scalp 15m | -0.18% | -92 | +55 | -0.95% | 8 | 50 | 1.06 | -0.4% | 1 | ✅ |
| 16 | **bb_squeeze** | intraday 15m | -0.26% | -128 | -159 | -1.02% | 5 | 40 | 0.69 | -0.5% | 2 | ✅ |
| 17 | **macd_adx** | intraday 15m | -0.35% | -173 | -52 | -1.11% | 4 | 25 | 0.63 | -0.8% | 1 | ✅ |
| 18 | **vwap_reversion** | intraday 15m | -0.41% | -204 | +0 | -1.18% | 7 | 57 | 0.50 | -0.6% | 0 | ✅ |
| 19 | **vwap_pullback** | intraday 15m | -0.48% | -238 | -124 | -1.24% | 10 | 20 | 0.59 | -1.1% | 3 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -3.04% | -1,520 | -59 | -3.81% | 9 | 22 | 0.12 | -3.6% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| gap_and_go | NSE:INFY | 15 | 1,073.91 | 1,027.00 | 1,129.30 | 14 Oct 09:25 |
| gap_and_go | NSE:TCS | 7 | 2,274.45 | 2,155.00 | 2,482.00 | 14 Oct 09:25 |
| tv_rating_scalper | NSE:HDFCBANK | 23 | 712.44 | 706.60 | 723.70 | 14 Oct 09:25 |
| tv_rating_scalper | NSE:SBIN | 17 | 955.59 | 947.76 | 970.69 | 14 Oct 09:25 |
| tv_rating_scalper | NSE:TCS | 7 | 2,323.06 | 2,304.02 | 2,359.76 | 14 Oct 09:45 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| hourly_macd_swing | NSE:TCS | 7 | 2,242.15 | 2,182.70 | 2,362.39 | 13 Oct 10:30 |
| hourly_macd_swing | NSE:AXISBANK | 13 | 1,263.65 | 1,245.45 | 1,299.89 | 13 Oct 14:30 |
| ema_crossover | NSE:KOTAKBANK | 37 | 443.14 | 440.58 | 447.99 | 14 Oct 10:00 |
| ema_crossover | NSE:SUNPHARMA | -9 | 1,754.65 | 1,762.69 | 1,736.62 | 14 Oct 10:00 |
| supertrend_intraday | NSE:AXISBANK | -13 | 1,259.65 | 1,278.69 | 1,222.62 | 14 Oct 09:45 |
| supertrend_intraday | NSE:KOTAKBANK | 37 | 442.94 | 435.91 | 456.89 | 14 Oct 09:45 |
| supertrend_intraday | NSE:ICICIBANK | -12 | 1,351.23 | 1,365.86 | 1,322.79 | 14 Oct 10:15 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| orb_breakout | NSE:RELIANCE | 14 | 1,171.83 | 1,162.70 | 1,186.70 | 14 Oct 10:00 |
| orb_breakout | NSE:HDFCBANK | 23 | 717.74 | 711.35 | 730.70 | 14 Oct 10:00 |
| orb_breakout | NSE:INFY | 15 | 1,087.62 | 1,069.45 | 1,122.55 | 14 Oct 10:30 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| rsi2_scalper | NSE:ICICIBANK | 12 | 1,351.77 | 1,340.69 | – | 14 Oct 10:15 |
| bb_squeeze | NSE:ITC | 63 | 261.05 | 260.10 | 263.56 | 14 Oct 09:25 |
| bb_squeeze | NSE:SUNPHARMA | -9 | 1,752.55 | 1,761.08 | 1,736.85 | 14 Oct 09:45 |
| macd_adx | NSE:TCS | 7 | 2,323.06 | 2,298.25 | 2,363.51 | 14 Oct 09:45 |
| vwap_pullback | NSE:INFY | 15 | 1,080.82 | 1,074.07 | 1,093.36 | 14 Oct 09:45 |
| vwap_pullback | NSE:LT | -4 | 3,646.67 | 3,661.21 | 3,619.48 | 14 Oct 09:45 |
| vwap_pullback | NSE:TCS | 7 | 2,317.36 | 2,300.50 | 2,347.31 | 14 Oct 10:15 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.261364 | 83,345.55 | – | – | 13 Oct 09:30 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.68092 | 2,508.57 | – | – | 13 Oct 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 14 Oct 10:30 | rsi2_scalper | SELL | 13 | NSE:AXISBANK | 1,268.55 | +101 | RSI2 snapped back (79) |
| 14 Oct 10:30 | orb_breakout | BUY | 15 | NSE:INFY | 1,087.62 |  | ORB up > 1085.5 |
| 14 Oct 10:15 | vwap_pullback | BUY | 7 | NSE:TCS | 2,317.36 |  | pullback held VWAP in uptrend |
| 14 Oct 10:15 | vwap_pullback | SELL | 22 | NSE:HDFCBANK | 715.11 | -66 | stop-loss |
| 14 Oct 10:15 | supertrend_intraday | SELL | 12 | NSE:ICICIBANK | 1,351.23 |  | Supertrend flipped down |
| 14 Oct 10:15 | rsi2_scalper | BUY | 12 | NSE:ICICIBANK | 1,351.77 |  | RSI2 6 in uptrend |
| 14 Oct 10:00 | vwap_pullback | BUY | 22 | NSE:HDFCBANK | 717.74 |  | pullback held VWAP in uptrend |
| 14 Oct 10:00 | orb_breakout | BUY | 23 | NSE:HDFCBANK | 717.74 |  | ORB up > 715.9 |
| 14 Oct 10:00 | orb_breakout | BUY | 14 | NSE:RELIANCE | 1,171.83 |  | ORB up > 1169.7 |
| 14 Oct 10:00 | ema_crossover | SELL | 9 | NSE:SUNPHARMA | 1,754.65 |  | EMA9<21, RSI 42 |
| 14 Oct 10:00 | ema_crossover | BUY | 37 | NSE:KOTAKBANK | 443.14 |  | EMA9>21, RSI 64 |
| 14 Oct 09:50 | vwap_pullback | SELL | 7 | NSE:TCS | 2,301.94 | -156 | stop-loss |
| 14 Oct 09:45 | vwap_pullback | SELL | 4 | NSE:LT | 3,646.67 |  | rally rejected at VWAP in downtrend |
| 14 Oct 09:45 | vwap_pullback | BUY | 7 | NSE:TCS | 2,323.06 |  | pullback held VWAP in uptrend |
| 14 Oct 09:45 | vwap_pullback | BUY | 15 | NSE:INFY | 1,080.82 |  | pullback held VWAP in uptrend |
| 14 Oct 09:45 | tv_rating_scalper | BUY | 7 | NSE:TCS | 2,323.06 |  | TV 15m +0.60 / 1h +0.56 |
| 14 Oct 09:45 | supertrend_intraday | BUY | 37 | NSE:KOTAKBANK | 442.94 |  | Supertrend flipped up |
| 14 Oct 09:45 | supertrend_intraday | SELL | 13 | NSE:AXISBANK | 1,259.65 |  | Supertrend flipped down |
| 14 Oct 09:45 | rsi2_scalper | BUY | 13 | NSE:AXISBANK | 1,260.15 |  | RSI2 10 in uptrend |
| 14 Oct 09:45 | macd_adx | BUY | 7 | NSE:TCS | 2,323.06 |  | MACD up, ADX 49 |
| 14 Oct 09:45 | bb_squeeze | SELL | 9 | NSE:SUNPHARMA | 1,752.55 |  | squeeze breakout down |
| 14 Oct 09:35 | tv_rating_scalper | SELL | 7 | NSE:TCS | 2,332.23 | +396 | target |
| 14 Oct 09:35 | bb_squeeze | SELL | 9 | NSE:SUNPHARMA | 1,754.75 | -19 | stop-loss |
| 14 Oct 09:30 | bb_squeeze | BUY | 9 | NSE:SUNPHARMA | 1,755.95 |  | squeeze breakout up |
| 14 Oct 09:30 | bb_squeeze | SELL | 9 | NSE:SUNPHARMA | 1,755.25 | -145 | stop-loss |
| 14 Oct 09:25 | tv_rating_scalper | BUY | 17 | NSE:SBIN | 955.59 |  | TV 15m +0.56 / 1h +0.34 |
| 14 Oct 09:25 | tv_rating_scalper | BUY | 7 | NSE:TCS | 2,274.45 |  | TV 15m +0.56 / 1h +0.49 |
| 14 Oct 09:25 | tv_rating_scalper | BUY | 23 | NSE:HDFCBANK | 712.44 |  | TV 15m +0.56 / 1h +0.47 |
| 14 Oct 09:25 | gap_and_go | BUY | 7 | NSE:TCS | 2,274.45 |  | gap up +1.8% and go |
| 14 Oct 09:25 | gap_and_go | BUY | 15 | NSE:INFY | 1,073.91 |  | gap up +1.2% and go |
