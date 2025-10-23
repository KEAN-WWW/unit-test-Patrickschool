"""
Unit tests for the Calculator class.
"""

import pytest
from app.calculator import Calculator

def test_add():
    """Test addition."""
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    """Test subtraction."""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

def test_multiply():
    """Test multiplication."""
    calc = Calculator()
    assert calc.multiply(3, 4) == 12

def test_divide():
    """Test division."""
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    """Test divide by zero raises ZeroDivisionError."""
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)
