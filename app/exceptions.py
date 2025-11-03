"""
Custom exceptions for the calculator application.
"""

class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass

class InvalidExpressionError(CalculatorError):
    """Raised when the expression is invalid."""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""
    pass