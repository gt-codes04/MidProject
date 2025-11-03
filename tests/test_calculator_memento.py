import copy
import pytest
from app.calculator_memento import Memento, Caretaker, CalculatorMemento


class DummyOriginator:
    def __init__(self):
        self.state = []

    def save_to_memento(self):
        # return a memento with a copy of the state
        return Memento(self.state.copy())

    def restore_from_memento(self, m):
        self.state = m.get_state()


def test_memento_returns_copy_for_list():
    lst = [1, 2, 3]
    m = Memento(lst)
    s = m.get_state()
    assert s == lst
    # modifying original shouldn't affect memento's returned state
    lst.append(4)
    s2 = m.get_state()
    assert s2 == [1, 2, 3]


def test_calculator_memento_alias():
    lst = [1]
    cm = CalculatorMemento(lst)
    assert isinstance(cm, Memento)
    assert cm.get_state() == [1]


def test_caretaker_undo_redo_roundtrip():
    origin = DummyOriginator()
    origin.state = [0]
    caretaker = Caretaker()

    # push initial state
    caretaker.push(origin.save_to_memento())

    # mutate origin, push new state
    origin.state.append(1)
    caretaker.push(origin.save_to_memento())

    # another change
    origin.state.append(2)
    caretaker.push(origin.save_to_memento())

    # undo -> should restore to previous state
    assert caretaker.undo(origin) is True
    assert origin.state == [0, 1]

    # undo again
    assert caretaker.undo(origin) is True
    assert origin.state == [0]

    # redo
    assert caretaker.redo(origin) is True
    # after redo, origin should have the next state (0,1)
    assert origin.state == [0, 1]

    # redo again
    assert caretaker.redo(origin) is True
    assert origin.state == [0, 1, 2]


def test_undo_returns_false_when_empty():
    origin = DummyOriginator()
    ct = Caretaker()
    assert ct.undo(origin) is False
    assert ct.redo(origin) is False


def test_memento_with_non_copyable_state():
    # When state has no .copy(), Memento should still return the value
    m = Memento(42)
    assert m.get_state() == 42


def test_caretaker_save_exception_handling():
    # originator whose save_to_memento raises, but restore works
    class BadSaver:
        def __init__(self):
            self.state = [1]

        def save_to_memento(self):
            raise RuntimeError("cannot save")

        def restore_from_memento(self, m):
            self.state = m.get_state()

    origin = BadSaver()
    ct = Caretaker()
    # push two mementos directly
    ct.push(Memento([1]))
    ct.push(Memento([1, 2]))

    # undo should still attempt to restore previous (and not raise)
    assert ct.undo(origin) in (True, False)


def test_memento_copy_exceptions():
    class BadCopy:
        def copy(self):
            raise RuntimeError("bad copy")

    b = BadCopy()
    m = Memento(b)
    # get_state should return the object itself when copy raises
    assert m.get_state() is b
