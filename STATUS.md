# Bot leaderboard

_Updated 29 Oct 2026 10:20 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **momentum_rotation** | positional 1D | +5.74% | +2,870 | +85 | +4.50% | 0 | – | – | -4.4% | 3 | ok |
| 2 | **tv_rating_swing** | swing 1D | +4.91% | +2,456 | -37 | +3.67% | 1 | 0 | 0.00 | -2.3% | 3 | ok |
| 3 | **nifty_buy_hold** | benchmark 1D | +1.24% | +620 | +60 | +0.00% | 0 | – | – | -3.0% | 1 | ok |
| 4 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -1.24% | 0 | – | – | 0.0% | 0 | ok |
| 5 | **dual_momentum** | positional 1D | +0.00% | +0 | +0 | -1.24% | 0 | – | – | 0.0% | 0 | ok |
| 6 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -1.24% | 0 | – | – | 0.0% | 0 | ok |
| 7 | **supertrend_intraday** | intraday 15m | -0.10% | -52 | +0 | -1.34% | 23 | 39 | 1.09 | -2.4% | 0 | ok |
| 8 | **ema_crossover** | intraday 15m | -1.22% | -612 | +0 | -2.46% | 39 | 33 | 0.87 | -3.6% | 0 | ok |
| 9 | **tv_rating_scalper** | intraday 15m | -2.94% | -1,468 | -91 | -4.18% | 53 | 36 | 0.75 | -5.2% | 1 | ok |
| 10 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | -490 | +0.99% | 5 | 60 | 4.63 | -0.9% | 0 | retired |
| 11 | **gap_and_go** | intraday 15m | +1.40% | +701 | -391 | +0.16% | 10 | 80 | 2.36 | -1.2% | 0 | retired |
| 12 | **vwap_pullback** | intraday 15m | +0.98% | +491 | +32 | -0.26% | 41 | 51 | 1.48 | -1.7% | 0 | retired |
| 13 | **donchian_turtle** | swing 1D | +0.79% | +395 | +0 | -0.45% | 3 | 67 | 2.04 | -2.5% | 0 | retired |
| 14 | **orb_breakout** | intraday 15m | +0.54% | +272 | -11 | -0.70% | 15 | 60 | 1.51 | -1.5% | 0 | retired |
| 15 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -1.24% | 0 | – | – | 0.0% | 0 | retired |
| 16 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -1.24% | 0 | – | – | 0.0% | 0 | retired |
| 17 | **vwap_reversion** | intraday 15m | -0.33% | -166 | +151 | -1.57% | 35 | 57 | 1.09 | -1.3% | 0 | retired |
| 18 | **bb_squeeze** | intraday 15m | -0.98% | -492 | -413 | -2.22% | 20 | 40 | 0.68 | -1.4% | 0 | retired |
| 19 | **macd_adx** | intraday 15m | -1.02% | -512 | -178 | -2.26% | 22 | 32 | 0.71 | -1.4% | 0 | retired |
| 20 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | -554 | -2.77% | 35 | 49 | 0.61 | -1.5% | 0 | retired |
| 21 | **crypto_supertrend** | crypto 1h | -8.03% | -4,014 | -495 | -9.27% | 13 | 15 | 0.05 | -8.1% | 0 | retired |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| dual_momentum | Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash |
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
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:HCLTECH | 12 | 1,314.16 | 1,156.23 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:TCS | 7 | 2,256.35 | 1,985.19 | – | 13 Oct 15:10 |
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,712.22 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,309.72 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:DRREDDY | 13 | 1,241.85 | 1,255.22 | – | 19 Oct 15:05 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |
| tv_rating_scalper | NSE:HDFCBANK | -23 | 679.36 | 684.94 | 668.63 | 29 Oct 09:30 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 29 Oct 09:30 | tv_rating_scalper | SELL | 23 | NSE:HDFCBANK | 679.36 |  | TV 15m -0.60 / 1h -0.47 |
| 28 Oct 15:15 | supertrend_intraday | BUY | 8 | NSE:BHARTIARTL | 1,958.49 | -154 | intraday square-off |
| 28 Oct 15:15 | supertrend_intraday | BUY | 14 | NSE:INFY | 1,114.77 | -47 | intraday square-off |
| 28 Oct 15:15 | ema_crossover | BUY | 14 | NSE:INFY | 1,114.77 | -47 | intraday square-off |
| 28 Oct 14:40 | ema_crossover | BUY | 13 | NSE:RELIANCE | 1,161.53 | +227 | target |
| 28 Oct 14:30 | tv_rating_scalper | BUY | 11 | NSE:ICICIBANK | 1,378.98 | -77 | 15m rating faded (+0.11) |
| 28 Oct 13:15 | supertrend_intraday | BUY | 13 | NSE:AXISBANK | 1,218.14 | -230 | Supertrend reversed |
| 28 Oct 12:45 | tv_rating_scalper | BUY | 62 | NSE:ITC | 256.60 | +20 | 15m rating faded (+0.05) |
| 28 Oct 12:25 | ema_crossover | BUY | 6 | NSE:TCS | 2,439.09 | -159 | stop-loss |
| 28 Oct 11:45 | tv_rating_scalper | BUY | 17 | NSE:SBIN | 954.44 | -78 | 15m rating faded (+0.11) |
| 28 Oct 10:30 | ema_crossover | SELL | 13 | NSE:RELIANCE | 1,179.56 |  | EMA9<21, RSI 41 |
| 28 Oct 10:15 | tv_rating_scalper | SELL | 17 | NSE:SBIN | 950.31 |  | TV 15m -0.56 / 1h -0.49 |
| 28 Oct 10:00 | tv_rating_scalper | BUY | 24 | NSE:HDFCBANK | 678.79 | -191 | stop-loss |
| 28 Oct 10:00 | ema_crossover | BUY | 13 | NSE:RELIANCE | 1,199.14 | -149 | stop-loss |
| 28 Oct 09:45 | supertrend_intraday | SELL | 8 | NSE:BHARTIARTL | 1,940.21 |  | Supertrend flipped down |
| 28 Oct 09:45 | supertrend_intraday | SELL | 13 | NSE:AXISBANK | 1,201.06 |  | Supertrend flipped down |
| 28 Oct 09:45 | supertrend_intraday | SELL | 14 | NSE:INFY | 1,111.98 |  | Supertrend flipped down |
| 28 Oct 09:45 | ema_crossover | SELL | 6 | NSE:TCS | 2,413.82 |  | EMA9<21, RSI 21 |
| 28 Oct 09:45 | ema_crossover | SELL | 14 | NSE:INFY | 1,111.98 |  | EMA9<21, RSI 24 |
| 28 Oct 09:45 | ema_crossover | SELL | 13 | NSE:RELIANCE | 1,188.26 |  | EMA9<21, RSI 44 |
| 28 Oct 09:30 | tv_rating_scalper | SELL | 11 | NSE:ICICIBANK | 1,372.63 |  | TV 15m -0.65 / 1h -0.25 |
| 28 Oct 09:30 | tv_rating_scalper | SELL | 24 | NSE:HDFCBANK | 671.17 |  | TV 15m -0.65 / 1h -0.51 |
| 28 Oct 09:25 | tv_rating_scalper | SELL | 62 | NSE:ITC | 257.05 |  | TV 15m -0.54 / 1h -0.35 |
| 27 Oct 15:15 | supertrend_intraday | BUY | 14 | NSE:RELIANCE | 1,195.84 | -119 | intraday square-off |
| 27 Oct 15:15 | ema_crossover | BUY | 6 | NSE:TCS | 2,507.60 | -98 | intraday square-off |
| 27 Oct 12:55 | ema_crossover | BUY | 13 | NSE:RELIANCE | 1,198.74 | -148 | stop-loss |
| 27 Oct 12:15 | tv_rating_scalper | BUY | 23 | NSE:HDFCBANK | 688.24 | -61 | 15m rating faded (+0.00) |
| 27 Oct 11:45 | ema_crossover | BUY | 14 | NSE:INFY | 1,148.63 | -202 | stop-loss |
| 27 Oct 11:40 | tv_rating_scalper | BUY | 14 | NSE:INFY | 1,144.88 | -150 | stop-loss |
| 27 Oct 10:45 | tv_rating_scalper | SELL | 23 | NSE:HDFCBANK | 685.91 |  | TV 15m -0.51 / 1h -0.51 |
