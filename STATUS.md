# Bot leaderboard

_Updated 13 Nov 2026 10:15 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **nifty_buy_hold** | benchmark 1D | +11.80% | +5,900 | -157 | +0.00% | 0 | – | – | -3.0% | 1 | ok |
| 2 | **tv_rating_swing** | swing 1D | +11.47% | +5,735 | +440 | -0.33% | 1 | 0 | 0.00 | -2.4% | 3 | ok |
| 3 | **dual_momentum** | positional 1D | +10.67% | +5,336 | -379 | -1.13% | 0 | – | – | -1.2% | 1 | ok |
| 4 | **momentum_rotation** | positional 1D | +9.35% | +4,675 | +255 | -2.45% | 2 | 100 | ∞ | -4.4% | 3 | ok |
| 5 | **supertrend_intraday** | intraday 15m | +0.23% | +117 | +26 | -11.57% | 39 | 41 | 1.15 | -2.5% | 2 | ok |
| 6 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -11.80% | 0 | – | – | 0.0% | 0 | ok |
| 7 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -11.80% | 0 | – | – | 0.0% | 0 | ok |
| 8 | **ema_crossover** | intraday 15m | -1.41% | -707 | -40 | -13.21% | 58 | 38 | 0.94 | -3.6% | 2 | ok |
| 9 | **tv_rating_scalper** | intraday 15m | -2.40% | -1,202 | -203 | -14.20% | 92 | 38 | 0.93 | -5.8% | 1 | ok |
| 10 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | +0 | -9.57% | 5 | 60 | 4.63 | -0.9% | 0 | retired |
| 11 | **gap_and_go** | intraday 15m | +1.40% | +701 | +0 | -10.40% | 10 | 80 | 2.36 | -1.2% | 0 | retired |
| 12 | **vwap_pullback** | intraday 15m | +0.98% | +491 | +0 | -10.82% | 41 | 51 | 1.48 | -1.7% | 0 | retired |
| 13 | **donchian_turtle** | swing 1D | +0.79% | +395 | +0 | -11.01% | 3 | 67 | 2.04 | -2.5% | 0 | retired |
| 14 | **orb_breakout** | intraday 15m | +0.54% | +272 | +0 | -11.26% | 15 | 60 | 1.51 | -1.5% | 0 | retired |
| 15 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -11.80% | 0 | – | – | 0.0% | 0 | retired |
| 16 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -11.80% | 0 | – | – | 0.0% | 0 | retired |
| 17 | **vwap_reversion** | intraday 15m | -0.33% | -166 | +0 | -12.13% | 35 | 57 | 1.09 | -1.3% | 0 | retired |
| 18 | **bb_squeeze** | intraday 15m | -0.98% | -492 | +0 | -12.78% | 20 | 40 | 0.68 | -1.4% | 0 | retired |
| 19 | **macd_adx** | intraday 15m | -1.02% | -512 | +0 | -12.82% | 22 | 32 | 0.71 | -1.4% | 0 | retired |
| 20 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | +0 | -13.33% | 35 | 49 | 0.61 | -1.5% | 0 | retired |
| 21 | **crypto_supertrend** | crypto 1h | -8.03% | -4,014 | +0 | -19.83% | 13 | 15 | 0.05 | -8.1% | 0 | retired |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| dual_momentum | Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| supertrend_intraday | Supertrend 10/3 flips on 15m with the NIFTY trend, entries before 11:00; 2R |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
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
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,719.76 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,502.88 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:DRREDDY | 13 | 1,241.85 | 1,302.74 | – | 19 Oct 15:05 |
| dual_momentum | NSE:BANKBEES | 86 | 569.32 | – | – | 02 Nov 15:10 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:DRREDDY | 12 | 1,365.27 | 1,201.20 | – | 04 Nov 15:10 |
| momentum_rotation | NSE:ETERNAL | 49 | 361.57 | 318.12 | – | 09 Nov 15:10 |
| supertrend_intraday | NSE:SUNPHARMA | 8 | 1,900.58 | 1,880.74 | 1,944.83 | 13 Nov 09:45 |
| supertrend_intraday | NSE:LT | 3 | 4,189.74 | 4,136.60 | 4,282.70 | 13 Nov 10:15 |
| ema_crossover | NSE:BHARTIARTL | 7 | 2,092.42 | 2,081.94 | 2,112.41 | 13 Nov 09:45 |
| ema_crossover | NSE:INFY | 14 | 1,150.43 | 1,143.14 | 1,161.92 | 13 Nov 10:00 |
| tv_rating_scalper | NSE:SUNPHARMA | 8 | 1,900.58 | 1,885.00 | 1,930.60 | 13 Nov 09:45 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 13 Nov 10:15 | supertrend_intraday | BUY | 3 | NSE:LT | 4,189.74 |  | Supertrend flipped up |
| 13 Nov 10:00 | ema_crossover | BUY | 14 | NSE:INFY | 1,150.43 |  | EMA9>21, RSI 56 |
| 13 Nov 09:45 | tv_rating_scalper | BUY | 8 | NSE:SUNPHARMA | 1,900.58 |  | TV 15m +0.56 / 1h +0.45 |
| 13 Nov 09:45 | supertrend_intraday | BUY | 8 | NSE:SUNPHARMA | 1,900.58 |  | Supertrend flipped up |
| 13 Nov 09:45 | ema_crossover | BUY | 7 | NSE:BHARTIARTL | 2,092.42 |  | EMA9>21, RSI 54 |
| 13 Nov 09:40 | tv_rating_scalper | SELL | 14 | NSE:SBIN | 1,077.28 | -189 | stop-loss |
| 13 Nov 09:30 | tv_rating_scalper | SELL | 7 | NSE:BHARTIARTL | 2,085.08 | +11 | 15m rating faded (-0.29) |
| 13 Nov 09:30 | tv_rating_scalper | SELL | 32 | NSE:KOTAKBANK | 488.55 | -70 | 15m rating faded (-0.00) |
| 13 Nov 09:25 | tv_rating_scalper | BUY | 32 | NSE:KOTAKBANK | 490.50 |  | TV 15m +0.51 / 1h +0.38 |
| 13 Nov 09:25 | tv_rating_scalper | BUY | 7 | NSE:BHARTIARTL | 2,082.42 |  | TV 15m +0.56 / 1h +0.51 |
| 13 Nov 09:25 | tv_rating_scalper | BUY | 14 | NSE:SBIN | 1,090.22 |  | TV 15m +0.60 / 1h +0.40 |
| 12 Nov 15:15 | supertrend_intraday | SELL | 33 | NSE:KOTAKBANK | 489.65 | -33 | intraday square-off |
| 12 Nov 15:15 | supertrend_intraday | SELL | 12 | NSE:AXISBANK | 1,340.43 | -136 | intraday square-off |
| 12 Nov 15:15 | supertrend_intraday | SELL | 10 | NSE:ICICIBANK | 1,586.68 | -44 | intraday square-off |
| 12 Nov 15:15 | ema_crossover | SELL | 20 | NSE:HDFCBANK | 811.59 | +4 | intraday square-off |
| 12 Nov 13:15 | tv_rating_scalper | SELL | 33 | NSE:KOTAKBANK | 486.65 | -52 | 15m rating faded (-0.09) |
| 12 Nov 13:15 | ema_crossover | SELL | 7 | NSE:BHARTIARTL | 2,089.08 | -56 | opposite EMA cross |
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
