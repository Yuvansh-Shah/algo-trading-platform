# Bot leaderboard

_Updated 19 Nov 2026 15:25 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **dual_momentum** | positional 1D | +14.24% | +7,121 | +1,026 | +1.17% | 0 | – | – | -1.2% | 1 | ok |
| 2 | **nifty_buy_hold** | benchmark 1D | +13.07% | +6,534 | +540 | +0.00% | 0 | – | – | -3.0% | 1 | ok |
| 3 | **tv_rating_swing** | swing 1D | +10.41% | +5,207 | -162 | -2.65% | 2 | 50 | 1.86 | -2.8% | 3 | ok |
| 4 | **momentum_rotation** | positional 1D | +10.18% | +5,092 | +477 | -2.88% | 2 | 100 | ∞ | -4.4% | 3 | ok |
| 5 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -13.07% | 0 | – | – | 0.0% | 0 | ok |
| 6 | **bb_reversion_daily** | swing 1D | -0.84% | -420 | -140 | -13.91% | 0 | – | – | -1.4% | 1 | ok |
| 7 | **supertrend_intraday** | intraday 15m | -0.90% | -451 | +132 | -13.97% | 49 | 41 | 0.98 | -3.4% | 0 | ok |
| 8 | **ema_crossover** | intraday 15m | -1.24% | -622 | +0 | -14.31% | 68 | 40 | 0.98 | -3.9% | 0 | ok |
| 9 | **tv_rating_scalper** | intraday 15m | -2.03% | -1,017 | -8 | -15.10% | 111 | 40 | 0.98 | -5.8% | 0 | ok |
| 10 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | +0 | -10.84% | 5 | 60 | 4.63 | -0.9% | 0 | retired |
| 11 | **gap_and_go** | intraday 15m | +1.40% | +701 | +0 | -11.67% | 10 | 80 | 2.36 | -1.2% | 0 | retired |
| 12 | **vwap_pullback** | intraday 15m | +0.98% | +491 | +0 | -12.09% | 41 | 51 | 1.48 | -1.7% | 0 | retired |
| 13 | **donchian_turtle** | swing 1D | +0.79% | +395 | +0 | -12.28% | 3 | 67 | 2.04 | -2.5% | 0 | retired |
| 14 | **orb_breakout** | intraday 15m | +0.54% | +272 | +0 | -12.52% | 15 | 60 | 1.51 | -1.5% | 0 | retired |
| 15 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -13.07% | 0 | – | – | 0.0% | 0 | retired |
| 16 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -13.07% | 0 | – | – | 0.0% | 0 | retired |
| 17 | **vwap_reversion** | intraday 15m | -0.33% | -166 | +0 | -13.40% | 35 | 57 | 1.09 | -1.3% | 0 | retired |
| 18 | **bb_squeeze** | intraday 15m | -0.98% | -492 | +0 | -14.05% | 20 | 40 | 0.68 | -1.4% | 0 | retired |
| 19 | **macd_adx** | intraday 15m | -1.02% | -512 | +0 | -14.09% | 22 | 32 | 0.71 | -1.4% | 0 | retired |
| 20 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | +0 | -14.60% | 35 | 49 | 0.61 | -1.5% | 0 | retired |
| 21 | **crypto_supertrend** | crypto 1h | -8.03% | -4,014 | +0 | -21.10% | 13 | 15 | 0.05 | -8.1% | 0 | retired |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| dual_momentum | Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
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
| dual_momentum | NSE:BANKBEES | 86 | 569.32 | – | – | 02 Nov 15:10 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,502.88 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:DRREDDY | 13 | 1,241.85 | 1,305.35 | – | 19 Oct 15:05 |
| tv_rating_swing | NSE:EICHERMOT | 2 | 8,044.61 | 7,474.87 | – | 19 Nov 15:05 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:DRREDDY | 12 | 1,365.27 | 1,201.20 | – | 04 Nov 15:10 |
| momentum_rotation | NSE:ETERNAL | 49 | 361.57 | 318.12 | – | 09 Nov 15:10 |
| bb_reversion_daily | NSE:TCS | 6 | 2,410.88 | 2,265.78 | – | 13 Nov 15:10 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
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
| 18 Nov 10:00 | tv_rating_scalper | SELL | 14 | NSE:SBIN | 1,105.93 | -127 | 15m rating faded (-0.05) |
| 18 Nov 09:30 | tv_rating_scalper | BUY | 14 | NSE:SBIN | 1,114.47 |  | TV 15m +0.60 / 1h +0.51 |
| 18 Nov 09:30 | tv_rating_scalper | SELL | 11 | NSE:AXISBANK | 1,366.53 | -37 | 15m rating faded (-0.02) |
| 18 Nov 09:25 | tv_rating_scalper | BUY | 11 | NSE:AXISBANK | 1,369.17 |  | TV 15m +0.51 / 1h +0.45 |
| 17 Nov 15:15 | tv_rating_scalper | SELL | 10 | NSE:ICICIBANK | 1,607.48 | +75 | intraday square-off |
| 17 Nov 15:15 | tv_rating_scalper | SELL | 32 | NSE:KOTAKBANK | 496.00 | +32 | intraday square-off |
| 17 Nov 15:15 | supertrend_intraday | SELL | 8 | NSE:SUNPHARMA | 1,871.33 | -52 | intraday square-off |
| 17 Nov 15:15 | supertrend_intraday | SELL | 3 | NSE:LT | 4,174.36 | +28 | intraday square-off |
| 17 Nov 15:15 | ema_crossover | SELL | 10 | NSE:ICICIBANK | 1,607.48 | +75 | intraday square-off |
| 17 Nov 13:30 | supertrend_intraday | SELL | 6 | NSE:TCS | 2,415.82 | +25 | Supertrend reversed |
| 17 Nov 12:30 | tv_rating_scalper | SELL | 11 | NSE:AXISBANK | 1,370.43 | +231 | target |
| 17 Nov 12:15 | ema_crossover | SELL | 11 | NSE:AXISBANK | 1,368.13 | +154 | target |
