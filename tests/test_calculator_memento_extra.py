import app.calculator_memento as cm


def test_memento_shallow_copy():
    original = [1]
    m = cm.Memento(original)
    # Mutate original after creating memento; memento should keep the old copy
    original.append(2)
    assert m.get_state() == [1]


def test_caretaker_undo_redo():
    class Origin:
        def __init__(self, state):
            self.state = state

        def save_to_memento(self):
            return cm.Memento(self.state)

        def restore_from_memento(self, m):
            self.state = m.get_state()

    origin = Origin("s0")
    c = cm.Caretaker()

    # push initial state
    c.push(origin.save_to_memento())

    # change and push another state
    origin.state = "s1"
    c.push(origin.save_to_memento())

    # change current state but don't push
    origin.state = "s2"

    assert c.undo(origin) is True
    # undo should restore to the previous saved state (s0)
    assert origin.state == "s0"

    # redo should bring back the state that was current when undo was called (s2)
    assert c.redo(origin) is True
    assert origin.state == "s2"


def test_undo_with_save_failure_returns_true():
    class BadOrigin:
        def __init__(self, state):
            self.state = state

        def save_to_memento(self):
            raise RuntimeError("cannot save")

        def restore_from_memento(self, m):
            self.state = m.get_state()

    bad = BadOrigin("x0")
    c = cm.Caretaker()
    c.push(cm.Memento("x1"))

    # Even if save_to_memento raises, undo should attempt restore and return True
    assert c.undo(bad) is True
