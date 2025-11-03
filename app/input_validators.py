from .exceptions import ValidationError
from .calculator_config import Config

def to_float(x):
    try:
        return float(x)
    except Exception as e:
        raise ValidationError(f"Invalid numeric input: {x}") from e

def validate_two_numbers(a, b):
    a = to_float(a)
    b = to_float(b)
    maxv = Config.get_max_input_value()
    if abs(a) > maxv or abs(b) > maxv:
        raise ValidationError(f"Input exceeds allowed magnitude (>|{maxv}|).")
    return a, b
