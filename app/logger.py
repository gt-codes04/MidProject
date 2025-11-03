import logging, os
from .calculator_config import Config

def setup_logger():
    Config.load()
    logfile = os.path.join(Config.get_log_dir(), Config.get_log_file())
    if not logging.getLogger().handlers:
        logging.basicConfig(
            level=logging.INFO,
            filename=logfile,
            encoding=Config.get_default_encoding(),
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

class LoggingObserver:
    def update(self, operation: str, a: float, b: float, result: float) -> None:
        logging.info("%s(%.10g, %.10g) => %.10g", operation, a, b, result)
