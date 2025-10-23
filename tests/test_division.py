"""
Unit tests for division in Calculator.
"""

import pytest
from app.calculator import Calculator

def test_divide():
    """Test normal division."""
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(-6, 3) == -2

def test_divide_by_zero():
    """Test divide by zero raises ZeroDivisionError."""
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)
