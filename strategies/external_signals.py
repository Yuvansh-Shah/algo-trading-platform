"""Executes signals dropped into signals/inbox/*.json by anything outside the engine:
Claude using the TradingView MCP (see claude/), a script, or you by hand.

Signal format (one object or a list):
  {"strategy": "external_signals", "symbol": "NSE:TCS", "action": "buy",
   "value": 25000, "sl": 2010, "tp": 2250, "reason": "MCP: 4h STRONG_BUY + earnings beat",
   "expires": "2026-09-29T10:00:00Z"}
action: buy | sell | close.  Size with qty, value (money) or pct (of equity).
"""
from engine import Strategy


class ExternalSignals(Strategy):
    market = "NSE"          # checked every run while NSE is open
    interval = "15m"
    capital = 100_000
    allow_short = False

    def on_bar(self, ctx):
        for sig in ctx.signals():
            sym, action = sig["symbol"], sig.get("action", "").lower()
            size = {k: sig[k] for k in ("qty", "value", "pct") if k in sig} or {"pct": 20}
            levels = {k: sig[k] for k in ("sl", "tp", "sl_pct", "tp_pct", "trail_pct") if k in sig}
            why = sig.get("reason", "external signal")
            if action == "buy":
                ctx.buy(sym, **size, **levels, reason=why)
            elif action == "sell":
                ctx.sell(sym, **size, **levels, reason=why)
            elif action == "close":
                ctx.close(sym, reason=why)
            else:
                ctx.log("ignored signal with unknown action:", sig)
