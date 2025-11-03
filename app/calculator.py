# app/calculator_config.py
from __future__ import annotations
import os
from dotenv import load_dotenv, find_dotenv  # <-- add find_dotenv

class Config:
    """Loads and provides access to configuration settings."""

    @staticmethod
    def load_config() -> None:
        """
        Load .env from project root reliably.
        - find_dotenv() searches up the directory tree.
        - override=True ensures .env values replace process env vars.
        """
        dotenv_path = find_dotenv(usecwd=True)
        load_dotenv(dotenv_path=dotenv_path, override=True)

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

    @staticmethod
    def get_max_history_size() -> int:
        return int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 100))

    @staticmethod
    def get_auto_save() -> bool:
        val = os.getenv("CALCULATOR_AUTO_SAVE", "false").strip().lower()
        return val in {"1", "true", "yes", "on"}

    @staticmethod
    def get_precision() -> int:
        return int(os.getenv("CALCULATOR_PRECISION", 4))

    @staticmethod
    def get_max_input_value() -> float:
        return float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1_000_000))

    @staticmethod
    def get_default_encoding() -> str:
        return os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
