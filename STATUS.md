# Bot leaderboard

_Updated 16 Nov 2026 14:15 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **nifty_buy_hold** | benchmark 1D | +11.80% | +5,900 | +146 | +0.00% | 0 | – | – | -3.0% | 1 | ok |
| 2 | **dual_momentum** | positional 1D | +11.20% | +5,598 | +371 | -0.61% | 0 | – | – | -1.2% | 1 | ok |
| 3 | **tv_rating_swing** | swing 1D | +10.50% | +5,249 | -35 | -1.30% | 1 | 0 | 0.00 | -2.5% | 3 | ok |
| 4 | **momentum_rotation** | positional 1D | +9.41% | +4,704 | +236 | -2.39% | 2 | 100 | ∞ | -4.4% | 3 | ok |
| 5 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -11.80% | 0 | – | – | 0.0% | 0 | ok |
| 6 | **bb_reversion_daily** | swing 1D | -0.26% | -130 | -259 | -12.06% | 0 | – | – | -0.7% | 1 | ok |
| 7 | **supertrend_intraday** | intraday 15m | -1.00% | -499 | -313 | -12.80% | 42 | 38 | 1.00 | -3.2% | 2 | ok |
| 8 | **ema_crossover** | intraday 15m | -1.76% | -880 | -71 | -13.56% | 64 | 38 | 0.90 | -3.9% | 0 | ok |
| 9 | **tv_rating_scalper** | intraday 15m | -2.04% | -1,022 | +337 | -13.85% | 97 | 38 | 0.95 | -5.8% | 2 | ok |
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
| dual_momentum | Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
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
| tv_rating_swing | NSE:DRREDDY | 13 | 1,241.85 | 1,305.35 | – | 19 Oct 15:05 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:DRREDDY | 12 | 1,365.27 | 1,201.20 | – | 04 Nov 15:10 |
| momentum_rotation | NSE:ETERNAL | 49 | 361.57 | 318.12 | – | 09 Nov 15:10 |
| bb_reversion_daily | NSE:TCS | 6 | 2,410.88 | 2,265.78 | – | 13 Nov 15:10 |
| supertrend_intraday | NSE:ICICIBANK | 10 | 1,586.02 | 1,562.21 | 1,608.37 | 16 Nov 09:25 |
| supertrend_intraday | NSE:SBIN | 14 | 1,097.07 | 1,076.85 | 1,134.89 | 16 Nov 09:45 |
| tv_rating_scalper | NSE:SBIN | 14 | 1,091.42 | 1,082.47 | 1,108.66 | 16 Nov 09:30 |
| tv_rating_scalper | NSE:HDFCBANK | 20 | 806.36 | 799.75 | 819.10 | 16 Nov 10:00 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 16 Nov 13:40 | supertrend_intraday | SELL | 14 | NSE:INFY | 1,138.97 | -153 | stop-loss |
| 16 Nov 12:15 | ema_crossover | SELL | 20 | NSE:HDFCBANK | 813.14 | +127 | target |
| 16 Nov 11:30 | ema_crossover | SELL | 12 | NSE:RELIANCE | 1,335.93 | -56 | opposite EMA cross |
| 16 Nov 11:00 | tv_rating_scalper | SELL | 11 | NSE:RELIANCE | 1,337.73 | -32 | 15m rating faded (-0.11) |
| 16 Nov 10:45 | ema_crossover | SELL | 14 | NSE:INFY | 1,147.17 | -129 | stop-loss |
| 16 Nov 10:00 | tv_rating_scalper | BUY | 20 | NSE:HDFCBANK | 806.36 |  | TV 15m +0.65 / 1h +0.38 |
| 16 Nov 10:00 | ema_crossover | BUY | 14 | NSE:INFY | 1,155.83 |  | EMA9>21, RSI 70 |
| 16 Nov 10:00 | ema_crossover | BUY | 20 | NSE:HDFCBANK | 806.36 |  | EMA9>21, RSI 62 |
| 16 Nov 09:50 | tv_rating_scalper | SELL | 7 | NSE:BHARTIARTL | 2,164.07 | +236 | target |
| 16 Nov 09:45 | supertrend_intraday | BUY | 14 | NSE:SBIN | 1,097.07 |  | Supertrend flipped up |
| 16 Nov 09:45 | supertrend_intraday | BUY | 14 | NSE:INFY | 1,149.33 |  | Supertrend flipped up |
| 16 Nov 09:30 | tv_rating_scalper | BUY | 14 | NSE:SBIN | 1,091.42 |  | TV 15m +0.69 / 1h +0.51 |
| 16 Nov 09:25 | tv_rating_scalper | BUY | 7 | NSE:BHARTIARTL | 2,129.23 |  | TV 15m +0.51 / 1h +0.54 |
| 16 Nov 09:25 | tv_rating_scalper | BUY | 11 | NSE:RELIANCE | 1,339.97 |  | TV 15m +0.51 / 1h +0.47 |
| 16 Nov 09:25 | supertrend_intraday | BUY | 10 | NSE:ICICIBANK | 1,586.02 |  | Supertrend flipped up |
| 16 Nov 09:25 | ema_crossover | BUY | 12 | NSE:RELIANCE | 1,339.97 |  | EMA9>21, RSI 56 |
| 13 Nov 15:15 | tv_rating_scalper | SELL | 7 | NSE:BHARTIARTL | 2,118.78 | +127 | intraday square-off |
| 13 Nov 15:10 | bb_reversion_daily | BUY | 6 | NSE:TCS | 2,410.88 |  | below lower band in uptrend |
| 13 Nov 14:05 | supertrend_intraday | SELL | 3 | NSE:LT | 4,132.27 | -179 | stop-loss |
| 13 Nov 12:55 | tv_rating_scalper | SELL | 11 | NSE:RELIANCE | 1,336.73 | -133 | stop-loss |
| 13 Nov 12:30 | ema_crossover | SELL | 12 | NSE:RELIANCE | 1,338.73 | -121 | stop-loss |
| 13 Nov 12:15 | tv_rating_scalper | SELL | 8 | NSE:SUNPHARMA | 1,892.42 | -73 | 15m rating faded (-0.07) |
| 13 Nov 12:15 | supertrend_intraday | SELL | 8 | NSE:SUNPHARMA | 1,892.42 | -73 | Supertrend reversed |
| 13 Nov 11:50 | ema_crossover | SELL | 14 | NSE:INFY | 1,142.57 | -118 | stop-loss |
| 13 Nov 11:50 | ema_crossover | SELL | 7 | NSE:BHARTIARTL | 2,112.28 | +132 | target |
| 13 Nov 10:30 | tv_rating_scalper | BUY | 7 | NSE:BHARTIARTL | 2,099.62 |  | TV 15m +0.56 / 1h +0.47 |
| 13 Nov 10:30 | tv_rating_scalper | BUY | 11 | NSE:RELIANCE | 1,348.17 |  | TV 15m +0.56 / 1h +0.56 |
| 13 Nov 10:30 | ema_crossover | BUY | 12 | NSE:RELIANCE | 1,348.17 |  | EMA9>21, RSI 65 |
| 13 Nov 10:15 | supertrend_intraday | BUY | 3 | NSE:LT | 4,189.74 |  | Supertrend flipped up |
| 13 Nov 10:00 | ema_crossover | BUY | 14 | NSE:INFY | 1,150.43 |  | EMA9>21, RSI 56 |
