# Bot leaderboard

_Updated 09 Nov 2026 11:50 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **tv_rating_swing** | swing 1D | +11.62% | +5,810 | +200 | +0.86% | 1 | 0 | 0.00 | -2.3% | 3 | ok |
| 2 | **nifty_buy_hold** | benchmark 1D | +10.76% | +5,378 | +90 | +0.00% | 0 | – | – | -3.0% | 1 | ok |
| 3 | **momentum_rotation** | positional 1D | +8.13% | +4,065 | -223 | -2.63% | 1 | 100 | ∞ | -4.4% | 3 | ok |
| 4 | **dual_momentum** | positional 1D | +7.66% | +3,832 | +474 | -3.09% | 0 | – | – | -0.7% | 1 | ok |
| 5 | **supertrend_intraday** | intraday 15m | +1.47% | +735 | +0 | -9.29% | 33 | 45 | 1.50 | -2.5% | 0 | ok |
| 6 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -10.76% | 0 | – | – | 0.0% | 0 | ok |
| 7 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -10.76% | 0 | – | – | 0.0% | 0 | ok |
| 8 | **ema_crossover** | intraday 15m | -0.75% | -374 | +0 | -11.50% | 51 | 37 | 1.01 | -3.6% | 0 | ok |
| 9 | **tv_rating_scalper** | intraday 15m | -1.06% | -530 | -303 | -11.82% | 81 | 40 | 1.00 | -5.8% | 2 | ok |
| 10 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | -490 | -8.53% | 5 | 60 | 4.63 | -0.9% | 0 | retired |
| 11 | **gap_and_go** | intraday 15m | +1.40% | +701 | -391 | -9.35% | 10 | 80 | 2.36 | -1.2% | 0 | retired |
| 12 | **vwap_pullback** | intraday 15m | +0.98% | +491 | +32 | -9.77% | 41 | 51 | 1.48 | -1.7% | 0 | retired |
| 13 | **donchian_turtle** | swing 1D | +0.79% | +395 | +0 | -9.97% | 3 | 67 | 2.04 | -2.5% | 0 | retired |
| 14 | **orb_breakout** | intraday 15m | +0.54% | +272 | -11 | -10.21% | 15 | 60 | 1.51 | -1.5% | 0 | retired |
| 15 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -10.76% | 0 | – | – | 0.0% | 0 | retired |
| 16 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -10.76% | 0 | – | – | 0.0% | 0 | retired |
| 17 | **vwap_reversion** | intraday 15m | -0.33% | -166 | +151 | -11.09% | 35 | 57 | 1.09 | -1.3% | 0 | retired |
| 18 | **bb_squeeze** | intraday 15m | -0.98% | -492 | -413 | -11.74% | 20 | 40 | 0.68 | -1.4% | 0 | retired |
| 19 | **macd_adx** | intraday 15m | -1.02% | -512 | -178 | -11.78% | 22 | 32 | 0.71 | -1.4% | 0 | retired |
| 20 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | -554 | -12.29% | 35 | 49 | 0.61 | -1.5% | 0 | retired |
| 21 | **crypto_supertrend** | crypto 1h | -8.03% | -4,014 | -495 | -18.78% | 13 | 15 | 0.05 | -8.1% | 0 | retired |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| dual_momentum | Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash |
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
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,719.76 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,475.35 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:DRREDDY | 13 | 1,241.85 | 1,291.40 | – | 19 Oct 15:05 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:DRREDDY | 12 | 1,365.27 | 1,201.20 | – | 04 Nov 15:10 |
| dual_momentum | NSE:BANKBEES | 86 | 569.32 | – | – | 02 Nov 15:10 |
| tv_rating_scalper | NSE:SUNPHARMA | 8 | 1,915.38 | 1,899.68 | 1,945.64 | 09 Nov 09:15 |
| tv_rating_scalper | NSE:SBIN | 15 | 1,031.51 | 1,023.05 | 1,047.80 | 09 Nov 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 09 Nov 10:55 | tv_rating_scalper | SELL | 20 | NSE:HDFCBANK | 787.39 | -176 | stop-loss |
| 09 Nov 09:30 | tv_rating_scalper | BUY | 15 | NSE:SBIN | 1,031.51 |  | TV 15m +0.56 / 1h +0.60 |
| 09 Nov 09:30 | tv_rating_scalper | BUY | 20 | NSE:HDFCBANK | 795.81 |  | TV 15m +0.60 / 1h +0.60 |
| 09 Nov 09:30 | tv_rating_scalper | SELL | 14 | NSE:INFY | 1,153.27 | -268 | stop-loss |
| 09 Nov 09:15 | tv_rating_scalper | BUY | 8 | NSE:SUNPHARMA | 1,915.38 |  | TV 15m +0.54 / 1h +0.56 |
| 09 Nov 09:15 | tv_rating_scalper | BUY | 14 | NSE:INFY | 1,171.83 |  | TV 15m +0.54 / 1h +0.60 |
| 06 Nov 12:55 | tv_rating_scalper | SELL | 10 | NSE:ICICIBANK | 1,537.99 | +239 | target |
| 06 Nov 11:35 | ema_crossover | SELL | 58 | NSE:ITC | 279.04 | -131 | stop-loss |
| 06 Nov 11:15 | tv_rating_scalper | SELL | 6 | NSE:TCS | 2,508.60 | -161 | stop-loss |
| 06 Nov 10:55 | tv_rating_scalper | SELL | 13 | NSE:INFY | 1,178.66 | -171 | stop-loss |
| 06 Nov 10:15 | ema_crossover | BUY | 58 | NSE:ITC | 281.16 |  | EMA9>21, RSI 65 |
| 06 Nov 09:30 | tv_rating_scalper | BUY | 6 | NSE:TCS | 2,534.21 |  | TV 15m +0.65 / 1h +0.65 |
| 06 Nov 09:30 | tv_rating_scalper | BUY | 10 | NSE:ICICIBANK | 1,513.30 |  | TV 15m +0.65 / 1h +0.45 |
| 06 Nov 09:30 | tv_rating_scalper | BUY | 13 | NSE:INFY | 1,191.24 |  | TV 15m +0.69 / 1h +0.60 |
| 06 Nov 09:30 | tv_rating_scalper | SELL | 4 | NSE:LT | 4,008.80 | -72 | 15m rating faded (-0.16) |
| 06 Nov 09:25 | tv_rating_scalper | BUY | 4 | NSE:LT | 4,024.80 |  | TV 15m +0.51 / 1h +0.45 |
| 05 Nov 15:15 | supertrend_intraday | SELL | 6 | NSE:TCS | 2,498.00 | +101 | intraday square-off |
| 05 Nov 15:15 | supertrend_intraday | SELL | 14 | NSE:INFY | 1,162.87 | +137 | intraday square-off |
| 05 Nov 15:15 | supertrend_intraday | SELL | 11 | NSE:ICICIBANK | 1,498.20 | +451 | intraday square-off |
| 05 Nov 15:15 | ema_crossover | SELL | 4 | NSE:LT | 4,042.39 | +2 | intraday square-off |
| 05 Nov 14:50 | tv_rating_scalper | SELL | 12 | NSE:AXISBANK | 1,282.84 | +253 | target |
| 05 Nov 12:45 | tv_rating_scalper | SELL | 11 | NSE:ICICIBANK | 1,477.00 | +264 | target |
| 05 Nov 12:30 | ema_crossover | SELL | 6 | NSE:TCS | 2,475.50 | -157 | stop-loss |
| 05 Nov 11:10 | tv_rating_scalper | SELL | 21 | NSE:HDFCBANK | 749.80 | -148 | stop-loss |
| 05 Nov 10:10 | ema_crossover | SELL | 14 | NSE:INFY | 1,169.37 | +239 | target |
| 05 Nov 10:00 | ema_crossover | BUY | 6 | NSE:TCS | 2,500.40 |  | EMA9>21, RSI 71 |
| 05 Nov 09:45 | supertrend_intraday | BUY | 6 | NSE:TCS | 2,480.00 |  | Supertrend flipped up |
| 05 Nov 09:45 | supertrend_intraday | BUY | 14 | NSE:INFY | 1,152.53 |  | Supertrend flipped up |
| 05 Nov 09:45 | supertrend_intraday | BUY | 11 | NSE:ICICIBANK | 1,456.49 |  | Supertrend flipped up |
| 05 Nov 09:45 | ema_crossover | BUY | 4 | NSE:LT | 4,039.81 |  | EMA9>21, RSI 78 |
