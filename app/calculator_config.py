"""
Configuration settings for the calculator.
"""
import os
from dotenv import load_dotenv

load_dotenv()

class CalculatorConfig:
    MAX_HISTORY_SIZE = int(os.getenv('MAX_HISTORY_SIZE', 100))
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'calculator.log')