import pytest
from app.calculator import Calculator

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    assert calc.divide(-6, 2) == -3

def test_divide_zero_exception():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)
