# 🏆 Bot Leaderboard

_Updated 14 Oct 2026 09:45 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **tv_rating_scalper** | intraday 15m | +2.03% | +1,017 | +327 | +1.25% | 8 | 75 | 6.33 | -0.5% | 3 | ✅ |
| 🥈 | **momentum_rotation** | positional 1D | +1.84% | +920 | +771 | +1.06% | 0 | – | – | -0.2% | 3 | ✅ |
| 🥉 | **gap_and_go** | intraday 15m | +1.84% | +919 | +444 | +1.06% | 2 | 100 | ∞ | -0.5% | 2 | ✅ |
| 4 | **hourly_macd_swing** | swing 1h | +1.00% | +498 | +273 | +0.22% | 0 | – | – | -0.3% | 2 | ✅ |
| 5 | **supertrend_intraday** | intraday 15m | +0.93% | +467 | -23 | +0.15% | 3 | 67 | 31.05 | -0.4% | 2 | ✅ |
| 6 | **orb_breakout** | intraday 15m | +0.90% | +449 | +0 | +0.12% | 3 | 100 | ∞ | -0.6% | 0 | ✅ |
| 7 | **nifty_buy_hold** | benchmark 1D | +0.78% | +390 | -96 | +0.00% | 0 | – | – | -0.3% | 1 | ✅ |
| 8 | **ema_crossover** | intraday 15m | +0.68% | +342 | +0 | -0.10% | 5 | 60 | 3.53 | -0.4% | 0 | ✅ |
| 9 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -0.78% | 0 | – | – | 0.0% | 0 | ✅ |
| 10 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -0.78% | 0 | – | – | 0.0% | 0 | ✅ |
| 11 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -0.78% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -0.78% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **tv_rating_swing** | swing 1D | +0.00% | +0 | +0 | -0.78% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **macd_adx** | intraday 15m | -0.27% | -133 | -11 | -1.05% | 4 | 25 | 0.63 | -0.5% | 1 | ✅ |
| 15 | **bb_squeeze** | intraday 15m | -0.29% | -145 | -176 | -1.07% | 5 | 40 | 0.69 | -0.5% | 2 | ✅ |
| 16 | **vwap_pullback** | intraday 15m | -0.29% | -147 | -33 | -1.07% | 8 | 25 | 0.89 | -0.7% | 3 | ✅ |
| 17 | **rsi2_scalper** | scalp 15m | -0.32% | -159 | -11 | -1.10% | 7 | 43 | 0.43 | -0.4% | 1 | ✅ |
| 18 | **donchian_turtle** | swing 1D | -0.33% | -164 | -62 | -1.11% | 0 | – | – | -0.3% | 1 | ✅ |
| 19 | **vwap_reversion** | intraday 15m | -0.41% | -204 | +0 | -1.19% | 7 | 57 | 0.50 | -0.6% | 0 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -2.99% | -1,496 | -35 | -3.77% | 9 | 22 | 0.12 | -3.6% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| tv_rating_scalper | NSE:HDFCBANK | 23 | 712.44 | 706.60 | 723.70 | 14 Oct 09:25 |
| tv_rating_scalper | NSE:SBIN | 17 | 955.59 | 947.76 | 970.69 | 14 Oct 09:25 |
| tv_rating_scalper | NSE:TCS | 7 | 2,323.06 | 2,304.02 | 2,359.76 | 14 Oct 09:45 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| gap_and_go | NSE:INFY | 15 | 1,073.91 | 1,027.00 | 1,129.30 | 14 Oct 09:25 |
| gap_and_go | NSE:TCS | 7 | 2,274.45 | 2,155.00 | 2,482.00 | 14 Oct 09:25 |
| hourly_macd_swing | NSE:TCS | 7 | 2,242.15 | 2,182.70 | 2,362.39 | 13 Oct 10:30 |
| hourly_macd_swing | NSE:AXISBANK | 13 | 1,263.65 | 1,245.45 | 1,299.89 | 13 Oct 14:30 |
| supertrend_intraday | NSE:AXISBANK | -13 | 1,259.65 | 1,278.69 | 1,222.62 | 14 Oct 09:45 |
| supertrend_intraday | NSE:KOTAKBANK | 37 | 442.94 | 435.91 | 456.89 | 14 Oct 09:45 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| macd_adx | NSE:TCS | 7 | 2,323.06 | 2,298.25 | 2,363.51 | 14 Oct 09:45 |
| bb_squeeze | NSE:ITC | 63 | 261.05 | 260.10 | 263.56 | 14 Oct 09:25 |
| bb_squeeze | NSE:SUNPHARMA | -9 | 1,752.55 | 1,761.08 | 1,736.85 | 14 Oct 09:45 |
| vwap_pullback | NSE:INFY | 15 | 1,080.82 | 1,074.07 | 1,093.36 | 14 Oct 09:45 |
| vwap_pullback | NSE:TCS | 7 | 2,323.06 | 2,305.50 | 2,349.00 | 14 Oct 09:45 |
| vwap_pullback | NSE:LT | -4 | 3,646.67 | 3,661.21 | 3,619.48 | 14 Oct 09:45 |
| rsi2_scalper | NSE:AXISBANK | 13 | 1,260.15 | 1,249.82 | – | 14 Oct 09:45 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.261364 | 83,345.55 | – | – | 13 Oct 09:30 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.68092 | 2,508.57 | – | – | 13 Oct 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
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
| 14 Oct 09:25 | bb_squeeze | BUY | 9 | NSE:SUNPHARMA | 1,770.45 |  | squeeze breakout up |
| 14 Oct 09:25 | bb_squeeze | BUY | 63 | NSE:ITC | 261.05 |  | squeeze breakout up |
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
