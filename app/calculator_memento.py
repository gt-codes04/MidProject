"""Calculator memento utilities.

This module provides a small Memento + Caretaker implementation used by the
history / undo-redo logic. Keep the API minimal and avoid heavy deps so CI
runs in clean environments.
"""
from typing import Any, List


class Memento:
    """Simple memento holding an arbitrary serializable state.

    The state is copied on access to avoid accidental external mutation.
    """
    def __init__(self, state: Any):
        # store a shallow copy for safety; callers should provide copyable state
        try:
            # if it's a list/dict-like, make a shallow copy
            if hasattr(state, "copy"):
                self._state = state.copy()
            else:
                self._state = state
        except Exception:
            self._state = state

    def get_state(self) -> Any:
        # Return the stored state (caller will usually copy again if needed)
        try:
            if hasattr(self._state, "copy"):
                return self._state.copy()
        except Exception:
            pass
        return self._state


class Caretaker:
    """Keeps stacks of mementos for undo/redo operations.

    The Caretaker assumes an `originator` object with methods:
      - save_to_memento() -> Memento
      - restore_from_memento(m: Memento)
    """
    def __init__(self):
        self._undo: List[Memento] = []
        self._redo: List[Memento] = []

    def push(self, m: Memento) -> None:
        self._undo.append(m)
        self._redo.clear()

    def undo(self, originator) -> bool:
        if not self._undo:
            return False
        prev = self._undo.pop()
        # save current state to redo stack
        try:
            self._redo.append(originator.save_to_memento())
        except Exception:
            # If originator doesn't support saving, we still attempt restore
            pass
        originator.restore_from_memento(prev)
        return True

    def redo(self, originator) -> bool:
        if not self._redo:
            return False
        nxt = self._redo.pop()
        try:
            self._undo.append(originator.save_to_memento())
        except Exception:
            pass
        originator.restore_from_memento(nxt)
        return True


# Backwards-compatible alias sometimes used in other modules/tests
CalculatorMemento = Memento

