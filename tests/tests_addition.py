"""
Unit tests for addition in Calculator.
"""

from app.calculator import Calculator

def test_add():
    """Test addition."""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
