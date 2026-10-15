# 🏆 Bot Leaderboard

_Updated 15 Oct 2026 09:30 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 🥇 | **momentum_rotation** | positional 1D | +2.26% | +1,129 | +143 | +1.52% | 0 | – | – | -1.3% | 3 | ✅ |
| 🥈 | **gap_and_go** | intraday 15m | +2.18% | +1,090 | +194 | +1.44% | 4 | 100 | ∞ | -0.6% | 1 | ✅ |
| 🥉 | **tv_rating_scalper** | intraday 15m | +1.53% | +764 | -46 | +0.79% | 14 | 57 | 2.43 | -0.9% | 3 | ✅ |
| 4 | **hourly_macd_swing** | swing 1h | +1.33% | +663 | +85 | +0.59% | 1 | 0 | 0.00 | -0.9% | 2 | ✅ |
| 5 | **orb_breakout** | intraday 15m | +0.89% | +446 | +1 | +0.15% | 6 | 83 | 4.10 | -0.6% | 1 | ✅ |
| 6 | **nifty_buy_hold** | benchmark 1D | +0.74% | +369 | +156 | +0.00% | 0 | – | – | -0.8% | 1 | ✅ |
| 7 | **tv_rating_swing** | swing 1D | +0.69% | +344 | +145 | -0.05% | 0 | – | – | -0.1% | 1 | ✅ |
| 8 | **supertrend_intraday** | intraday 15m | +0.59% | +295 | +1 | -0.15% | 6 | 50 | 2.38 | -0.5% | 1 | ✅ |
| 9 | **ema_crossover** | intraday 15m | +0.55% | +274 | +0 | -0.19% | 11 | 45 | 1.94 | -0.4% | 0 | ✅ |
| 10 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -0.74% | 0 | – | – | 0.0% | 0 | ✅ |
| 11 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -0.74% | 0 | – | – | 0.0% | 0 | ✅ |
| 12 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -0.74% | 0 | – | – | 0.0% | 0 | ✅ |
| 13 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -0.74% | 0 | – | – | 0.0% | 0 | ✅ |
| 14 | **rsi2_scalper** | scalp 15m | -0.12% | -58 | +0 | -0.85% | 16 | 56 | 1.23 | -0.4% | 0 | ✅ |
| 15 | **donchian_turtle** | swing 1D | -0.16% | -78 | +1 | -0.89% | 0 | – | – | -0.5% | 1 | ✅ |
| 16 | **bb_squeeze** | intraday 15m | -0.25% | -124 | +0 | -0.99% | 8 | 38 | 0.84 | -0.6% | 0 | ✅ |
| 17 | **vwap_pullback** | intraday 15m | -0.85% | -425 | +0 | -1.59% | 19 | 32 | 0.74 | -1.7% | 0 | ✅ |
| 18 | **vwap_reversion** | intraday 15m | -0.97% | -485 | +0 | -1.71% | 15 | 47 | 0.46 | -1.2% | 0 | ✅ |
| 19 | **macd_adx** | intraday 15m | -1.10% | -552 | +0 | -1.84% | 10 | 20 | 0.36 | -1.4% | 0 | ✅ |
| 20 | **crypto_supertrend** | crypto 1h | -7.02% | -3,511 | +0 | -7.76% | 11 | 18 | 0.06 | -7.1% | 0 | ✅ |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement; exit when 15m turns neutral |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| supertrend_intraday | Supertrend 10/3 flips on 15m, stop at the Supertrend line, 2R |
| ema_crossover | EMA 9/21 cross + RSI>50 + above VWAP (mirror for shorts), 1.5/3 ATR |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
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
| gap_and_go | NSE:INFY | 15 | 1,099.22 | 1,069.45 | 1,131.85 | 15 Oct 09:25 |
| tv_rating_scalper | NSE:AXISBANK | 13 | 1,267.25 | 1,256.86 | 1,287.27 | 15 Oct 09:25 |
| tv_rating_scalper | NSE:ICICIBANK | -12 | 1,341.83 | 1,352.84 | 1,320.63 | 15 Oct 09:25 |
| tv_rating_scalper | NSE:ITC | 63 | 262.55 | 260.40 | 266.70 | 15 Oct 09:30 |
| hourly_macd_swing | NSE:TCS | 7 | 2,242.15 | 2,182.70 | 2,362.39 | 13 Oct 10:30 |
| hourly_macd_swing | NSE:AXISBANK | 13 | 1,267.25 | 1,254.59 | 1,315.81 | 15 Oct 09:25 |
| orb_breakout | NSE:AXISBANK | 13 | 1,267.25 | 1,259.30 | 1,306.40 | 15 Oct 09:25 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,501.48 | – | 14 Oct 15:05 |
| supertrend_intraday | NSE:AXISBANK | 13 | 1,267.25 | 1,255.50 | 1,314.00 | 15 Oct 09:25 |
| donchian_turtle | NSE:AXISBANK | 12 | 1,272.95 | 1,220.87 | – | 13 Oct 15:10 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 15 Oct 09:30 | tv_rating_scalper | BUY | 63 | NSE:ITC | 262.55 |  | TV 15m +0.69 / 1h +0.29 |
| 15 Oct 09:25 | tv_rating_scalper | SELL | 12 | NSE:ICICIBANK | 1,341.83 |  | TV 15m -0.54 / 1h -0.33 |
| 15 Oct 09:25 | tv_rating_scalper | BUY | 13 | NSE:AXISBANK | 1,267.25 |  | TV 15m +0.56 / 1h +0.60 |
| 15 Oct 09:25 | supertrend_intraday | BUY | 13 | NSE:AXISBANK | 1,267.25 |  | Supertrend flipped up |
| 15 Oct 09:25 | orb_breakout | BUY | 13 | NSE:AXISBANK | 1,267.25 |  | ORB up > 1269.9 |
| 15 Oct 09:25 | hourly_macd_swing | BUY | 13 | NSE:AXISBANK | 1,267.25 |  | 1h MACD bull cross above EMA200 |
| 15 Oct 09:25 | gap_and_go | BUY | 15 | NSE:INFY | 1,099.22 |  | gap up +1.0% and go |
| 15 Oct 09:00 | crypto_supertrend | SELL | 8.68092 | BINANCE:ETHUSDT | 2,363.04 | -1,274 | Supertrend turned down |
| 15 Oct 09:00 | crypto_supertrend | SELL | 0.261364 | BINANCE:BTCUSDT | 81,038.18 | -614 | Supertrend turned down |
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
