from app.history import HistoryManager
from app.calculator_memento import Caretaker

def test_history_add_and_list(tmp_path):
    h = HistoryManager(filepath=str(tmp_path/"h.csv"))
    h.add_entry(5,"add",3,8)
    assert not h.is_empty()
    assert "5 add 3 = 8" in h.to_list()[0]

def test_memento_undo_redo(tmp_path):
    h = HistoryManager(filepath=str(tmp_path/"h.csv"))
    ct = Caretaker()
    h.add_entry(1,"add",2,3); ct.push(h.save_to_memento())
    h.add_entry(2,"add",3,5)
    assert len(h.to_list())==2
    assert ct.undo(h) is True and len(h.to_list())==1
    assert ct.redo(h) is True and len(h.to_list())==2
