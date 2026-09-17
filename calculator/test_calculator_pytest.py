import pytest
from calculator.calculator import Calculator

# --- Fixtures (Best Practice for Classes) ---


@pytest.fixture
def calculator():
    """Provides a fresh Calculator instance for every test."""
    return Calculator()

# --- Standard Assertions ---


def test_subtract(calculator):
    assert calculator.subtract(10, 5) == 5
    assert calculator.subtract(-1, -1) == 0


def test_multiply(calculator):
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-1, 5) == -5
    assert calculator.multiply(0, 100) == 0


def test_divide(calculator):
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(5, 2) == 2.5

# --- Exception Handling ---


def test_divide_by_zero(calculator):
    # pytest.raises checks that the specific exception is thrown
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.divide(10, 0)

# --- Parametrized Tests (Best Practice) ---


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),          # Positive numbers
    (-1, 1, 0),         # Mixed signs
    (-5, -5, -10),      # Negative numbers
    (0, 0, 0),          # Zeros
    (1.5, 2.5, 4.0)     # Floats
])
def test_add(calculator, a, b, expected):
    """Testing addition using parametrization to run multiple data sets."""
    assert calculator.add(a, b) == expected
