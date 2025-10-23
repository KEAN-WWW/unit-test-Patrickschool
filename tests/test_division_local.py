"""
Local division tests for Calculator.
"""

import pytest
from app.calculator import Calculator

def test_divide_local():
    """Test more division cases."""
    calc = Calculator()
    assert calc.divide(9, 3) == 3
    assert calc.divide(-8, -2) == 4
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)
