"""Finds every Strategy subclass in strategies/*.py (files starting with _ are ignored)."""
from __future__ import annotations

import importlib.util
import inspect
import traceback
from pathlib import Path

from .strategy import Strategy

ROOT = Path(__file__).resolve().parent.parent
STRATEGY_DIR = ROOT / "strategies"


def load_strategies(only: list[str] | None = None) -> tuple[list[Strategy], list[str]]:
    found, errors = [], []
    for path in sorted(STRATEGY_DIR.glob("*.py")):
        if path.name.startswith("_"):
            continue
        try:
            spec = importlib.util.spec_from_file_location(f"strategies.{path.stem}", path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
        except Exception:
            errors.append(f"{path.name}: failed to import\n{traceback.format_exc(limit=3)}")
            continue
        classes = [c for _, c in inspect.getmembers(mod, inspect.isclass)
                   if issubclass(c, Strategy) and c is not Strategy and c.__module__ == mod.__name__]
        for cls in classes:
            s = cls()
            s.name = s.name or (path.stem if len(classes) == 1 else f"{path.stem}.{cls.__name__}")
            if only and s.name not in only:
                continue
            found.append(s)
    return found, errors
