# 🏆 Bot Leaderboard

_Updated 14 Oct 2026 13:35 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **tv_rating_scalper** | intraday 15m | +1.88% | +939 | +250 | +1.66% | 11 | 55 | 2.62 | -0.9% | 3 | ✅ |
| 🥈 | **gap_and_go** | intraday 15m | +1.48% | +742 | +267 | +1.27% | 2 | 100 | ∞ | -0.6% | 2 | ✅ |
| 🥉 | **supertrend_intraday** | intraday 15m | +1.02% | +511 | +22 | +0.81% | 3 | 67 | 31.05 | -0.5% | 3 | ✅ |
| 4 | **ema_crossover** | intraday 15m | +0.86% | +432 | +90 | +0.65% | 7 | 57 | 2.68 | -0.4% | 3 | ✅ |
| 5 | **momentum_rotation** | positional 1D | +0.77% | +384 | +234 | +0.55% | 0 | – | – | -1.3% | 3 | ✅ |
| 6 | **hourly_macd_swing** | swing 1h | +0.47% | +236 | +10 | +0.26% | 1 | 0 | 0.00 | -0.9% | 1 | ✅ |
| 7 | **orb_breakout** | intraday 15m | +0.45% | +226 | -223 | +0.24% | 4 | 75 | 2.90 | -0.6% | 2 | ✅ |
| 8 | **nifty_buy_hold** | benchmark 1D | +0.22% | +108 | -378 | +0.00% | 0 | – | – | -0.8% | 1 | ✅ |
| 9 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -0.22% | 0 | – | – | 0.0% | 0 | ✅ |
| 10 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -0.22% | 0 | – | – | 0.0% | 0 | ✅ |
| 11 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -0.22% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -0.22% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **tv_rating_swing** | swing 1D | +0.00% | +0 | +0 | -0.22% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **bb_squeeze** | intraday 15m | -0.16% | -82 | -113 | -0.38% | 7 | 43 | 0.93 | -0.6% | 0 | ✅ |
| 15 | **rsi2_scalper** | scalp 15m | -0.17% | -83 | +64 | -0.38% | 12 | 50 | 1.20 | -0.4% | 3 | ✅ |
| 16 | **donchian_turtle** | swing 1D | -0.42% | -211 | -109 | -0.64% | 0 | – | – | -0.5% | 1 | ✅ |
| 17 | **vwap_reversion** | intraday 15m | -0.80% | -400 | -196 | -1.01% | 12 | 50 | 0.51 | -1.1% | 3 | ✅ |
| 18 | **macd_adx** | intraday 15m | -0.97% | -487 | -366 | -1.19% | 7 | 14 | 0.25 | -1.3% | 2 | ✅ |
| 19 | **vwap_pullback** | intraday 15m | -1.20% | -599 | -485 | -1.41% | 15 | 20 | 0.52 | -1.7% | 1 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -2.89% | -1,446 | +15 | -3.11% | 9 | 22 | 0.12 | -3.6% | 2 | ✅ |

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
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
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
| ema_crossover | NSE:HDFCBANK | -23 | 709.61 | 712.52 | 702.42 | 14 Oct 13:30 |
| ema_crossover | NSE:LT | -4 | 3,606.08 | 3,624.84 | 3,571.33 | 14 Oct 13:30 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| hourly_macd_swing | NSE:TCS | 7 | 2,242.15 | 2,182.70 | 2,362.39 | 13 Oct 10:30 |
| orb_breakout | NSE:RELIANCE | 14 | 1,171.83 | 1,162.70 | 1,186.70 | 14 Oct 10:00 |
| orb_breakout | NSE:INFY | 15 | 1,087.62 | 1,069.45 | 1,122.55 | 14 Oct 10:30 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| rsi2_scalper | NSE:TCS | 7 | 2,294.26 | 2,275.45 | – | 14 Oct 13:00 |
| rsi2_scalper | NSE:INFY | 15 | 1,080.27 | 1,071.41 | – | 14 Oct 13:15 |
| rsi2_scalper | NSE:BHARTIARTL | 9 | 1,808.76 | 1,793.93 | – | 14 Oct 13:30 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| vwap_reversion | NSE:HDFCBANK | 23 | 709.89 | 705.78 | – | 14 Oct 13:30 |
| vwap_reversion | NSE:KOTAKBANK | 37 | 439.74 | 437.45 | – | 14 Oct 13:30 |
| vwap_reversion | NSE:SUNPHARMA | 9 | 1,727.15 | 1,717.53 | – | 14 Oct 13:30 |
| macd_adx | NSE:KOTAKBANK | -37 | 441.21 | 443.77 | 437.10 | 14 Oct 13:15 |
| macd_adx | NSE:SBIN | -17 | 947.41 | 951.02 | 937.17 | 14 Oct 13:30 |
| vwap_pullback | NSE:INFY | 15 | 1,080.82 | 1,074.07 | 1,093.36 | 14 Oct 09:45 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.261364 | 83,345.55 | – | – | 13 Oct 09:30 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.68092 | 2,508.57 | – | – | 13 Oct 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 14 Oct 13:30 | vwap_reversion | BUY | 9 | NSE:SUNPHARMA | 1,727.15 |  | -3.2 sigma below VWAP |
| 14 Oct 13:30 | vwap_reversion | BUY | 9 | NSE:BHARTIARTL | 1,809.46 | +43 | back to VWAP |
| 14 Oct 13:30 | vwap_reversion | BUY | 37 | NSE:KOTAKBANK | 439.74 |  | -2.5 sigma below VWAP |
| 14 Oct 13:30 | vwap_reversion | BUY | 23 | NSE:HDFCBANK | 709.89 |  | -2.6 sigma below VWAP |
| 14 Oct 13:30 | vwap_reversion | BUY | 13 | NSE:RELIANCE | 1,176.34 | +103 | back to VWAP |
| 14 Oct 13:30 | rsi2_scalper | BUY | 9 | NSE:BHARTIARTL | 1,808.76 |  | RSI2 5 in uptrend |
| 14 Oct 13:30 | macd_adx | SELL | 17 | NSE:SBIN | 947.41 |  | MACD down, ADX 23 |
| 14 Oct 13:30 | hourly_macd_swing | SELL | 13 | NSE:AXISBANK | 1,254.35 | -129 | 1h MACD bear cross |
| 14 Oct 13:30 | ema_crossover | SELL | 4 | NSE:LT | 3,606.08 |  | EMA9<21, RSI 32 |
| 14 Oct 13:30 | ema_crossover | SELL | 23 | NSE:HDFCBANK | 709.61 |  | EMA9<21, RSI 41 |
| 14 Oct 13:25 | vwap_reversion | SELL | 9 | NSE:SUNPHARMA | 1,726.75 | -82 | stop-loss |
| 14 Oct 13:25 | vwap_pullback | SELL | 17 | NSE:SBIN | 947.06 | -71 | stop-loss |
| 14 Oct 13:25 | macd_adx | SELL | 17 | NSE:SBIN | 947.06 | -132 | stop-loss |
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
