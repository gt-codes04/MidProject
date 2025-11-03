# app/calculator_config.py
"""Module for managing application configuration from environment variables."""
from __future__ import annotations
import os
try:
    from dotenv import load_dotenv
except Exception:
    # Provide a no-op fallback so the module imports in CI without extra deps.
    def load_dotenv(*args, **kwargs):
        return None


class Config:
    """Loads and provides access to configuration settings.

    Backwards-compatible `load()` entrypoint is provided because other
    modules call `Config.load()` during initialization.
    """

    @staticmethod
    def load(override: bool = True) -> None:
        """Load environment variables and ensure runtime directories exist."""
        # Load from .env if available (no-op if load_dotenv missing)
        try:
            load_dotenv(override=override)
        except TypeError:
            # older/simple fallback signature
            load_dotenv()
        # Ensure directories exist so logger/history can create files during tests
        os.makedirs(Config.get_log_dir(), exist_ok=True)
        os.makedirs(Config.get_history_dir(), exist_ok=True)

    # Backwards-compatible alias retained for older code
    load_config = load

    # --------- Paths / files ----------
    @staticmethod
    def get_log_dir() -> str:
        return os.getenv("CALCULATOR_LOG_DIR", "logs")

    @staticmethod
    def get_log_file() -> str:
        return os.getenv("CALCULATOR_LOG_FILE", "app.log")

    @staticmethod
    def get_history_dir() -> str:
        return os.getenv("CALCULATOR_HISTORY_DIR", "history")

    @staticmethod
    def get_history_file() -> str:
        return os.getenv("CALCULATOR_HISTORY_FILE", "calculation_history.csv")

    # --------- History / behavior ----------
    @staticmethod
    def get_max_history_size() -> int:
        return int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 100))

    @staticmethod
    def get_auto_save() -> bool:
        val = os.getenv("CALCULATOR_AUTO_SAVE", "false").strip().lower()
        return val in {"1", "true", "yes", "on"}

    # --------- Calculation settings ----------
    @staticmethod
    def get_precision() -> int:
        return int(os.getenv("CALCULATOR_PRECISION", 4))

    @staticmethod
    def get_max_input_value() -> float:
        return float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1_000_000))

    @staticmethod
    def get_default_encoding() -> str:
        return os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
