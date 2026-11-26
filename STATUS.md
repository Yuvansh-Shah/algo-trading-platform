# Bot leaderboard

_Updated 26 Nov 2026 11:00 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **dual_momentum** | positional 1D | +16.08% | +8,038 | +250 | +1.15% | 0 | – | – | -3.6% | 1 | ok |
| 2 | **nifty_buy_hold** | benchmark 1D | +14.93% | +7,465 | +284 | +0.00% | 0 | – | – | -3.0% | 1 | ok |
| 3 | **tv_rating_swing** | swing 1D | +11.98% | +5,991 | -277 | -2.95% | 2 | 50 | 1.86 | -2.8% | 3 | ok |
| 4 | **momentum_rotation** | positional 1D | +11.17% | +5,583 | +449 | -3.76% | 3 | 100 | ∞ | -4.4% | 3 | ok |
| 5 | **bb_reversion_daily** | swing 1D | +0.47% | +236 | +0 | -14.46% | 1 | 100 | ∞ | -1.5% | 0 | ok |
| 6 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -14.93% | 0 | – | – | 0.0% | 0 | ok |
| 7 | **tv_rating_scalper** | intraday 15m | -1.87% | -936 | +308 | -16.80% | 123 | 39 | 0.97 | -5.8% | 3 | ok |
| 8 | **ema_crossover** | intraday 15m | -2.04% | -1,022 | -46 | -16.97% | 74 | 39 | 0.91 | -4.4% | 2 | ok |
| 9 | **supertrend_intraday** | intraday 15m | -2.22% | -1,108 | +0 | -17.15% | 56 | 38 | 0.83 | -4.7% | 0 | ok |
| 10 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | +0 | -12.70% | 5 | 60 | 4.63 | -0.9% | 0 | retired |
| 11 | **gap_and_go** | intraday 15m | +1.40% | +701 | +0 | -13.53% | 10 | 80 | 2.36 | -1.2% | 0 | retired |
| 12 | **vwap_pullback** | intraday 15m | +0.98% | +491 | +0 | -13.95% | 41 | 51 | 1.48 | -1.7% | 0 | retired |
| 13 | **donchian_turtle** | swing 1D | +0.79% | +395 | +0 | -14.14% | 3 | 67 | 2.04 | -2.5% | 0 | retired |
| 14 | **orb_breakout** | intraday 15m | +0.54% | +272 | +0 | -14.39% | 15 | 60 | 1.51 | -1.5% | 0 | retired |
| 15 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -14.93% | 0 | – | – | 0.0% | 0 | retired |
| 16 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -14.93% | 0 | – | – | 0.0% | 0 | retired |
| 17 | **vwap_reversion** | intraday 15m | -0.33% | -166 | +0 | -15.26% | 35 | 57 | 1.09 | -1.3% | 0 | retired |
| 18 | **bb_squeeze** | intraday 15m | -0.98% | -492 | +0 | -15.91% | 20 | 40 | 0.68 | -1.4% | 0 | retired |
| 19 | **macd_adx** | intraday 15m | -1.02% | -512 | +0 | -15.95% | 22 | 32 | 0.71 | -1.4% | 0 | retired |
| 20 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | +0 | -16.46% | 35 | 49 | 0.61 | -1.5% | 0 | retired |
| 21 | **crypto_supertrend** | crypto 1h | -8.03% | -4,014 | +0 | -22.96% | 13 | 15 | 0.05 | -8.1% | 0 | retired |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| dual_momentum | Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement, with the NIFTY trend, entries before 11:00 |
| ema_crossover | EMA 9/21 cross + RSI + VWAP, with the NIFTY trend, entries before 11:00; 1.5/3 ATR |
| supertrend_intraday | Supertrend 10/3 flips on 15m with the NIFTY trend, entries before 11:00; 2R |
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
| dual_momentum | NSE:BANKBEES | 86 | 569.32 | – | – | 02 Nov 15:10 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,534.59 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:DRREDDY | 13 | 1,241.85 | 1,308.60 | – | 19 Oct 15:05 |
| tv_rating_swing | NSE:EICHERMOT | 2 | 8,044.61 | 7,767.36 | – | 19 Nov 15:05 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:DRREDDY | 12 | 1,365.27 | 1,201.20 | – | 04 Nov 15:10 |
| momentum_rotation | NSE:HDFCBANK | 21 | 849.22 | 747.16 | – | 20 Nov 15:10 |
| tv_rating_scalper | NSE:SUNPHARMA | 8 | 1,892.58 | 1,877.06 | 1,922.48 | 26 Nov 09:25 |
| tv_rating_scalper | NSE:TCS | 6 | 2,561.41 | 2,540.41 | 2,601.87 | 26 Nov 09:30 |
| tv_rating_scalper | NSE:INFY | 13 | 1,158.83 | 1,149.33 | 1,177.14 | 26 Nov 09:30 |
| ema_crossover | NSE:ICICIBANK | 9 | 1,634.83 | 1,621.93 | 1,657.25 | 26 Nov 10:45 |
| ema_crossover | NSE:RELIANCE | 11 | 1,377.58 | 1,367.81 | 1,396.88 | 26 Nov 11:00 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 26 Nov 11:00 | ema_crossover | BUY | 11 | NSE:RELIANCE | 1,377.58 |  | EMA9>21, RSI 58 |
| 26 Nov 10:45 | ema_crossover | BUY | 9 | NSE:ICICIBANK | 1,634.83 |  | EMA9>21, RSI 52 |
| 26 Nov 09:30 | tv_rating_scalper | BUY | 13 | NSE:INFY | 1,158.83 |  | TV 15m +0.60 / 1h +0.65 |
| 26 Nov 09:30 | tv_rating_scalper | BUY | 6 | NSE:TCS | 2,561.41 |  | TV 15m +0.65 / 1h +0.65 |
| 26 Nov 09:25 | tv_rating_scalper | BUY | 8 | NSE:SUNPHARMA | 1,892.58 |  | TV 15m +0.60 / 1h +0.56 |
| 25 Nov 15:15 | tv_rating_scalper | SELL | 6 | NSE:TCS | 2,503.40 | -48 | intraday square-off |
| 25 Nov 15:15 | supertrend_intraday | SELL | 9 | NSE:ICICIBANK | 1,637.67 | -15 | intraday square-off |
| 25 Nov 15:15 | supertrend_intraday | SELL | 19 | NSE:HDFCBANK | 841.63 | -116 | intraday square-off |
| 25 Nov 15:15 | supertrend_intraday | SELL | 11 | NSE:RELIANCE | 1,367.73 | -241 | intraday square-off |
| 25 Nov 15:15 | ema_crossover | SELL | 9 | NSE:ICICIBANK | 1,637.67 | +0 | intraday square-off |
| 25 Nov 15:15 | ema_crossover | SELL | 19 | NSE:HDFCBANK | 841.63 | -69 | intraday square-off |
| 25 Nov 13:00 | tv_rating_scalper | SELL | 31 | NSE:KOTAKBANK | 508.75 | -123 | 15m rating faded (-0.02) |
| 25 Nov 12:50 | tv_rating_scalper | SELL | 14 | NSE:INFY | 1,126.77 | -181 | stop-loss |
| 25 Nov 12:00 | ema_crossover | SELL | 11 | NSE:AXISBANK | 1,445.01 | +265 | target |
| 25 Nov 10:15 | ema_crossover | BUY | 11 | NSE:AXISBANK | 1,420.18 |  | EMA9>21, RSI 59 |
| 25 Nov 10:05 | ema_crossover | SELL | 11 | NSE:RELIANCE | 1,372.23 | -192 | stop-loss |
| 25 Nov 10:00 | ema_crossover | BUY | 9 | NSE:ICICIBANK | 1,636.83 |  | EMA9>21, RSI 66 |
| 25 Nov 10:00 | ema_crossover | BUY | 19 | NSE:HDFCBANK | 844.82 |  | EMA9>21, RSI 66 |
| 25 Nov 09:45 | supertrend_intraday | BUY | 9 | NSE:ICICIBANK | 1,638.53 |  | Supertrend flipped up |
| 25 Nov 09:45 | supertrend_intraday | BUY | 19 | NSE:HDFCBANK | 847.32 |  | Supertrend flipped up |
| 25 Nov 09:45 | supertrend_intraday | BUY | 11 | NSE:RELIANCE | 1,388.98 |  | Supertrend flipped up |
| 25 Nov 09:45 | ema_crossover | BUY | 11 | NSE:RELIANCE | 1,388.98 |  | EMA9>21, RSI 73 |
| 25 Nov 09:30 | tv_rating_scalper | BUY | 31 | NSE:KOTAKBANK | 512.45 |  | TV 15m +0.65 / 1h +0.60 |
| 25 Nov 09:30 | tv_rating_scalper | BUY | 6 | NSE:TCS | 2,510.20 |  | TV 15m +0.65 / 1h +0.60 |
| 25 Nov 09:30 | tv_rating_scalper | BUY | 14 | NSE:INFY | 1,139.13 |  | TV 15m +0.65 / 1h +0.65 |
| 23 Nov 15:10 | bb_reversion_daily | SELL | 6 | NSE:TCS | 2,455.51 | +252 | back to middle band |
| 23 Nov 12:30 | supertrend_intraday | SELL | 14 | NSE:INFY | 1,105.58 | -21 | Supertrend reversed |
| 23 Nov 12:10 | ema_crossover | SELL | 14 | NSE:INFY | 1,108.38 | -176 | stop-loss |
| 23 Nov 10:25 | supertrend_intraday | SELL | 11 | NSE:RELIANCE | 1,361.03 | -230 | stop-loss |
| 23 Nov 10:15 | tv_rating_scalper | SELL | 53 | NSE:ITC | 299.14 | -78 | 15m rating faded (-0.02) |
