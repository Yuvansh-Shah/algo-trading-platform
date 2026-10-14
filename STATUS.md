# 🏆 Bot Leaderboard

_Updated 14 Oct 2026 13:20 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **tv_rating_scalper** | intraday 15m | +1.85% | +925 | +236 | +1.47% | 11 | 55 | 2.62 | -0.9% | 3 | ✅ |
| 🥈 | **gap_and_go** | intraday 15m | +1.46% | +732 | +257 | +1.09% | 2 | 100 | ∞ | -0.6% | 2 | ✅ |
| 🥉 | **supertrend_intraday** | intraday 15m | +1.05% | +523 | +34 | +0.67% | 3 | 67 | 31.05 | -0.5% | 3 | ✅ |
| 4 | **ema_crossover** | intraday 15m | +0.88% | +438 | +96 | +0.50% | 7 | 57 | 2.68 | -0.4% | 1 | ✅ |
| 5 | **momentum_rotation** | positional 1D | +0.86% | +432 | +283 | +0.49% | 0 | – | – | -1.2% | 3 | ✅ |
| 6 | **hourly_macd_swing** | swing 1h | +0.53% | +265 | +39 | +0.15% | 0 | – | – | -0.8% | 2 | ✅ |
| 7 | **orb_breakout** | intraday 15m | +0.45% | +223 | -226 | +0.07% | 4 | 75 | 2.90 | -0.6% | 2 | ✅ |
| 8 | **nifty_buy_hold** | benchmark 1D | +0.38% | +188 | -298 | +0.00% | 0 | – | – | -0.6% | 1 | ✅ |
| 9 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -0.38% | 0 | – | – | 0.0% | 0 | ✅ |
| 10 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -0.38% | 0 | – | – | 0.0% | 0 | ✅ |
| 11 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -0.38% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -0.38% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **tv_rating_swing** | swing 1D | +0.00% | +0 | +0 | -0.38% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **rsi2_scalper** | scalp 15m | -0.11% | -55 | +93 | -0.49% | 12 | 50 | 1.20 | -0.4% | 2 | ✅ |
| 15 | **bb_squeeze** | intraday 15m | -0.16% | -82 | -113 | -0.54% | 7 | 43 | 0.93 | -0.6% | 0 | ✅ |
| 16 | **donchian_turtle** | swing 1D | -0.44% | -219 | -118 | -0.82% | 0 | – | – | -0.4% | 1 | ✅ |
| 17 | **vwap_reversion** | intraday 15m | -0.71% | -356 | -152 | -1.09% | 9 | 44 | 0.30 | -1.1% | 3 | ✅ |
| 18 | **macd_adx** | intraday 15m | -0.93% | -467 | -345 | -1.31% | 6 | 17 | 0.31 | -1.2% | 2 | ✅ |
| 19 | **vwap_pullback** | intraday 15m | -1.15% | -575 | -461 | -1.53% | 14 | 21 | 0.56 | -1.7% | 2 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -3.17% | -1,586 | -124 | -3.55% | 9 | 22 | 0.12 | -3.6% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
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
| tv_rating_scalper | NSE:BHARTIARTL | 9 | 1,815.86 | 1,800.98 | 1,844.55 | 14 Oct 11:15 |
| tv_rating_scalper | NSE:SUNPHARMA | -9 | 1,749.85 | 1,764.20 | 1,722.20 | 14 Oct 11:45 |
| tv_rating_scalper | NSE:LT | -4 | 3,629.47 | 3,659.24 | 3,572.12 | 14 Oct 13:15 |
| gap_and_go | NSE:INFY | 15 | 1,073.91 | 1,027.00 | 1,129.30 | 14 Oct 09:25 |
| gap_and_go | NSE:TCS | 7 | 2,274.45 | 2,155.00 | 2,482.00 | 14 Oct 09:25 |
| supertrend_intraday | NSE:AXISBANK | -13 | 1,259.65 | 1,278.69 | 1,222.62 | 14 Oct 09:45 |
| supertrend_intraday | NSE:KOTAKBANK | 37 | 442.94 | 435.91 | 456.89 | 14 Oct 09:45 |
| supertrend_intraday | NSE:ICICIBANK | -12 | 1,351.23 | 1,365.86 | 1,322.79 | 14 Oct 10:15 |
| ema_crossover | NSE:ICICIBANK | -12 | 1,348.63 | 1,354.75 | 1,338.09 | 14 Oct 11:30 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| hourly_macd_swing | NSE:TCS | 7 | 2,242.15 | 2,182.70 | 2,362.39 | 13 Oct 10:30 |
| hourly_macd_swing | NSE:AXISBANK | 13 | 1,263.65 | 1,245.45 | 1,299.89 | 13 Oct 14:30 |
| orb_breakout | NSE:RELIANCE | 14 | 1,171.83 | 1,162.70 | 1,186.70 | 14 Oct 10:00 |
| orb_breakout | NSE:INFY | 15 | 1,087.62 | 1,069.45 | 1,122.55 | 14 Oct 10:30 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| rsi2_scalper | NSE:TCS | 7 | 2,294.26 | 2,275.45 | – | 14 Oct 13:00 |
| rsi2_scalper | NSE:INFY | 15 | 1,080.27 | 1,071.41 | – | 14 Oct 13:15 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| vwap_reversion | NSE:BHARTIARTL | -9 | 1,815.14 | 1,824.47 | – | 14 Oct 11:15 |
| vwap_reversion | NSE:RELIANCE | -13 | 1,184.86 | 1,190.65 | – | 14 Oct 13:00 |
| vwap_reversion | NSE:SUNPHARMA | 9 | 1,735.05 | 1,728.53 | – | 14 Oct 13:15 |
| macd_adx | NSE:SBIN | 17 | 954.34 | 947.94 | 961.62 | 14 Oct 12:30 |
| macd_adx | NSE:KOTAKBANK | -37 | 441.21 | 443.77 | 437.10 | 14 Oct 13:15 |
| vwap_pullback | NSE:INFY | 15 | 1,080.82 | 1,074.07 | 1,093.36 | 14 Oct 09:45 |
| vwap_pullback | NSE:SBIN | 17 | 950.79 | 948.75 | 957.44 | 14 Oct 13:15 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.261364 | 83,345.55 | – | – | 13 Oct 09:30 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.68092 | 2,508.57 | – | – | 13 Oct 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 14 Oct 13:20 | vwap_pullback | BUY | 9 | NSE:SUNPHARMA | 1,730.35 | +116 | target |
| 14 Oct 13:20 | orb_breakout | SELL | 23 | NSE:HDFCBANK | 711.01 | -163 | stop-loss |
| 14 Oct 13:20 | ema_crossover | SELL | 37 | NSE:KOTAKBANK | 440.36 | -111 | stop-loss |
| 14 Oct 13:15 | vwap_reversion | BUY | 9 | NSE:SUNPHARMA | 1,735.05 |  | -2.6 sigma below VWAP |
| 14 Oct 13:15 | vwap_reversion | SELL | 9 | NSE:SUNPHARMA | 1,734.35 | -102 | stop-loss |
| 14 Oct 13:15 | vwap_pullback | BUY | 17 | NSE:SBIN | 950.79 |  | pullback held VWAP in uptrend |
| 14 Oct 13:15 | tv_rating_scalper | SELL | 4 | NSE:LT | 3,629.47 |  | TV 15m -0.56 / 1h -0.47 |
| 14 Oct 13:15 | tv_rating_scalper | SELL | 23 | NSE:HDFCBANK | 712.66 | -3 | 15m rating faded (-0.07) |
| 14 Oct 13:15 | rsi2_scalper | BUY | 15 | NSE:INFY | 1,080.27 |  | RSI2 8 in uptrend |
| 14 Oct 13:15 | macd_adx | SELL | 37 | NSE:KOTAKBANK | 441.21 |  | MACD down, ADX 22 |
| 14 Oct 13:15 | ema_crossover | BUY | 9 | NSE:SUNPHARMA | 1,735.05 | +169 | target |
| 14 Oct 13:15 | bb_squeeze | BUY | 9 | NSE:SUNPHARMA | 1,736.75 | +134 | target |
| 14 Oct 13:10 | vwap_pullback | SELL | 36 | NSE:KOTAKBANK | 441.61 | -72 | stop-loss |
| 14 Oct 13:00 | vwap_reversion | SELL | 13 | NSE:RELIANCE | 1,184.86 |  | 3.6 sigma above VWAP |
| 14 Oct 13:00 | rsi2_scalper | BUY | 7 | NSE:TCS | 2,294.26 |  | RSI2 4 in uptrend |
| 14 Oct 12:55 | vwap_reversion | BUY | 13 | NSE:RELIANCE | 1,185.34 | -93 | stop-loss |
| 14 Oct 12:45 | rsi2_scalper | SELL | 13 | NSE:AXISBANK | 1,262.95 | +29 | RSI2 snapped back (81) |
| 14 Oct 12:31 | vwap_reversion | BUY | 9 | NSE:SUNPHARMA | 1,744.85 |  | -2.2 sigma below VWAP |
| 14 Oct 12:31 | vwap_pullback | SELL | 9 | NSE:SUNPHARMA | 1,744.15 |  | rally rejected at VWAP in downtrend |
| 14 Oct 12:31 | vwap_pullback | BUY | 4 | NSE:LT | 3,657.43 | -50 | lost VWAP |
| 14 Oct 12:30 | macd_adx | BUY | 17 | NSE:SBIN | 954.34 |  | MACD up, ADX 21 |
| 14 Oct 12:15 | vwap_reversion | SELL | 13 | NSE:RELIANCE | 1,178.76 |  | 2.7 sigma above VWAP |
| 14 Oct 12:15 | rsi2_scalper | SELL | 15 | NSE:INFY | 1,086.43 | +54 | RSI2 snapped back (76) |
| 14 Oct 12:15 | macd_adx | BUY | 17 | NSE:SBIN | 951.19 | -88 | stop-loss |
| 14 Oct 12:00 | rsi2_scalper | SELL | 17 | NSE:SBIN | 947.16 | -15 | time stop (1h) |
| 14 Oct 11:45 | vwap_pullback | BUY | 36 | NSE:KOTAKBANK | 443.39 |  | pullback held VWAP in uptrend |
| 14 Oct 11:45 | vwap_pullback | SELL | 7 | NSE:TCS | 2,301.24 | -121 | lost VWAP |
| 14 Oct 11:45 | tv_rating_scalper | SELL | 9 | NSE:SUNPHARMA | 1,749.85 |  | TV 15m -0.60 / 1h -0.42 |
| 14 Oct 11:45 | tv_rating_scalper | SELL | 7 | NSE:TCS | 2,301.24 | -161 | stop-loss |
| 14 Oct 11:45 | rsi2_scalper | BUY | 13 | NSE:AXISBANK | 1,260.05 |  | RSI2 5 in uptrend |
