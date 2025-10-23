"""Local division test file for Calculator.divide."""

from app.calculator import Calculator

def test_division_local():
    """Local division test: 12 / 4 == 3"""
    calc = Calculator()
    assert calc.divide(12, 4) == 3
