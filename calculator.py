# calculator.py


class Calculator:
    """A simple calculator class."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        if a == 0 or b == 0:
            raise ValueError("Multiplication by zero is not allowed")
        return a * b

    def divide(self, a, b):
        """Return the division of a by b.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
