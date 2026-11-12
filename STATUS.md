# Bot leaderboard

_Updated 12 Nov 2026 12:45 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **nifty_buy_hold** | benchmark 1D | +11.84% | +5,921 | +186 | +0.00% | 0 | – | – | -3.0% | 1 | ok |
| 2 | **dual_momentum** | positional 1D | +10.84% | +5,422 | +518 | -1.00% | 0 | – | – | -1.2% | 1 | ok |
| 3 | **tv_rating_swing** | swing 1D | +10.78% | +5,392 | +67 | -1.06% | 1 | 0 | 0.00 | -2.4% | 3 | ok |
| 4 | **momentum_rotation** | positional 1D | +8.75% | +4,374 | +368 | -3.10% | 2 | 100 | ∞ | -4.4% | 3 | ok |
| 5 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -11.84% | 0 | – | – | 0.0% | 0 | ok |
| 6 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -11.84% | 0 | – | – | 0.0% | 0 | ok |
| 7 | **supertrend_intraday** | intraday 15m | -0.17% | -84 | -412 | -12.01% | 36 | 44 | 1.25 | -2.5% | 3 | ok |
| 8 | **ema_crossover** | intraday 15m | -1.39% | -696 | -97 | -13.23% | 56 | 38 | 0.95 | -3.6% | 2 | ok |
| 9 | **tv_rating_scalper** | intraday 15m | -1.85% | -926 | -328 | -13.69% | 88 | 39 | 0.97 | -5.8% | 1 | ok |
| 10 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | +0 | -9.61% | 5 | 60 | 4.63 | -0.9% | 0 | retired |
| 11 | **gap_and_go** | intraday 15m | +1.40% | +701 | +0 | -10.44% | 10 | 80 | 2.36 | -1.2% | 0 | retired |
| 12 | **vwap_pullback** | intraday 15m | +0.98% | +491 | +0 | -10.86% | 41 | 51 | 1.48 | -1.7% | 0 | retired |
| 13 | **donchian_turtle** | swing 1D | +0.79% | +395 | +0 | -11.05% | 3 | 67 | 2.04 | -2.5% | 0 | retired |
| 14 | **orb_breakout** | intraday 15m | +0.54% | +272 | +0 | -11.30% | 15 | 60 | 1.51 | -1.5% | 0 | retired |
| 15 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -11.84% | 0 | – | – | 0.0% | 0 | retired |
| 16 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -11.84% | 0 | – | – | 0.0% | 0 | retired |
| 17 | **vwap_reversion** | intraday 15m | -0.33% | -166 | +0 | -12.17% | 35 | 57 | 1.09 | -1.3% | 0 | retired |
| 18 | **bb_squeeze** | intraday 15m | -0.98% | -492 | +0 | -12.83% | 20 | 40 | 0.68 | -1.4% | 0 | retired |
| 19 | **macd_adx** | intraday 15m | -1.02% | -512 | +0 | -12.87% | 22 | 32 | 0.71 | -1.4% | 0 | retired |
| 20 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | +0 | -13.37% | 35 | 49 | 0.61 | -1.5% | 0 | retired |
| 21 | **crypto_supertrend** | crypto 1h | -8.03% | -4,014 | +0 | -19.87% | 13 | 15 | 0.05 | -8.1% | 0 | retired |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| dual_momentum | Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| supertrend_intraday | Supertrend 10/3 flips on 15m with the NIFTY trend, entries before 11:00; 2R |
| ema_crossover | EMA 9/21 cross + RSI + VWAP, with the NIFTY trend, entries before 11:00; 1.5/3 ATR |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement, with the NIFTY trend, entries before 11:00 |
| hourly_macd_swing | 1h MACD crosses above signal while above EMA200; exit on cross down; 2/4 ATR |
| gap_and_go | Gap >0.8% + first 15m candle confirms + break of its high/low, 2R |
| vwap_pullback | Trend (EMA20>EMA50) + pullback that holds VWAP, 1 ATR stop, 2R target |
| donchian_turtle | Close above prior 20-day high -> buy; exit below 10-day low; 2 ATR stop |
| orb_breakout | 15-min opening range breakout, long/short, stop at other side, 2R target |
| connors_rsi2 | Close > SMA200 and RSI(2) < 10 -> buy; exit close > SMA5 (hold 1-5 days) |
| ema_trend_swing | EMA20>EMA50 uptrend, close crosses back above EMA20 -> buy; 8% trailing stop |
| vwap_reversion | Fade 2-sigma stretches from VWAP, exit back at VWAP |
| bb_squeeze | BB width at a 30-bar low, then a close outside the band; exit at mid band |
| macd_adx | MACD histogram crosses zero with ADX>20 and EMA50 trend; exit on opposite cross |
| rsi2_scalper | RSI(2)<10 above EMA50 (or >90 below), exit on snap-back or after 4 bars |
| crypto_supertrend | BTC/ETH long while 1h Supertrend 10/3 is up (checked in NSE hours only, USDT) |

</details>

## Open positions

| Bot | Symbol | Qty | Avg | Stop | Target | Opened |
|---|---|---:|---:|---:|---:|---|
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| dual_momentum | NSE:BANKBEES | 86 | 569.32 | – | – | 02 Nov 15:10 |
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,719.76 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,502.88 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:DRREDDY | 13 | 1,241.85 | 1,301.07 | – | 19 Oct 15:05 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:DRREDDY | 12 | 1,365.27 | 1,201.20 | – | 04 Nov 15:10 |
| momentum_rotation | NSE:ETERNAL | 49 | 361.57 | 318.12 | – | 09 Nov 15:10 |
| supertrend_intraday | NSE:ICICIBANK | 10 | 1,590.32 | 1,560.42 | 1,642.26 | 12 Nov 09:45 |
| supertrend_intraday | NSE:AXISBANK | 12 | 1,351.07 | 1,324.52 | 1,401.26 | 12 Nov 09:45 |
| supertrend_intraday | NSE:KOTAKBANK | 33 | 490.40 | 480.87 | 506.76 | 12 Nov 09:45 |
| ema_crossover | NSE:BHARTIARTL | 7 | 2,096.02 | 2,081.60 | 2,120.59 | 12 Nov 09:45 |
| ema_crossover | NSE:HDFCBANK | 20 | 810.96 | 804.77 | 823.16 | 12 Nov 10:00 |
| tv_rating_scalper | NSE:KOTAKBANK | 33 | 488.00 | 484.00 | 495.71 | 12 Nov 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 12 Nov 12:30 | tv_rating_scalper | SELL | 12 | NSE:AXISBANK | 1,334.73 | -146 | stop-loss |
| 12 Nov 12:20 | tv_rating_scalper | SELL | 56 | NSE:ITC | 285.79 | -146 | stop-loss |
| 12 Nov 10:00 | ema_crossover | BUY | 20 | NSE:HDFCBANK | 810.96 |  | EMA9>21, RSI 56 |
| 12 Nov 09:45 | supertrend_intraday | BUY | 33 | NSE:KOTAKBANK | 490.40 |  | Supertrend flipped up |
| 12 Nov 09:45 | supertrend_intraday | BUY | 12 | NSE:AXISBANK | 1,351.07 |  | Supertrend flipped up |
| 12 Nov 09:45 | supertrend_intraday | BUY | 10 | NSE:ICICIBANK | 1,590.32 |  | Supertrend flipped up |
| 12 Nov 09:45 | ema_crossover | BUY | 7 | NSE:BHARTIARTL | 2,096.02 |  | EMA9>21, RSI 58 |
| 12 Nov 09:30 | tv_rating_scalper | BUY | 12 | NSE:AXISBANK | 1,346.27 |  | TV 15m +0.51 / 1h +0.56 |
| 12 Nov 09:30 | tv_rating_scalper | BUY | 33 | NSE:KOTAKBANK | 488.00 |  | TV 15m +0.60 / 1h +0.60 |
| 12 Nov 09:30 | tv_rating_scalper | BUY | 56 | NSE:ITC | 288.26 |  | TV 15m +0.65 / 1h +0.56 |
| 11 Nov 15:15 | tv_rating_scalper | SELL | 12 | NSE:RELIANCE | 1,332.93 | -18 | intraday square-off |
| 11 Nov 15:15 | ema_crossover | SELL | 57 | NSE:ITC | 284.44 | +99 | intraday square-off |
| 11 Nov 13:30 | supertrend_intraday | SELL | 12 | NSE:AXISBANK | 1,339.73 | +36 | Supertrend reversed |
| 11 Nov 13:30 | supertrend_intraday | SELL | 14 | NSE:INFY | 1,147.67 | -212 | Supertrend reversed |
| 11 Nov 13:00 | supertrend_intraday | SELL | 6 | NSE:TCS | 2,462.01 | -208 | Supertrend reversed |
| 11 Nov 11:45 | tv_rating_scalper | SELL | 10 | NSE:ICICIBANK | 1,593.58 | -160 | stop-loss |
| 11 Nov 11:35 | tv_rating_scalper | SELL | 12 | NSE:AXISBANK | 1,351.43 | +247 | target |
| 11 Nov 10:15 | ema_crossover | SELL | 6 | NSE:TCS | 2,475.50 | -149 | stop-loss |
| 11 Nov 10:10 | ema_crossover | SELL | 14 | NSE:INFY | 1,160.37 | -125 | stop-loss |
| 11 Nov 10:00 | ema_crossover | BUY | 57 | NSE:ITC | 282.56 |  | EMA9>21, RSI 64 |
| 11 Nov 10:00 | ema_crossover | BUY | 6 | NSE:TCS | 2,499.10 |  | EMA9>21, RSI 66 |
| 11 Nov 10:00 | ema_crossover | BUY | 14 | NSE:INFY | 1,168.73 |  | EMA9>21, RSI 69 |
| 11 Nov 09:45 | supertrend_intraday | BUY | 12 | NSE:AXISBANK | 1,336.07 |  | Supertrend flipped up |
| 11 Nov 09:45 | supertrend_intraday | BUY | 6 | NSE:TCS | 2,495.50 |  | Supertrend flipped up |
| 11 Nov 09:45 | supertrend_intraday | BUY | 14 | NSE:INFY | 1,162.23 |  | Supertrend flipped up |
| 11 Nov 09:35 | ema_crossover | SELL | 12 | NSE:AXISBANK | 1,331.13 | -58 | target |
| 11 Nov 09:30 | tv_rating_scalper | BUY | 10 | NSE:ICICIBANK | 1,608.82 |  | TV 15m +0.65 / 1h +0.56 |
| 11 Nov 09:30 | ema_crossover | BUY | 12 | NSE:AXISBANK | 1,335.27 |  | EMA9>21, RSI 57 |
| 11 Nov 09:30 | ema_crossover | SELL | 12 | NSE:AXISBANK | 1,334.73 | +47 | target |
| 11 Nov 09:25 | tv_rating_scalper | BUY | 12 | NSE:AXISBANK | 1,330.17 |  | TV 15m +0.51 / 1h +0.38 |
