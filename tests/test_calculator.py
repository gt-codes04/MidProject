from unittest.mock import patch
import pytest
from app.calculator import Calculator

def test_repl_exit(capsys, clean_calculator):
    with patch("builtins.input", side_effect=["exit"]): clean_calculator.run()
    out = capsys.readouterr().out
    assert "Exiting calculator. Goodbye!" in out

def test_repl_help(capsys, clean_calculator):
    with patch("builtins.input", side_effect=["help","exit"]): clean_calculator.run()
    out = capsys.readouterr().out
    assert "Available Commands" in out

@pytest.fixture
def clean_calculator():
    """Return a fresh calculator instance for each test."""
    # Use the Calculator class from app.calculator
    r = Calculator()
    r.history.clear()  # Ensure history starts empty
    return r

def test_repl_history_empty(capsys, clean_calculator):
    with patch("builtins.input", side_effect=["history","exit"]): clean_calculator.run()
    out = capsys.readouterr().out
    assert "History is empty." in out

def test_repl_add_and_result(capsys, clean_calculator):
    with patch("builtins.input", side_effect=["add 5 3","exit"]): clean_calculator.run()
    out = capsys.readouterr().out
    assert "Result: 8" in out

def test_repl_divide_by_zero(capsys, clean_calculator):
    with patch("builtins.input", side_effect=["divide 5 0","exit"]): clean_calculator.run()
    out = capsys.readouterr().out
    assert "Error: Cannot divide by zero." in out

def test_repl_invalid_command(capsys, clean_calculator):
    with patch("builtins.input", side_effect=["invalid command", "exit"]): clean_calculator.run()
    out = capsys.readouterr().out
    assert "Input Error: Invalid command format." in out

def test_repl_undo_redo_flow(capsys, clean_calculator):
    inputs = [
        "add 5 3",      # Do calculation
        "undo",         # Undo it
        "redo",         # Redo it
        "undo",         # Undo again
        "add 7 4",      # New calculation (should clear redo stack)
        "redo",         # Should show nothing to redo
        "exit"
    ]
    with patch("builtins.input", side_effect=inputs): clean_calculator.run()
    out = capsys.readouterr().out
    assert "Result: 8" in out
    assert "Undo successful" in out
    assert "Redo successful" in out
    assert "Nothing to redo" in out

def test_repl_clear_save_load(capsys, clean_calculator):
    inputs = [
        "add 5 3",     # Do calculation
        "save",        # Save history
        "clear",       # Clear history
        "history",     # Should be empty
        "load",        # Load saved history
        "history",     # Should show calculation again
        "exit"
    ]
    with patch("builtins.input", side_effect=inputs): clean_calculator.run()
    out = capsys.readouterr().out
    assert "History saved" in out
    assert "History cleared" in out
    assert "History is empty" in out
    assert "History loaded" in out
    assert "5.0 add 3.0 = 8.0" in out  # Numbers are stored and displayed with decimal points

def test_repl_invalid_number_input(capsys, clean_calculator):
    inputs = ["add abc 3", "exit"]
    with patch("builtins.input", side_effect=inputs): clean_calculator.run()
    out = capsys.readouterr().out
    assert "Error: Invalid numeric input: abc" in out

def test_repl_large_number_input(capsys, clean_calculator):
    inputs = ["add 1e15 3", "exit"]  # Should exceed default max of 1e12
    with patch("builtins.input", side_effect=inputs): clean_calculator.run()
    out = capsys.readouterr().out
    assert "Error: Input exceeds allowed magnitude" in out

def test_repl_quit_alias(capsys, clean_calculator):
    with patch("builtins.input", side_effect=["quit"]): clean_calculator.run()
    out = capsys.readouterr().out
    assert "Exiting calculator. Goodbye!" in out
