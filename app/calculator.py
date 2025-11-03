from typing import Tuple
from .calculation import CalculationFactory
from .history import HistoryManager
from .calculator_memento import Caretaker
from .logger import setup_logger, LoggingObserver
from .exceptions import OperationError, ValidationError
from .input_validators import validate_two_numbers

def validate_input(s: str) -> Tuple[str, str | None, str | None]:
    s = (s or "").strip().lower()
    if s in {"exit","quit"}: return ("exit",None,None)
    if s=="help": return ("help",None,None)
    if s=="history": return ("history",None,None)
    if s=="clear": return ("clear",None,None)
    if s=="undo": return ("undo",None,None)
    if s=="redo": return ("redo",None,None)
    if s=="save": return ("save",None,None)
    if s=="load": return ("load",None,None)
    parts = s.split()
    if len(parts)==3: return (parts[0], parts[1], parts[2])
    raise ValueError("Invalid command format.")

class CalculatorREPL:
    def __init__(self):
        setup_logger()
        self.history = HistoryManager()
        self.caretaker = Caretaker()
        self.observers = [LoggingObserver()]

    def _notify(self, op, a, b, result):
        for obs in self.observers:
            obs.update(op, a, b, result)

    def perform(self, op: str, a_raw: str, b_raw: str):
        try:
            a, b = validate_two_numbers(a_raw, b_raw)
            calc = CalculationFactory.create(op, a, b)
            self.caretaker.push(self.history.save_to_memento())
            result = calc.get_result()
            self.history.add_entry(a, op, b, result)
            self._notify(op, a, b, result)
            out = int(result) if result == int(result) else result
            print(f"Result: {out}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except (OperationError, ValidationError) as e:
            print(f"Error: {e}")

    def cmd_history(self):
        if self.history.is_empty():
            print("History is empty.")
        else:
            for line in self.history.to_list():
                print(line)

    def cmd_clear(self):
        self.history.clear()
        print("History cleared.")

    def cmd_undo(self):
        print("Undo successful." if self.caretaker.undo(self.history) else "Nothing to undo.")

    def cmd_redo(self):
        print("Redo successful." if self.caretaker.redo(self.history) else "Nothing to redo.")

    def cmd_save(self):
        self.history.save()
        print("History saved.")

    def cmd_load(self):
        self.history.load()
        print("History loaded.")

    def _help(self):
        print("Available Commands")
        print("  help, history, clear, undo, redo, save, load, exit")
        print("  Or: add 5 3 | divide 10 2 | power 2 8 | int_divide 10 3 | modulus 10 3 | percent 25 100 | abs_diff 9 2 | root 27 3")

    def run(self):
        print("Advanced Calculator REPL. Type 'help' for commands, 'exit' to quit.")
        while True:
            try:
                line = input(">> ")
                kind, a, b = validate_input(line)
                if kind=="exit": print("Exiting calculator. Goodbye!"); break
                if kind=="help": self._help(); continue
                if kind=="history": self.cmd_history(); continue
                if kind=="clear": self.cmd_clear(); continue
                if kind=="undo": self.cmd_undo(); continue
                if kind=="redo": self.cmd_redo(); continue
                if kind=="save": self.cmd_save(); continue
                if kind=="load": self.cmd_load(); continue
                if a is None or b is None: print("Input Error: Invalid command format."); continue
                self.perform(kind, a, b)
            except ValueError as ve:
                if str(ve)=="Invalid command format.":
                    print("Input Error: Invalid command format.")
                else:
                    print(f"Input Error: {ve}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":  # pragma: no cover
    CalculatorREPL().run()
