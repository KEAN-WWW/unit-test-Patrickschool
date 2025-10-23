"""Addition tests for Calculator.add."""

from app.calculator import Calculator

def test_addition_basic():
    """Basic addition test: 2 + 3 == 5"""
    calc = Calculator()
    assert calc.add(2, 3) == 5
