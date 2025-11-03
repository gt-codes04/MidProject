# app/exceptions.py
class CalculatorError(Exception):
    """Base error for the calculator app."""
    pass

class OperationError(CalculatorError):
    """Unsupported/invalid operation."""
    pass

class ValidationError(CalculatorError):
    """Bad or out-of-range input."""
    pass

# Backwards-compatible aliases/narrower names used elsewhere in the codebase.
class InvalidExpressionError(ValidationError):
    """Raised when the expression is invalid (alias for ValidationError)."""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""
    pass

__all__ = [
    "CalculatorError",
    "OperationError",
    "ValidationError",
    "InvalidExpressionError",
    "DivisionByZeroError",
]
