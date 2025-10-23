"""Multiplication tests for Calculator.multiply."""

from app.calculator import Calculator

def test_multiplication_basic():
    """Basic multiplication test: 6 * 7 == 42"""
    calc = Calculator()
    assert calc.multiply(6, 7) == 42
