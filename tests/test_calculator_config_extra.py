import os

import app.calculator_config as cfg


def test_fallback_load_dotenv_parses(tmp_path, monkeypatch):
    env_file = tmp_path / ".env_test"
    env_file.write_text("""# comment\nKEY1=val1\nKEY2=\"quoted val\"\nINVALIDLINE\n""")

    monkeypatch.delenv("KEY1", raising=False)
    monkeypatch.delenv("KEY2", raising=False)

    # Use the fallback loader directly and assert it populates os.environ
    cfg._fallback_load_dotenv(override=True, path=str(env_file))

    assert os.environ.get("KEY1") == "val1"
    assert os.environ.get("KEY2") == "quoted val"


def test_load_respects_override_and_creates_dirs(tmp_path, monkeypatch):
    # Point log/history to temporary directories
    log_dir = tmp_path / "logsdir"
    hist_dir = tmp_path / "histdir"
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(log_dir))
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(hist_dir))

    # Simulate an older load_dotenv that doesn't accept the 'override' kwarg
    # so calling load_dotenv(override=...) raises TypeError and the code
    # should then call load_dotenv() successfully.
    def simple_loader():
        # set a side-effect to show it was called
        os.environ.setdefault("DUMMY_LOADER", "1")

    monkeypatch.setattr(cfg, "load_dotenv", simple_loader)

    # This should not raise and should create the directories
    cfg.Config.load(override=True)

    assert log_dir.exists()
    assert hist_dir.exists()


def test_get_precision_and_auto_save(monkeypatch):
    monkeypatch.setenv("CALCULATOR_PRECISION", "8")
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "True")

    assert cfg.Config.get_precision() == 8
    assert cfg.Config.get_auto_save() is True
