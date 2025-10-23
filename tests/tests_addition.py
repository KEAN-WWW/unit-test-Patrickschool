import pytest
from app.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 5) == 4
    assert calc.add(0, 0) == 0
