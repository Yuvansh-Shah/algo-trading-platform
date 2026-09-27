# Algo Trading Status

_Updated 27 Sep 2026 17:11 IST · paper trading unless marked LIVE_

| Bot | Market | TF | Equity | Total P&L | Today | Trades | Win % | Open | Last run | Health |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| crypto_supertrend |  |  | 10,000 | +0 (+0.00%) | +0 | 0 | – | 0 | – | ❌ assignment destination is read-only |
| ema_crossover |  |  | 100,000 | +0 (+0.00%) | +0 | 0 | – | 0 | – | ✅ |
| external_signals |  |  | 100,000 | +0 (+0.00%) | +0 | 0 | – | 0 | – | ✅ |
| tv_rating_swing |  |  | 200,000 | +0 (+0.00%) | +0 | 0 | – | 0 | – | ✅ |

## Open positions

_None_

## Last 25 trades

_No trades yet_

## Errors

**crypto_supertrend** at 27 Sep 17:11
```
Traceback (most recent call last):
  File "/home/runner/work/algo-trading-platform/algo-trading-platform/engine/run.py", line 197, in main
    s.on_bar(ctx)
  File "/home/runner/work/algo-trading-platform/algo-trading-platform/strategies/crypto_supertrend.py", line 14, in on_bar
    _, direction = ta.supertrend(df, 10, 3.0)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/algo-trading-platform/algo-trading-platform/engine/ta.py", line 88, in supertrend
    lower[i] = lower[i - 1]
    ~~~~~^^^
ValueError: assignment destination is read-only

```
