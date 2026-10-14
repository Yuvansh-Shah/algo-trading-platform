# 🏆 Bot Leaderboard

_Updated 14 Oct 2026 15:35 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **gap_and_go** | intraday 15m | +1.82% | +908 | +432 | +1.41% | 4 | 100 | ∞ | -0.6% | 0 | ✅ |
| 🥈 | **tv_rating_scalper** | intraday 15m | +1.67% | +833 | +144 | +1.26% | 14 | 57 | 2.43 | -0.9% | 0 | ✅ |
| 🥉 | **orb_breakout** | intraday 15m | +0.91% | +456 | +7 | +0.51% | 6 | 83 | 4.10 | -0.6% | 0 | ✅ |
| 4 | **momentum_rotation** | positional 1D | +0.71% | +354 | +204 | +0.30% | 0 | – | – | -1.3% | 3 | ✅ |
| 5 | **supertrend_intraday** | intraday 15m | +0.61% | +305 | -184 | +0.21% | 6 | 50 | 2.38 | -0.5% | 0 | ✅ |
| 6 | **ema_crossover** | intraday 15m | +0.55% | +274 | -67 | +0.15% | 11 | 45 | 1.94 | -0.4% | 0 | ✅ |
| 7 | **hourly_macd_swing** | swing 1h | +0.52% | +258 | +33 | +0.11% | 1 | 0 | 0.00 | -0.9% | 1 | ✅ |
| 8 | **nifty_buy_hold** | benchmark 1D | +0.40% | +202 | -284 | +0.00% | 0 | – | – | -0.8% | 1 | ✅ |
| 9 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -0.40% | 0 | – | – | 0.0% | 0 | ✅ |
| 10 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -0.40% | 0 | – | – | 0.0% | 0 | ✅ |
| 11 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -0.40% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -0.40% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **tv_rating_swing** | swing 1D | -0.01% | -6 | -6 | -0.42% | 0 | – | – | -0.1% | 1 | ✅ |
| 14 | **rsi2_scalper** | scalp 15m | -0.12% | -58 | +89 | -0.52% | 16 | 56 | 1.23 | -0.4% | 0 | ✅ |
| 15 | **donchian_turtle** | swing 1D | -0.12% | -61 | +41 | -0.53% | 0 | – | – | -0.5% | 1 | ✅ |
| 16 | **bb_squeeze** | intraday 15m | -0.25% | -124 | -155 | -0.65% | 8 | 38 | 0.84 | -0.6% | 0 | ✅ |
| 17 | **vwap_pullback** | intraday 15m | -0.85% | -425 | -311 | -1.25% | 19 | 32 | 0.74 | -1.7% | 0 | ✅ |
| 18 | **vwap_reversion** | intraday 15m | -0.97% | -485 | -282 | -1.37% | 15 | 47 | 0.46 | -1.2% | 0 | ✅ |
| 19 | **macd_adx** | intraday 15m | -1.10% | -552 | -430 | -1.51% | 10 | 20 | 0.36 | -1.4% | 0 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -3.72% | -1,860 | -399 | -4.12% | 9 | 22 | 0.12 | -3.8% | 2 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
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
| hourly_macd_swing | NSE:TCS | 7 | 2,242.15 | 2,182.70 | 2,362.39 | 13 Oct 10:30 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,468.93 | – | 14 Oct 15:05 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |
| crypto_supertrend | BINANCE:BTCUSDT | 0.261364 | 83,345.55 | – | – | 13 Oct 09:30 |
| crypto_supertrend | BINANCE:ETHUSDT | 8.68092 | 2,508.57 | – | – | 13 Oct 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 14 Oct 15:15 | vwap_reversion | SELL | 9 | NSE:SUNPHARMA | 1,729.55 | +14 | intraday square-off |
| 14 Oct 15:15 | vwap_reversion | SELL | 37 | NSE:KOTAKBANK | 437.66 | -85 | intraday square-off |
| 14 Oct 15:15 | vwap_reversion | SELL | 23 | NSE:HDFCBANK | 709.56 | -16 | intraday square-off |
| 14 Oct 15:15 | vwap_pullback | SELL | 62 | NSE:ITC | 261.90 | +26 | intraday square-off |
| 14 Oct 15:15 | vwap_pullback | SELL | 13 | NSE:RELIANCE | 1,181.66 | +37 | intraday square-off |
| 14 Oct 15:15 | tv_rating_scalper | BUY | 4 | NSE:LT | 3,617.12 | +42 | intraday square-off |
| 14 Oct 15:15 | tv_rating_scalper | BUY | 9 | NSE:SUNPHARMA | 1,730.25 | +169 | intraday square-off |
| 14 Oct 15:15 | supertrend_intraday | BUY | 12 | NSE:ICICIBANK | 1,343.97 | +79 | intraday square-off |
| 14 Oct 15:15 | supertrend_intraday | BUY | 13 | NSE:AXISBANK | 1,265.85 | -89 | intraday square-off |
| 14 Oct 15:15 | orb_breakout | SELL | 15 | NSE:INFY | 1,092.53 | +66 | intraday square-off |
| 14 Oct 15:15 | orb_breakout | SELL | 14 | NSE:RELIANCE | 1,181.66 | +129 | intraday square-off |
| 14 Oct 15:15 | macd_adx | BUY | 37 | NSE:KOTAKBANK | 437.84 | +117 | intraday square-off |
| 14 Oct 15:15 | gap_and_go | SELL | 7 | NSE:TCS | 2,299.14 | +165 | intraday square-off |
| 14 Oct 15:15 | gap_and_go | SELL | 15 | NSE:INFY | 1,091.88 | +261 | intraday square-off |
| 14 Oct 15:15 | ema_crossover | SELL | 13 | NSE:AXISBANK | 1,265.35 | -19 | intraday square-off |
| 14 Oct 15:15 | ema_crossover | BUY | 23 | NSE:HDFCBANK | 709.84 | -14 | intraday square-off |
| 14 Oct 15:15 | ema_crossover | BUY | 12 | NSE:ICICIBANK | 1,343.97 | +48 | intraday square-off |
| 14 Oct 15:15 | bb_squeeze | SELL | 15 | NSE:INFY | 1,092.53 | -34 | intraday square-off |
| 14 Oct 15:05 | tv_rating_swing | BUY | 10 | NSE:TECHM | 1,579.32 |  | TV STRONG BUY +0.56, RSI 57 |
| 14 Oct 15:00 | macd_adx | SELL | 13 | NSE:RELIANCE | 1,183.46 | -36 | MACD reversed |
| 14 Oct 14:45 | ema_crossover | BUY | 13 | NSE:AXISBANK | 1,266.15 |  | EMA9>21, RSI 55 |
| 14 Oct 14:30 | vwap_pullback | SELL | 15 | NSE:INFY | 1,093.83 | +187 | target |
| 14 Oct 14:31 | rsi2_scalper | SELL | 9 | NSE:BHARTIARTL | 1,799.14 | -95 | time stop (1h) |
| 14 Oct 14:30 | bb_squeeze | BUY | 15 | NSE:INFY | 1,094.27 |  | squeeze breakout up |
| 14 Oct 14:15 | supertrend_intraday | SELL | 37 | NSE:KOTAKBANK | 439.11 | -150 | Supertrend reversed |
| 14 Oct 14:15 | rsi2_scalper | SELL | 63 | NSE:ITC | 261.90 | +17 | RSI2 snapped back (90) |
| 14 Oct 14:15 | macd_adx | BUY | 13 | NSE:RELIANCE | 1,185.64 |  | MACD up, ADX 34 |
| 14 Oct 14:10 | macd_adx | BUY | 17 | NSE:SBIN | 951.79 | -83 | stop-loss |
| 14 Oct 14:05 | ema_crossover | BUY | 4 | NSE:LT | 3,627.53 | -93 | stop-loss |
| 14 Oct 14:00 | vwap_pullback | BUY | 62 | NSE:ITC | 261.35 |  | pullback held VWAP in uptrend |
