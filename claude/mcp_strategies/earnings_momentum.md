---
enabled: true
bot: external_signals
---
# Earnings + technicals momentum (NIFTY 50)

Uses things only the MCP gives easily: news, earnings calendar, analyst forecasts.

1. `run-screener` on market `india`, filters `{"index": "NIFTY 50"}`, columns
   close, change, Recommend.All, RSI, EMA50, volume. Keep names with Recommend.All ≥ 0.3,
   RSI between 50 and 70, and close > EMA50.
2. For each survivor (max 8), `get-technicals-rating` on 1D and 4h. Require both ≥ BUY.
3. `get-earnings-calendar` for India — drop names reporting in the next 3 trading days.
4. `get-news` for each remaining name — drop anything with clearly negative fresh news
   (downgrade, fraud, regulatory action, big block sale) in the last 48h.
5. `get-forecasts` — prefer names where the average analyst target is ≥ 8% above price.
6. Signal BUY for the best 2 (pct 20, sl_pct 4, tp_pct 8), unless the bot already holds them.
7. For any stock the bot already holds whose 1D technicals rating is now SELL or worse,
   or with fresh clearly negative news, signal `close`.
