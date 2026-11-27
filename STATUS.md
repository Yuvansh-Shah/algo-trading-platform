# Bot leaderboard

_Updated 27 Nov 2026 11:05 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **dual_momentum** | positional 1D | +15.23% | +7,617 | +7 | +0.87% | 0 | – | – | -3.6% | 1 | ok |
| 2 | **nifty_buy_hold** | benchmark 1D | +14.37% | +7,183 | -240 | +0.00% | 0 | – | – | -3.0% | 1 | ok |
| 3 | **tv_rating_swing** | swing 1D | +10.61% | +5,305 | -178 | -3.76% | 2 | 50 | 1.86 | -2.8% | 3 | ok |
| 4 | **momentum_rotation** | positional 1D | +10.30% | +5,151 | -136 | -4.06% | 3 | 100 | ∞ | -4.4% | 3 | ok |
| 5 | **bb_reversion_daily** | swing 1D | +0.47% | +236 | +0 | -13.89% | 1 | 100 | ∞ | -1.5% | 0 | ok |
| 6 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -14.37% | 0 | – | – | 0.0% | 0 | ok |
| 7 | **ema_crossover** | intraday 15m | -1.61% | -807 | +0 | -15.98% | 76 | 39 | 0.95 | -4.4% | 0 | ok |
| 8 | **tv_rating_scalper** | intraday 15m | -2.19% | -1,094 | -535 | -16.55% | 130 | 40 | 0.99 | -5.8% | 0 | ok |
| 9 | **supertrend_intraday** | intraday 15m | -2.22% | -1,108 | +0 | -16.58% | 56 | 38 | 0.83 | -4.7% | 0 | ok |
| 10 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | +0 | -12.14% | 5 | 60 | 4.63 | -0.9% | 0 | retired |
| 11 | **gap_and_go** | intraday 15m | +1.40% | +701 | +0 | -12.96% | 10 | 80 | 2.36 | -1.2% | 0 | retired |
| 12 | **vwap_pullback** | intraday 15m | +0.98% | +491 | +0 | -13.38% | 41 | 51 | 1.48 | -1.7% | 0 | retired |
| 13 | **donchian_turtle** | swing 1D | +0.79% | +395 | +0 | -13.58% | 3 | 67 | 2.04 | -2.5% | 0 | retired |
| 14 | **orb_breakout** | intraday 15m | +0.54% | +272 | +0 | -13.82% | 15 | 60 | 1.51 | -1.5% | 0 | retired |
| 15 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -14.37% | 0 | – | – | 0.0% | 0 | retired |
| 16 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -14.37% | 0 | – | – | 0.0% | 0 | retired |
| 17 | **vwap_reversion** | intraday 15m | -0.33% | -166 | +0 | -14.70% | 35 | 57 | 1.09 | -1.3% | 0 | retired |
| 18 | **bb_squeeze** | intraday 15m | -0.98% | -492 | +0 | -15.35% | 20 | 40 | 0.68 | -1.4% | 0 | retired |
| 19 | **macd_adx** | intraday 15m | -1.02% | -512 | +0 | -15.39% | 22 | 32 | 0.71 | -1.4% | 0 | retired |
| 20 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | +0 | -15.90% | 35 | 49 | 0.61 | -1.5% | 0 | retired |
| 21 | **crypto_supertrend** | crypto 1h | -8.03% | -4,014 | +0 | -22.39% | 13 | 15 | 0.05 | -8.1% | 0 | retired |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| dual_momentum | Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| ema_crossover | EMA 9/21 cross + RSI + VWAP, with the NIFTY trend, entries before 11:00; 1.5/3 ATR |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement, with the NIFTY trend, entries before 11:00 |
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

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 27 Nov 10:30 | tv_rating_scalper | SELL | 14 | NSE:SBIN | 1,141.47 | -65 | 15m rating faded (-0.20) |
| 27 Nov 10:00 | tv_rating_scalper | BUY | 14 | NSE:SBIN | 1,145.53 |  | TV 15m +0.56 / 1h +0.35 |
| 27 Nov 09:35 | tv_rating_scalper | SELL | 13 | NSE:INFY | 1,159.47 | -265 | stop-loss |
| 27 Nov 09:30 | tv_rating_scalper | SELL | 32 | NSE:KOTAKBANK | 507.25 | +29 | 15m rating faded (-0.36) |
| 27 Nov 09:30 | tv_rating_scalper | SELL | 6 | NSE:TCS | 2,592.48 | -235 | stop-loss |
| 27 Nov 09:25 | tv_rating_scalper | BUY | 32 | NSE:KOTAKBANK | 506.10 |  | TV 15m +0.56 / 1h +0.51 |
| 27 Nov 09:25 | tv_rating_scalper | BUY | 6 | NSE:TCS | 2,630.43 |  | TV 15m +0.56 / 1h +0.56 |
| 27 Nov 09:25 | tv_rating_scalper | BUY | 13 | NSE:INFY | 1,179.24 |  | TV 15m +0.56 / 1h +0.60 |
| 26 Nov 15:15 | tv_rating_scalper | SELL | 13 | NSE:INFY | 1,177.96 | +241 | target |
| 26 Nov 15:10 | tv_rating_scalper | SELL | 6 | NSE:TCS | 2,603.68 | +246 | target |
| 26 Nov 15:00 | ema_crossover | SELL | 11 | NSE:RELIANCE | 1,400.12 | +240 | target |
| 26 Nov 11:20 | tv_rating_scalper | SELL | 8 | NSE:SUNPHARMA | 1,923.92 | +243 | target |
| 26 Nov 11:15 | ema_crossover | SELL | 9 | NSE:ICICIBANK | 1,629.37 | -56 | opposite EMA cross |
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
