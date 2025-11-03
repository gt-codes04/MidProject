import os, pandas as pd
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
                df = pd.read_csv(self.filepath, encoding=Config.get_default_encoding())
                self._rows = df.to_dict("records")
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
        pd.DataFrame(self._rows, columns=["operation","a","b","result"]).to_csv(
            self.filepath, index=False, encoding=Config.get_default_encoding()
        )

    def load(self):  # pragma: no cover
        self._load_or_initialize()

    # Memento originator
    def save_to_memento(self) -> Memento:
        return Memento(self._rows.copy())

    def restore_from_memento(self, m: Memento):
        self._rows = list(m.get_state())
