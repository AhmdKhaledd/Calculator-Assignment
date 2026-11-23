
import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# ADDITION TESTS

def test_add_positive_numbers(calc):
    assert calc.add(5, 3) == 8

def test_add_negative_numbers(calc):
    assert calc.add(-5, -3) == -8

def test_add_zero(calc):
    assert calc.add(5, 0) == 5


# SUBTRACTION TESTS

def test_subtract_positive_numbers(calc):
    assert calc.subtract(10, 4) == 6

def test_subtract_negative_result(calc):
    assert calc.subtract(3, 8) == -5

def test_subtract_zero(calc):
    assert calc.subtract(7, 0) == 7


# MULTIPLICATION TESTS

def test_multiply_positive_numbers(calc):
    assert calc.multiply(4, 5) == 20

def test_multiply_negative_numbers(calc):
    assert calc.multiply(-4, 5) == -20

def test_multiply_by_zero(calc):
    assert calc.multiply(10, 0) == 0


# DIVISION TESTS

def test_divide_positive_numbers(calc):
    assert calc.divide(10, 2) == 5

def test_divide_decimal_result(calc):
    assert calc.divide(5, 2) == 2.5

def test_divide_negative_numbers(calc):
    assert calc.divide(-10, 2) == -5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)
