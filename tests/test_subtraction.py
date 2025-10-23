"""
Unit tests for subtraction in Calculator.
"""

from app.calculator import Calculator

def test_subtract():
    """Test subtraction."""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 0) == 0
    assert calc.subtract(-1, -1) == 0
