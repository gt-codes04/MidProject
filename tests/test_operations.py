from app import operations as ops
from app.exceptions import ValidationError
import pytest

def test_add():
    assert ops.add(2, 3) == 5
    assert ops.add(-1, 1) == 0
    assert ops.add(0.1, 0.2) == pytest.approx(0.3)

def test_subtract():
    assert ops.subtract(5, 3) == 2
    assert ops.subtract(1, 1) == 0
    assert ops.subtract(0.3, 0.1) == pytest.approx(0.2)

def test_multiply():
    assert ops.multiply(2, 3) == 6
    assert ops.multiply(-2, 3) == -6
    assert ops.multiply(0.1, 0.1) == pytest.approx(0.01)

def test_divide_ok():
    assert ops.divide(10, 2) == 5
    assert ops.divide(-10, 2) == -5
    assert ops.divide(1, 2) == 0.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        ops.divide(1, 0)

def test_power():
    assert ops.power(2, 3) == 8
    assert ops.power(2, 0) == 1
    assert ops.power(2, -1) == 0.5

def test_root():
    assert ops.root(27, 3) == pytest.approx(3)
    assert ops.root(4, 2) == 2
    with pytest.raises(ValidationError, match="Root with zero degree is undefined"):
        ops.root(4, 0)

def test_modulus():
    assert ops.modulus(10, 3) == 1
    assert ops.modulus(-10, 3) == 2  # Python's modulo behavior
    with pytest.raises(ZeroDivisionError, match="Cannot modulus by zero"):
        ops.modulus(10, 0)

def test_int_divide():
    assert ops.int_divide(10, 3) == 3
    assert ops.int_divide(-10, 3) == -4  # Python's floor division behavior
    with pytest.raises(ZeroDivisionError, match="Cannot integer-divide by zero"):
        ops.int_divide(10, 0)

def test_percent():
    assert ops.percent(25, 100) == 25
    assert ops.percent(50, 200) == 25
    assert ops.percent(1, 3) == pytest.approx(33.333333)
    with pytest.raises(ZeroDivisionError, match="Cannot compute percentage with denominator zero"):
        ops.percent(25, 0)

def test_abs_diff():
    assert ops.abs_diff(10, 3) == 7
    assert ops.abs_diff(3, 10) == 7  # Commutative
    assert ops.abs_diff(-5, 5) == 10  # Works with negatives
    assert ops.abs_diff(0.1, 0.2) == pytest.approx(0.1)  # Works with decimals
