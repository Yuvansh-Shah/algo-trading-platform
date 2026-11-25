# Bot leaderboard

_Updated 25 Nov 2026 10:40 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **dual_momentum** | positional 1D | +15.36% | +7,679 | +829 | +1.08% | 0 | – | – | -3.6% | 1 | ok |
| 2 | **nifty_buy_hold** | benchmark 1D | +14.27% | +7,137 | +847 | +0.00% | 0 | – | – | -3.0% | 1 | ok |
| 3 | **tv_rating_swing** | swing 1D | +12.09% | +6,044 | +404 | -2.19% | 2 | 50 | 1.86 | -2.8% | 3 | ok |
| 4 | **momentum_rotation** | positional 1D | +10.23% | +5,117 | +314 | -4.04% | 3 | 100 | ∞ | -4.4% | 3 | ok |
| 5 | **bb_reversion_daily** | swing 1D | +0.47% | +236 | +0 | -13.80% | 1 | 100 | ∞ | -1.5% | 0 | ok |
| 6 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -14.27% | 0 | – | – | 0.0% | 0 | ok |
| 7 | **supertrend_intraday** | intraday 15m | -1.74% | -871 | -159 | -16.02% | 53 | 40 | 0.92 | -4.2% | 3 | ok |
| 8 | **tv_rating_scalper** | intraday 15m | -1.77% | -885 | -27 | -16.04% | 120 | 40 | 1.01 | -5.8% | 3 | ok |
| 9 | **ema_crossover** | intraday 15m | -2.28% | -1,142 | -192 | -16.56% | 71 | 38 | 0.87 | -4.4% | 3 | ok |
| 10 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | +0 | -12.04% | 5 | 60 | 4.63 | -0.9% | 0 | retired |
| 11 | **gap_and_go** | intraday 15m | +1.40% | +701 | +0 | -12.87% | 10 | 80 | 2.36 | -1.2% | 0 | retired |
| 12 | **vwap_pullback** | intraday 15m | +0.98% | +491 | +0 | -13.29% | 41 | 51 | 1.48 | -1.7% | 0 | retired |
| 13 | **donchian_turtle** | swing 1D | +0.79% | +395 | +0 | -13.48% | 3 | 67 | 2.04 | -2.5% | 0 | retired |
| 14 | **orb_breakout** | intraday 15m | +0.54% | +272 | +0 | -13.73% | 15 | 60 | 1.51 | -1.5% | 0 | retired |
| 15 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -14.27% | 0 | – | – | 0.0% | 0 | retired |
| 16 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -14.27% | 0 | – | – | 0.0% | 0 | retired |
| 17 | **vwap_reversion** | intraday 15m | -0.33% | -166 | +0 | -14.61% | 35 | 57 | 1.09 | -1.3% | 0 | retired |
| 18 | **bb_squeeze** | intraday 15m | -0.98% | -492 | +0 | -15.26% | 20 | 40 | 0.68 | -1.4% | 0 | retired |
| 19 | **macd_adx** | intraday 15m | -1.02% | -512 | +0 | -15.30% | 22 | 32 | 0.71 | -1.4% | 0 | retired |
| 20 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | +0 | -15.80% | 35 | 49 | 0.61 | -1.5% | 0 | retired |
| 21 | **crypto_supertrend** | crypto 1h | -8.03% | -4,014 | +0 | -22.30% | 13 | 15 | 0.05 | -8.1% | 0 | retired |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| dual_momentum | Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
| supertrend_intraday | Supertrend 10/3 flips on 15m with the NIFTY trend, entries before 11:00; 2R |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement, with the NIFTY trend, entries before 11:00 |
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
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,530.59 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:DRREDDY | 13 | 1,241.85 | 1,305.35 | – | 19 Oct 15:05 |
| tv_rating_swing | NSE:EICHERMOT | 2 | 8,044.61 | 7,695.75 | – | 19 Nov 15:05 |
| momentum_rotation | NSE:KOTAKBANK | 37 | 439.54 | 386.72 | – | 13 Oct 15:10 |
| momentum_rotation | NSE:DRREDDY | 12 | 1,365.27 | 1,201.20 | – | 04 Nov 15:10 |
| momentum_rotation | NSE:HDFCBANK | 21 | 849.22 | 747.16 | – | 20 Nov 15:10 |
| supertrend_intraday | NSE:RELIANCE | 11 | 1,388.98 | 1,350.29 | 1,460.11 | 25 Nov 09:45 |
| supertrend_intraday | NSE:HDFCBANK | 19 | 847.32 | 820.84 | 899.46 | 25 Nov 09:45 |
| supertrend_intraday | NSE:ICICIBANK | 9 | 1,638.53 | 1,600.18 | 1,716.04 | 25 Nov 09:45 |
| tv_rating_scalper | NSE:INFY | 14 | 1,139.13 | 1,129.79 | 1,157.12 | 25 Nov 09:30 |
| tv_rating_scalper | NSE:TCS | 6 | 2,510.20 | 2,489.62 | 2,549.86 | 25 Nov 09:30 |
| tv_rating_scalper | NSE:KOTAKBANK | 31 | 512.45 | 508.25 | 520.55 | 25 Nov 09:30 |
| ema_crossover | NSE:HDFCBANK | 19 | 844.82 | 835.92 | 861.50 | 25 Nov 10:00 |
| ema_crossover | NSE:ICICIBANK | 9 | 1,636.83 | 1,621.67 | 1,662.26 | 25 Nov 10:00 |
| ema_crossover | NSE:AXISBANK | 11 | 1,420.18 | 1,406.34 | 1,443.73 | 25 Nov 10:15 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
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
| 23 Nov 10:05 | tv_rating_scalper | SELL | 6 | NSE:TCS | 2,446.91 | +238 | target |
| 23 Nov 10:00 | ema_crossover | BUY | 14 | NSE:INFY | 1,120.42 |  | EMA9>21, RSI 68 |
| 23 Nov 09:50 | tv_rating_scalper | SELL | 11 | NSE:RELIANCE | 1,368.53 | -148 | stop-loss |
| 23 Nov 09:45 | tv_rating_scalper | BUY | 53 | NSE:ITC | 300.46 |  | TV 15m +0.51 / 1h +0.47 |
| 23 Nov 09:45 | tv_rating_scalper | BUY | 6 | NSE:TCS | 2,406.08 |  | TV 15m +0.54 / 1h +0.36 |
| 23 Nov 09:45 | supertrend_intraday | BUY | 14 | NSE:INFY | 1,106.52 |  | Supertrend flipped up |
| 23 Nov 09:40 | tv_rating_scalper | SELL | 31 | NSE:KOTAKBANK | 510.50 | -253 | stop-loss |
| 23 Nov 09:35 | tv_rating_scalper | SELL | 11 | NSE:AXISBANK | 1,437.01 | -252 | stop-loss |
| 23 Nov 09:25 | tv_rating_scalper | BUY | 31 | NSE:KOTAKBANK | 518.40 |  | TV 15m +0.56 / 1h +0.40 |
| 23 Nov 09:25 | tv_rating_scalper | BUY | 11 | NSE:AXISBANK | 1,459.19 |  | TV 15m +0.56 / 1h +0.54 |
| 23 Nov 09:25 | tv_rating_scalper | BUY | 11 | NSE:RELIANCE | 1,381.28 |  | TV 15m +0.60 / 1h +0.60 |
| 23 Nov 09:25 | supertrend_intraday | BUY | 11 | NSE:RELIANCE | 1,381.28 |  | Supertrend flipped up |
| 20 Nov 15:15 | supertrend_intraday | SELL | 6 | NSE:TCS | 2,378.92 | -22 | intraday square-off |
| 20 Nov 15:10 | momentum_rotation | BUY | 21 | NSE:HDFCBANK | 849.22 |  | 3M perf +16.6% |
