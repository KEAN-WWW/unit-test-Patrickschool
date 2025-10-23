"""Tests for the Calculator class: addition, subtraction, multiplication, division."""

import pytest
from app.calculator import Calculator

def test_addition():
    """Addition: 5 + 3 == 8"""
    calc = Calculator()
    assert calc.add(5, 3) == 8

def test_subtraction():
    """Subtraction: 10 - 4 == 6"""
    calc = Calculator()
    assert calc.subtract(10, 4) == 6

def test_multiplication():
    """Multiplication: 3 * 4 == 12"""
    calc = Calculator()
    assert calc.multiply(3, 4) == 12

def test_division():
    """Division: 10 / 2 == 5"""
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    """Division by zero raises ZeroDivisionError"""
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)
