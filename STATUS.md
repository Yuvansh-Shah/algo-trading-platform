# 🏆 Bot Leaderboard

_Updated 14 Oct 2026 12:20 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **gap_and_go** | intraday 15m | +1.85% | +926 | +451 | +0.98% | 2 | 100 | ∞ | -0.5% | 2 | ✅ |
| 🥈 | **tv_rating_scalper** | intraday 15m | +1.69% | +843 | +153 | +0.81% | 10 | 60 | 2.63 | -0.9% | 3 | ✅ |
| 🥉 | **momentum_rotation** | positional 1D | +1.49% | +744 | +595 | +0.61% | 0 | – | – | -0.8% | 3 | ✅ |
| 4 | **supertrend_intraday** | intraday 15m | +1.01% | +507 | +18 | +0.14% | 3 | 67 | 31.05 | -0.5% | 3 | ✅ |
| 5 | **orb_breakout** | intraday 15m | +0.89% | +446 | -3 | +0.02% | 3 | 100 | ∞ | -0.6% | 3 | ✅ |
| 6 | **nifty_buy_hold** | benchmark 1D | +0.88% | +438 | -48 | +0.00% | 0 | – | – | -0.3% | 1 | ✅ |
| 7 | **hourly_macd_swing** | swing 1h | +0.79% | +394 | +168 | -0.09% | 0 | – | – | -0.6% | 2 | ✅ |
| 8 | **ema_crossover** | intraday 15m | +0.78% | +392 | +50 | -0.09% | 5 | 60 | 3.53 | -0.4% | 3 | ✅ |
| 9 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -0.88% | 0 | – | – | 0.0% | 0 | ✅ |
| 10 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -0.88% | 0 | – | – | 0.0% | 0 | ✅ |
| 11 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -0.88% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -0.88% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **tv_rating_swing** | swing 1D | +0.00% | +0 | +0 | -0.88% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **rsi2_scalper** | scalp 15m | -0.19% | -94 | +53 | -1.06% | 11 | 45 | 1.06 | -0.4% | 1 | ✅ |
| 15 | **bb_squeeze** | intraday 15m | -0.32% | -160 | -191 | -1.20% | 6 | 33 | 0.54 | -0.6% | 1 | ✅ |
| 16 | **donchian_turtle** | swing 1D | -0.34% | -171 | -70 | -1.22% | 0 | – | – | -0.4% | 1 | ✅ |
| 17 | **vwap_reversion** | intraday 15m | -0.61% | -304 | -100 | -1.48% | 7 | 57 | 0.50 | -0.8% | 2 | ✅ |
| 18 | **macd_adx** | intraday 15m | -0.77% | -386 | -265 | -1.65% | 6 | 17 | 0.31 | -1.0% | 0 | ✅ |
| 19 | **vwap_pullback** | intraday 15m | -0.89% | -445 | -331 | -1.77% | 11 | 18 | 0.50 | -1.3% | 3 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -3.27% | -1,634 | -173 | -4.14% | 9 | 22 | 0.12 | -3.6% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| gap_and_go | NSE:INFY | 15 | 1,073.91 | 1,027.00 | 1,129.30 | 14 Oct 09:25 |
| gap_and_go | NSE:TCS | 7 | 2,274.45 | 2,155.00 | 2,482.00 | 14 Oct 09:25 |
| tv_rating_scalper | NSE:HDFCBANK | 23 | 712.44 | 706.60 | 723.70 | 14 Oct 09:25 |
| tv_rating_scalper | NSE:BHARTIARTL | 9 | 1,815.86 | 1,800.98 | 1,844.55 | 14 Oct 11:15 |
| tv_rating_scalper | NSE:SUNPHARMA | -9 | 1,749.85 | 1,764.20 | 1,722.20 | 14 Oct 11:45 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| supertrend_intraday | NSE:AXISBANK | -13 | 1,259.65 | 1,278.69 | 1,222.62 | 14 Oct 09:45 |
| supertrend_intraday | NSE:KOTAKBANK | 37 | 442.94 | 435.91 | 456.89 | 14 Oct 09:45 |
| supertrend_intraday | NSE:ICICIBANK | -12 | 1,351.23 | 1,365.86 | 1,322.79 | 14 Oct 10:15 |
| orb_breakout | NSE:RELIANCE | 14 | 1,171.83 | 1,162.70 | 1,186.70 | 14 Oct 10:00 |
| orb_breakout | NSE:HDFCBANK | 23 | 717.74 | 711.35 | 730.70 | 14 Oct 10:00 |
| orb_breakout | NSE:INFY | 15 | 1,087.62 | 1,069.45 | 1,122.55 | 14 Oct 10:30 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| hourly_macd_swing | NSE:TCS | 7 | 2,242.15 | 2,182.70 | 2,362.39 | 13 Oct 10:30 |
| hourly_macd_swing | NSE:AXISBANK | 13 | 1,263.65 | 1,245.45 | 1,299.89 | 13 Oct 14:30 |
| ema_crossover | NSE:KOTAKBANK | 37 | 443.14 | 440.58 | 447.99 | 14 Oct 10:00 |
| ema_crossover | NSE:SUNPHARMA | -9 | 1,754.65 | 1,762.69 | 1,736.62 | 14 Oct 10:00 |
| ema_crossover | NSE:ICICIBANK | -12 | 1,348.63 | 1,354.75 | 1,338.09 | 14 Oct 11:30 |
| rsi2_scalper | NSE:AXISBANK | 13 | 1,260.05 | 1,249.72 | – | 14 Oct 11:45 |
| bb_squeeze | NSE:SUNPHARMA | -9 | 1,752.55 | 1,761.08 | 1,736.85 | 14 Oct 09:45 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| vwap_reversion | NSE:BHARTIARTL | -9 | 1,815.14 | 1,824.47 | – | 14 Oct 11:15 |
| vwap_reversion | NSE:RELIANCE | -13 | 1,178.76 | 1,185.10 | – | 14 Oct 12:15 |
| vwap_pullback | NSE:INFY | 15 | 1,080.82 | 1,074.07 | 1,093.36 | 14 Oct 09:45 |
| vwap_pullback | NSE:LT | -4 | 3,646.67 | 3,661.21 | 3,619.48 | 14 Oct 09:45 |
| vwap_pullback | NSE:KOTAKBANK | 36 | 443.39 | 441.82 | 446.25 | 14 Oct 11:45 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.261364 | 83,345.55 | – | – | 13 Oct 09:30 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.68092 | 2,508.57 | – | – | 13 Oct 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 14 Oct 12:15 | vwap_reversion | SELL | 13 | NSE:RELIANCE | 1,178.76 |  | 2.7 sigma above VWAP |
| 14 Oct 12:15 | rsi2_scalper | SELL | 15 | NSE:INFY | 1,086.43 | +54 | RSI2 snapped back (76) |
| 14 Oct 12:15 | macd_adx | BUY | 17 | NSE:SBIN | 951.19 | -88 | stop-loss |
| 14 Oct 12:00 | rsi2_scalper | SELL | 17 | NSE:SBIN | 947.16 | -15 | time stop (1h) |
| 14 Oct 11:45 | vwap_pullback | BUY | 36 | NSE:KOTAKBANK | 443.39 |  | pullback held VWAP in uptrend |
| 14 Oct 11:45 | vwap_pullback | SELL | 7 | NSE:TCS | 2,301.24 | -121 | lost VWAP |
| 14 Oct 11:45 | tv_rating_scalper | SELL | 9 | NSE:SUNPHARMA | 1,749.85 |  | TV 15m -0.60 / 1h -0.42 |
| 14 Oct 11:45 | tv_rating_scalper | SELL | 7 | NSE:TCS | 2,301.24 | -161 | stop-loss |
| 14 Oct 11:45 | rsi2_scalper | BUY | 13 | NSE:AXISBANK | 1,260.05 |  | RSI2 5 in uptrend |
| 14 Oct 11:45 | rsi2_scalper | BUY | 15 | NSE:INFY | 1,082.27 |  | RSI2 9 in uptrend |
| 14 Oct 11:45 | macd_adx | SELL | 7 | NSE:TCS | 2,301.24 | -161 | MACD reversed |
| 14 Oct 11:30 | ema_crossover | SELL | 12 | NSE:ICICIBANK | 1,348.63 |  | EMA9<21, RSI 44 |
| 14 Oct 11:15 | vwap_reversion | SELL | 9 | NSE:BHARTIARTL | 1,815.14 |  | 2.0 sigma above VWAP |
| 14 Oct 11:15 | tv_rating_scalper | BUY | 9 | NSE:BHARTIARTL | 1,815.86 |  | TV 15m +0.51 / 1h +0.42 |
| 14 Oct 11:15 | rsi2_scalper | SELL | 12 | NSE:ICICIBANK | 1,349.43 | -36 | time stop (1h) |
| 14 Oct 11:15 | macd_adx | SELL | 17 | NSE:SBIN | 946.51 |  | MACD down, ADX 23 |
| 14 Oct 11:05 | bb_squeeze | SELL | 63 | NSE:ITC | 260.00 | -75 | stop-loss |
| 14 Oct 11:00 | rsi2_scalper | BUY | 17 | NSE:SBIN | 947.59 |  | RSI2 4 in uptrend |
| 14 Oct 10:55 | tv_rating_scalper | SELL | 17 | NSE:SBIN | 947.31 | -149 | stop-loss |
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
