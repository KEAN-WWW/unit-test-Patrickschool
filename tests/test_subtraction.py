"""Subtraction tests for Calculator.subtract."""

from app.calculator import Calculator

def test_subtraction_basic():
    """Basic subtraction test: 20 - 8 == 12"""
    calc = Calculator()
    assert calc.subtract(20, 8) == 12
