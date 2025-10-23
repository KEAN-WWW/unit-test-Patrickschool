"""
Calculator module with basic arithmetic operations.
"""

class Calculator:
    """Simple calculator class."""

    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Return the difference of a and b."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Return the product of a and b."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Return the division of a by b. Raises ZeroDivisionError if b is 0."""
        return a / b  # Let Python naturally raise ZeroDivisionError
