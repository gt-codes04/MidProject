from .exceptions import ValidationError

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def power(a, b): return a ** b

def root(a, b):
    if b == 0:
        raise ValidationError("Root with zero degree is undefined")
    return a ** (1 / b)

def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot modulus by zero")
    return a % b

def int_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot integer-divide by zero")
    return a // b

def percent(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot compute percentage with denominator zero")
    return (a / b) * 100

def abs_diff(a, b): return abs(a - b)
