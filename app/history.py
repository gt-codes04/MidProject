import os
import csv
from typing import List, Dict, Any
from .calculator_memento import Memento
from .calculator_config import Config

class HistoryManager:
    def __init__(self, filepath: str | None = None):
        Config.load()
        self.filepath = filepath or os.path.join(
            Config.get_history_dir(), Config.get_history_file()
        )
        self._rows: List[Dict[str, Any]] = []
        self._load_or_initialize()

    def _load_or_initialize(self):  # pragma: no cover
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, encoding=Config.get_default_encoding(), newline='') as fh:
                    reader = csv.DictReader(fh)
                    self._rows = [
                        {
                            "operation": row.get("operation"),
                            "a": float(row.get("a")) if row.get("a") not in (None, "") else 0.0,
                            "b": float(row.get("b")) if row.get("b") not in (None, "") else 0.0,
                            "result": float(row.get("result")) if row.get("result") not in (None, "") else 0.0,
                        }
                        for row in reader
                    ]
            except Exception:
                self._rows = []
        else:
            self._rows = []

    def add_entry(self, a: float, op: str, b: float, result: float):
        self._rows.append({"operation": op, "a": a, "b": b, "result": result})
        maxn = Config.get_max_history_size()
        if len(self._rows) > maxn:
            self._rows.pop(0)

    def clear(self):
        self._rows.clear()

    def is_empty(self) -> bool:
        return len(self._rows) == 0

    def to_list(self) -> List[str]:
        return [f"{r['a']} {r['operation']} {r['b']} = {r['result']}" for r in self._rows]

    def save(self):  # pragma: no cover
        # Write CSV using the stdlib csv module to avoid pandas dependency
        with open(self.filepath, "w", encoding=Config.get_default_encoding(), newline='') as fh:
            writer = csv.DictWriter(fh, fieldnames=["operation", "a", "b", "result"])
            writer.writeheader()
            for row in self._rows:
                writer.writerow({
                    "operation": row.get("operation"),
                    "a": row.get("a"),
                    "b": row.get("b"),
                    "result": row.get("result"),
                })

    def load(self):  # pragma: no cover
        self._load_or_initialize()

    # Memento originator
    def save_to_memento(self) -> Memento:
        return Memento(self._rows.copy())

    def restore_from_memento(self, m: Memento):
        self._rows = list(m.get_state())
