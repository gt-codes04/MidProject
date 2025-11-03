# app/calculator_memento.py
from __future__ import annotations
from dataclasses import dataclass
import pandas as pd

@dataclass
class Memento:
    """Memento that stores a snapshot of the history DataFrame."""
    _state: pd.DataFrame

    def get_state(self) -> pd.DataFrame:
        # Always return a deep copy to avoid accidental mutation.
        return self._state.copy(deep=True)
