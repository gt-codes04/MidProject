import os
import shutil
from pathlib import Path
from app.calculator_config import Config


def test_getters_default_and_env(monkeypatch, tmp_path):
    # Ensure defaults when no env vars set
    monkeypatch.delenv("CALCULATOR_LOG_DIR", raising=False)
    monkeypatch.delenv("CALCULATOR_HISTORY_DIR", raising=False)
    monkeypatch.delenv("CALCULATOR_PRECISION", raising=False)
    assert Config.get_log_dir() == "logs"
    assert Config.get_history_dir() == "history"
    assert isinstance(Config.get_precision(), int)

    # Override via environment and verify getters read them
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path / "mylogs"))
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path / "myhist"))
    monkeypatch.setenv("CALCULATOR_PRECISION", "9")
    assert Config.get_log_dir() == str(tmp_path / "mylogs")
    assert Config.get_history_dir() == str(tmp_path / "myhist")
    assert Config.get_precision() == 9


def test_load_creates_directories(monkeypatch, tmp_path):
    # Set dirs to locations inside tmp_path
    log_dir = tmp_path / "logs_dir"
    hist_dir = tmp_path / "history_dir"
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(log_dir))
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(hist_dir))

    # Remove if exists
    if log_dir.exists():
        shutil.rmtree(log_dir)
    if hist_dir.exists():
        shutil.rmtree(hist_dir)

    # Call load which should create the directories
    Config.load(override=True)

    assert log_dir.exists() and log_dir.is_dir()
    assert hist_dir.exists() and hist_dir.is_dir()

    # Cleanup created directories
    shutil.rmtree(log_dir)
    shutil.rmtree(hist_dir)


def test_load_handles_typeerror_signature(monkeypatch, tmp_path):
    # Simulate a load_dotenv implementation that raises TypeError when called
    # with keyword args, and works when called without args.
    called = {"count": 0}

    def fake_load_dotenv(*args, **kwargs):
        # First invocation with keyword arg will raise TypeError
        if kwargs:
            called["count"] += 1
            raise TypeError("bad signature")
        # On the fallback call without kwargs, set an env var
        os.environ["CALCULATOR_PRECISION"] = "12"

    # Monkeypatch the module-level load_dotenv used by Config
    import app.calculator_config as cc
    monkeypatch.setattr(cc, "load_dotenv", fake_load_dotenv)

    # Ensure env not set previously
    monkeypatch.delenv("CALCULATOR_PRECISION", raising=False)

    # Call load which will first call fake_load_dotenv(override=...), raise
    # TypeError, then call fake_load_dotenv() which sets the var
    cc.Config.load(override=True)
    assert os.environ.get("CALCULATOR_PRECISION") == "12"


def test_fallback_loader_reads_env_file(tmp_path, monkeypatch):
    # Create a temporary .env file with various lines to exercise parsing
    env_file = tmp_path / ".env_test"
    env_file.write_text("""
# comment line
CALCULATOR_LOG_DIR = test_logs
CALCULATOR_HISTORY_DIR=test_history
CALCULATOR_PRECISION=7
INVALID_LINE_WITHOUT_EQUALS
QUOTED="quoted value"
SINGLE_QUOTE='sq'
""")

    import app.calculator_config as cc

    # Ensure variables are not set
    for k in ["CALCULATOR_LOG_DIR", "CALCULATOR_HISTORY_DIR", "CALCULATOR_PRECISION", "QUOTED", "SINGLE_QUOTE"]:
        monkeypatch.delenv(k, raising=False)

    # Call the fallback loader directly with the path to our file
    cc._fallback_load_dotenv(override=True, path=str(env_file))

    assert os.environ.get("CALCULATOR_LOG_DIR") == "test_logs"
    assert os.environ.get("CALCULATOR_HISTORY_DIR") == "test_history"
    assert os.environ.get("CALCULATOR_PRECISION") == "7"
    assert os.environ.get("QUOTED") == "quoted value"
    assert os.environ.get("SINGLE_QUOTE") == "sq"
