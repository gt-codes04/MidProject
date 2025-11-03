from app.input_validators import to_float, validate_two_numbers
from app.exceptions import ValidationError
import pytest

def test_to_float_valid():
    assert to_float("1.23") == 1.23
    assert to_float("-1.23") == -1.23
    assert to_float("0") == 0.0
    assert to_float("1e6") == 1000000.0

def test_to_float_invalid():
    with pytest.raises(ValidationError, match="Invalid numeric input"):
        to_float("abc")
    with pytest.raises(ValidationError, match="Invalid numeric input"):
        to_float("")
    with pytest.raises(ValidationError, match="Invalid numeric input"):
        to_float(None)

def test_validate_two_numbers_valid():
    a, b = validate_two_numbers("1.23", "4.56")
    assert a == 1.23
    assert b == 4.56
    
    # Test negative numbers
    a, b = validate_two_numbers("-1.23", "-4.56")
    assert a == -1.23
    assert b == -4.56

def test_validate_two_numbers_exceeds_max():
    with pytest.raises(ValidationError, match="Input exceeds allowed magnitude"):
        validate_two_numbers("1e13", "1")  # Should exceed default max of 1e12
    
    with pytest.raises(ValidationError, match="Input exceeds allowed magnitude"):
        validate_two_numbers("1", "1e13")