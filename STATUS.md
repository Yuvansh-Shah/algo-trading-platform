# Bot leaderboard

_Updated 21 Oct 2026 14:15 IST · paper trading · every bot started with ₹50,000 (crypto in USDT)_

| # | Bot | Style | Return | P&L | Today | vs NIFTY | Trades | Win % | Profit factor | Max DD | Open | Health |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **momentum_rotation** | positional 1D | +5.52% | +2,760 | -52 | +4.49% | 0 | – | – | -1.6% | 3 | ok |
| 2 | **tv_rating_swing** | swing 1D | +3.45% | +1,725 | -6 | +2.42% | 1 | 0 | 0.00 | -2.2% | 3 | ok |
| 3 | **nifty_buy_hold** | benchmark 1D | +1.03% | +513 | -357 | +0.00% | 0 | – | – | -1.8% | 1 | ok |
| 4 | **supertrend_intraday** | intraday 15m | +0.92% | +462 | +0 | -0.10% | 16 | 50 | 1.67 | -1.9% | 0 | ok |
| 5 | **tv_rating_scalper** | intraday 15m | +0.66% | +330 | +0 | -0.37% | 35 | 46 | 1.28 | -2.0% | 0 | ok |
| 6 | **ema_crossover** | intraday 15m | +0.26% | +132 | +0 | -0.76% | 27 | 41 | 1.27 | -1.7% | 0 | ok |
| 7 | **bb_reversion_daily** | swing 1D | +0.00% | +0 | +0 | -1.03% | 0 | – | – | 0.0% | 0 | ok |
| 8 | **dual_momentum** | positional 1D | +0.00% | +0 | +0 | -1.03% | 0 | – | – | 0.0% | 0 | ok |
| 9 | **external_signals** | claude 15m | +0.00% | +0 | +0 | -1.03% | 0 | – | – | 0.0% | 0 | ok |
| 10 | **hourly_macd_swing** | swing 1h | +2.23% | +1,115 | -490 | +1.20% | 5 | 60 | 4.63 | -0.9% | 0 | retired |
| 11 | **gap_and_go** | intraday 15m | +1.40% | +701 | -391 | +0.38% | 10 | 80 | 2.36 | -1.2% | 0 | retired |
| 12 | **vwap_pullback** | intraday 15m | +0.98% | +491 | +32 | -0.04% | 41 | 51 | 1.48 | -1.7% | 0 | retired |
| 13 | **donchian_turtle** | swing 1D | +0.79% | +395 | +0 | -0.24% | 3 | 67 | 2.04 | -2.5% | 0 | retired |
| 14 | **orb_breakout** | intraday 15m | +0.54% | +272 | -11 | -0.48% | 15 | 60 | 1.51 | -1.5% | 0 | retired |
| 15 | **connors_rsi2** | swing 1D | +0.00% | +0 | +0 | -1.03% | 0 | – | – | 0.0% | 0 | retired |
| 16 | **ema_trend_swing** | swing 1D | +0.00% | +0 | +0 | -1.03% | 0 | – | – | 0.0% | 0 | retired |
| 17 | **vwap_reversion** | intraday 15m | -0.33% | -166 | +151 | -1.36% | 35 | 57 | 1.09 | -1.3% | 0 | retired |
| 18 | **bb_squeeze** | intraday 15m | -0.98% | -492 | -413 | -2.01% | 20 | 40 | 0.68 | -1.4% | 0 | retired |
| 19 | **macd_adx** | intraday 15m | -1.02% | -512 | -178 | -2.05% | 22 | 32 | 0.71 | -1.4% | 0 | retired |
| 20 | **rsi2_scalper** | scalp 15m | -1.53% | -765 | -554 | -2.56% | 35 | 49 | 0.61 | -1.5% | 0 | retired |
| 21 | **crypto_supertrend** | crypto 1h | -8.03% | -4,014 | -495 | -9.05% | 13 | 15 | 0.05 | -8.1% | 0 | retired |

<details><summary>What each bot does</summary>

| Bot | Strategy |
|---|---|
| momentum_rotation | Hold top-3 NIFTY 50 by 3M return (above SMA50, TV rating > 0); rotate out below top 10 |
| tv_rating_swing | NIFTY 50 names rated STRONG BUY (1D) + BUY (1W) by TradingView; 7% trailing stop |
| nifty_buy_hold | Benchmark - 100% NIFTY 50 ETF (NIFTYBEES), buy once and hold |
| supertrend_intraday | Supertrend 10/3 flips on 15m with the NIFTY trend, entries before 11:00; 2R |
| tv_rating_scalper | TradingView 15m STRONG BUY/SELL + 1h agreement, with the NIFTY trend, entries before 11:00 |
| ema_crossover | EMA 9/21 cross + RSI + VWAP, with the NIFTY trend, entries before 11:00; 1.5/3 ATR |
| bb_reversion_daily | Close below lower BB(20,2) while above SMA200 -> buy; exit at the middle band |
| dual_momentum | Monthly: hold the strongest of NIFTY / Bank NIFTY / Next 50 / Gold ETFs by 6M return, else cash |
| external_signals | Executes signals Claude writes using the TradingView MCP (claude/mcp_strategies) |
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
| tv_rating_swing | NSE:TECHM | 10 | 1,579.32 | 1,703.39 | – | 14 Oct 15:05 |
| tv_rating_swing | NSE:ICICIBANK | 12 | 1,383.98 | 1,309.72 | – | 15 Oct 15:05 |
| tv_rating_swing | NSE:DRREDDY | 13 | 1,241.85 | 1,161.38 | – | 19 Oct 15:05 |
| nifty_buy_hold | NSE:NIFTYBEES | 192 | 256.54 | – | – | 13 Oct 09:45 |

## Last 30 fills

| Time (IST) | Bot | Side | Qty | Symbol | Price | P&L | Reason |
|---|---|---|---:|---|---:|---:|---|
| 21 Oct 09:25 | donchian_turtle | SELL | 14 | NSE:INFY | 1,154.62 | +609 | bot retired |
| 21 Oct 09:25 | donchian_turtle | SELL | 11 | NSE:ICICIBANK | 1,405.72 | +212 | bot retired |
| 21 Oct 09:25 | donchian_turtle | SELL | 12 | NSE:AXISBANK | 1,240.75 | -403 | bot retired |
| 19 Oct 23:19 | crypto_supertrend | SELL | 8.57134 | BINANCE:ETHUSDT | 2,394.86 | -411 | bot retired |
| 19 Oct 23:19 | crypto_supertrend | SELL | 0.255042 | BINANCE:BTCUSDT | 81,845.64 | -71 | bot retired |
| 19 Oct 15:15 | vwap_reversion | SELL | 23 | NSE:HDFCBANK | 711.71 | -42 | intraday square-off |
| 19 Oct 15:15 | vwap_pullback | BUY | 13 | NSE:AXISBANK | 1,236.45 | +1 | intraday square-off |
| 19 Oct 15:15 | vwap_pullback | BUY | 9 | NSE:SUNPHARMA | 1,739.05 | +100 | intraday square-off |
| 19 Oct 15:15 | vwap_pullback | BUY | 63 | NSE:ITC | 261.30 | +39 | intraday square-off |
| 19 Oct 15:15 | tv_rating_scalper | BUY | 23 | NSE:HDFCBANK | 711.99 | -43 | intraday square-off |
| 19 Oct 15:15 | tv_rating_scalper | BUY | 13 | NSE:AXISBANK | 1,236.45 | +112 | intraday square-off |
| 19 Oct 15:15 | tv_rating_scalper | SELL | 6 | NSE:TCS | 2,463.11 | +20 | intraday square-off |
| 19 Oct 15:15 | supertrend_intraday | SELL | 17 | NSE:SBIN | 972.41 | -11 | intraday square-off |
| 19 Oct 15:15 | supertrend_intraday | BUY | 14 | NSE:INFY | 1,127.98 | +122 | intraday square-off |
| 19 Oct 15:15 | supertrend_intraday | BUY | 23 | NSE:HDFCBANK | 711.99 | +20 | intraday square-off |
| 19 Oct 15:15 | orb_breakout | BUY | 8 | NSE:BHARTIARTL | 1,874.37 | +173 | intraday square-off |
| 19 Oct 15:15 | orb_breakout | BUY | 11 | NSE:ICICIBANK | 1,386.18 | +19 | intraday square-off |
| 19 Oct 15:15 | orb_breakout | SELL | 16 | NSE:SBIN | 972.46 | -180 | intraday square-off |
| 19 Oct 15:15 | gap_and_go | SELL | 6 | NSE:TCS | 2,463.11 | +20 | intraday square-off |
| 19 Oct 15:15 | gap_and_go | SELL | 14 | NSE:INFY | 1,127.92 | -417 | intraday square-off |
| 19 Oct 15:15 | ema_crossover | BUY | 14 | NSE:INFY | 1,128.38 | +201 | intraday square-off |
| 19 Oct 15:15 | ema_crossover | BUY | 11 | NSE:ICICIBANK | 1,386.18 | -26 | intraday square-off |
| 19 Oct 15:05 | tv_rating_swing | BUY | 13 | NSE:DRREDDY | 1,241.85 |  | TV STRONG BUY +0.54, RSI 60 |
| 19 Oct 15:05 | tv_rating_swing | SELL | 13 | NSE:AXISBANK | 1,233.35 | -701 | TV rating turned SELL (-0.51) |
| 19 Oct 15:00 | vwap_reversion | SELL | 17 | NSE:SBIN | 972.61 | +41 | back to VWAP |
| 19 Oct 15:00 | ema_crossover | BUY | 6 | NSE:TCS | 2,465.99 | -90 | opposite EMA cross |
| 19 Oct 14:40 | vwap_reversion | SELL | 9 | NSE:SUNPHARMA | 1,736.65 | -108 | stop-loss |
| 19 Oct 14:00 | ema_crossover | SELL | 6 | NSE:TCS | 2,452.31 |  | EMA9<21, RSI 47 |
| 19 Oct 13:45 | rsi2_scalper | SELL | 6 | NSE:TCS | 2,451.51 | -15 | time stop (1h) |
| 19 Oct 13:45 | rsi2_scalper | SELL | 13 | NSE:RELIANCE | 1,204.56 | -96 | time stop (1h) |
