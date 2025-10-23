"""Basic division tests for Calculator.divide."""

from app.calculator import Calculator

def test_division_basic():
    """Basic division test: 9 / 3 == 3"""
    calc = Calculator()
    assert calc.divide(9, 3) == 3
