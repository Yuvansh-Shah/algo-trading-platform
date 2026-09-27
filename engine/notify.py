"""Phone notifications.

- ntfy.sh (default, free, no account): install the "ntfy" app, subscribe to your topic,
  and set the NTFY_TOPIC secret on GitHub.
- Telegram (optional): set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID secrets.
"""
from __future__ import annotations

import os

import requests


def send(message: str, title: str = "Algo bot", tags: str = "chart_with_upwards_trend",
         priority: str = "default") -> None:
    topic = os.environ.get("NTFY_TOPIC", "").strip()
    if topic:
        try:
            requests.post(f"https://ntfy.sh/{topic}", data=message.encode("utf-8"), timeout=10,
                          headers={"Title": title.encode("ascii", "ignore").decode(), "Tags": tags,
                                   "Priority": priority})
        except Exception as e:
            print("ntfy failed:", e)
    tok, chat = os.environ.get("TELEGRAM_BOT_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    if tok and chat:
        try:
            requests.post(f"https://api.telegram.org/bot{tok}/sendMessage", timeout=10,
                          json={"chat_id": chat, "text": f"*{title}*\n{message}", "parse_mode": "Markdown"})
        except Exception as e:
            print("telegram failed:", e)
    if not topic and not (tok and chat):
        print(f"(notify) {title}: {message}")
