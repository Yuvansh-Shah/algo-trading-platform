# Bot leaderboard

_Updated 20 Nov 2026 14:35 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **dual_momentum** | positional 1D | +17.05% | +8,527 | +1,410 | +2.84% | 0 | – | – | -1.2% | 1 | ok |
| 2 | **nifty_buy_hold** | benchmark 1D | +14.21% | +7,106 | +589 | +0.00% | 0 | – | – | -3.0% | 1 | ok |
| 3 | **tv_rating_swing** | swing 1D | +11.43% | +5,716 | +735 | -2.78% | 2 | 50 | 1.86 | -2.8% | 3 | ok |
| 4 | **momentum_rotation** | positional 1D | +10.48% | +5,241 | +453 | -3.73% | 2 | 100 | ∞ | -4.4% | 3 | ok |
| 5 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -14.21% | 0 | – | – | 0.0% | 0 | ok |
| 6 | **bb_reversion_daily** | swing 1D | -0.41% | -203 | +328 | -14.62% | 0 | – | – | -1.5% | 1 | ok |
| 7 | **tv_rating_scalper** | intraday 15m | -0.65% | -326 | +722 | -14.86% | 115 | 41 | 1.08 | -5.8% | 0 | ok |
| 8 | **supertrend_intraday** | intraday 15m | -0.75% | -375 | +87 | -14.96% | 49 | 41 | 0.98 | -3.4% | 2 | ok |
| 9 | **ema_crossover** | intraday 15m | -1.53% | -766 | -143 | -15.74% | 69 | 39 | 0.95 | -3.9% | 0 | ok |
| 10 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | +0 | -11.98% | 5 | 60 | 4.63 | -0.9% | 0 | retired |
| 11 | **gap_and_go** | intraday 15m | +1.40% | +701 | +0 | -12.81% | 10 | 80 | 2.36 | -1.2% | 0 | retired |
| 12 | **vwap_pullback** | intraday 15m | +0.98% | +491 | +0 | -13.23% | 41 | 51 | 1.48 | -1.7% | 0 | retired |
| 13 | **donchian_turtle** | swing 1D | +0.79% | +395 | +0 | -13.42% | 3 | 67 | 2.04 | -2.5% | 0 | retired |
| 14 | **orb_breakout** | intraday 15m | +0.54% | +272 | +0 | -13.67% | 15 | 60 | 1.51 | -1.5% | 0 | retired |
| 15 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -14.21% | 0 | – | – | 0.0% | 0 | retired |
| 16 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -14.21% | 0 | – | – | 0.0% | 0 | retired |
| 17 | **vwap_reversion** | intraday 15m | -0.33% | -166 | +0 | -14.54% | 35 | 57 | 1.09 | -1.3% | 0 | retired |
| 18 | **bb_squeeze** | intraday 15m | -0.98% | -492 | +0 | -15.20% | 20 | 40 | 0.68 | -1.4% | 0 | retired |
| 19 | **macd_adx** | intraday 15m | -1.02% | -512 | +0 | -15.24% | 22 | 32 | 0.71 | -1.4% | 0 | retired |
| 20 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | +0 | -15.74% | 35 | 49 | 0.61 | -1.5% | 0 | retired |
| 21 | **crypto_supertrend** | crypto 1h | -8.03% | -4,014 | +0 | -22.24% | 13 | 15 | 0.05 | -8.1% | 0 | retired |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| dual_momentum | Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement, with the NIFTY trend, entries before 11:00 |
| supertrend_intraday | Supertrend 10/3 flips on 15m with the NIFTY trend, entries before 11:00; 2R |
| ema_crossover | EMA 9/21 cross + RSI + VWAP, with the NIFTY trend, entries before 11:00; 1.5/3 ATR |
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
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,525.66 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:DRREDDY | 13 | 1,241.85 | 1,305.35 | – | 19 Oct 15:05 |
| tv_rating_swing | NSE:EICHERMOT | 2 | 8,044.61 | 7,569.27 | – | 19 Nov 15:05 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:DRREDDY | 12 | 1,365.27 | 1,201.20 | – | 04 Nov 15:10 |
| momentum_rotation | NSE:ETERNAL | 49 | 361.57 | 318.12 | – | 09 Nov 15:10 |
| bb_reversion_daily | NSE:TCS | 6 | 2,410.88 | 2,265.78 | – | 13 Nov 15:10 |
| supertrend_intraday | NSE:INFY | 15 | 1,087.22 | 1,076.22 | 1,123.26 | 20 Nov 09:25 |
| supertrend_intraday | NSE:TCS | 6 | 2,381.48 | 2,331.20 | 2,483.61 | 20 Nov 09:45 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 20 Nov 14:30 | ema_crossover | SELL | 14 | NSE:INFY | 1,095.58 | -136 | opposite EMA cross |
| 20 Nov 12:40 | tv_rating_scalper | SELL | 32 | NSE:KOTAKBANK | 510.95 | +269 | target |
| 20 Nov 12:15 | tv_rating_scalper | SELL | 10 | NSE:ICICIBANK | 1,627.47 | +243 | target |
| 20 Nov 11:05 | tv_rating_scalper | SELL | 11 | NSE:AXISBANK | 1,397.52 | +259 | target |
| 20 Nov 09:45 | supertrend_intraday | BUY | 6 | NSE:TCS | 2,381.48 |  | Supertrend flipped up |
| 20 Nov 09:45 | ema_crossover | BUY | 14 | NSE:INFY | 1,104.72 |  | EMA9>21, RSI 67 |
| 20 Nov 09:30 | tv_rating_scalper | BUY | 32 | NSE:KOTAKBANK | 502.30 |  | TV 15m +0.51 / 1h +0.35 |
| 20 Nov 09:30 | tv_rating_scalper | SELL | 3 | NSE:LT | 4,140.17 | -50 | 15m rating faded (-0.49) |
| 20 Nov 09:25 | tv_rating_scalper | BUY | 10 | NSE:ICICIBANK | 1,602.32 |  | TV 15m +0.54 / 1h +0.42 |
| 20 Nov 09:25 | tv_rating_scalper | BUY | 3 | NSE:LT | 4,154.73 |  | TV 15m +0.60 / 1h +0.56 |
| 20 Nov 09:25 | tv_rating_scalper | BUY | 11 | NSE:AXISBANK | 1,373.27 |  | TV 15m +0.60 / 1h +0.51 |
| 20 Nov 09:25 | supertrend_intraday | BUY | 15 | NSE:INFY | 1,087.22 |  | Supertrend flipped up |
| 19 Nov 15:15 | tv_rating_scalper | SELL | 53 | NSE:ITC | 300.84 | +126 | intraday square-off |
| 19 Nov 15:15 | tv_rating_scalper | SELL | 8 | NSE:SUNPHARMA | 1,904.72 | +147 | intraday square-off |
| 19 Nov 15:15 | tv_rating_scalper | SELL | 7 | NSE:BHARTIARTL | 2,151.77 | +40 | intraday square-off |
| 19 Nov 15:15 | supertrend_intraday | SELL | 8 | NSE:SUNPHARMA | 1,904.72 | +107 | intraday square-off |
| 19 Nov 15:15 | supertrend_intraday | SELL | 7 | NSE:BHARTIARTL | 2,151.77 | +40 | intraday square-off |
| 19 Nov 15:05 | tv_rating_swing | BUY | 2 | NSE:EICHERMOT | 8,044.61 |  | TV STRONG BUY +0.65, RSI 69 |
| 19 Nov 11:00 | tv_rating_scalper | BUY | 53 | NSE:ITC | 298.31 |  | TV 15m +0.51 / 1h +0.49 |
| 19 Nov 10:45 | tv_rating_scalper | SELL | 11 | NSE:AXISBANK | 1,359.53 | -76 | 15m rating faded (-0.25) |
| 19 Nov 10:30 | supertrend_intraday | BUY | 8 | NSE:SUNPHARMA | 1,890.38 |  | Supertrend flipped up |
| 19 Nov 10:15 | tv_rating_scalper | BUY | 8 | NSE:SUNPHARMA | 1,885.38 |  | TV 15m +0.51 / 1h +0.47 |
| 19 Nov 10:15 | tv_rating_scalper | BUY | 11 | NSE:AXISBANK | 1,365.77 |  | TV 15m +0.54 / 1h +0.31 |
| 19 Nov 09:45 | tv_rating_swing | SELL | 10 | NSE:TECHM | 1,711.76 | +1,306 | stop-loss |
| 19 Nov 09:45 | tv_rating_scalper | BUY | 7 | NSE:BHARTIARTL | 2,145.03 |  | TV 15m +0.51 / 1h +0.49 |
| 19 Nov 09:45 | tv_rating_scalper | SELL | 8 | NSE:SUNPHARMA | 1,873.23 | -131 | 15m rating faded (-0.40) |
| 19 Nov 09:45 | tv_rating_scalper | SELL | 11 | NSE:RELIANCE | 1,355.73 | -78 | 15m rating faded (-0.34) |
| 19 Nov 09:45 | supertrend_intraday | BUY | 7 | NSE:BHARTIARTL | 2,145.03 |  | Supertrend flipped up |
| 19 Nov 09:30 | tv_rating_scalper | BUY | 8 | NSE:SUNPHARMA | 1,888.68 |  | TV 15m +0.56 / 1h +0.60 |
| 19 Nov 09:25 | tv_rating_scalper | BUY | 11 | NSE:RELIANCE | 1,362.17 |  | TV 15m +0.56 / 1h +0.47 |
