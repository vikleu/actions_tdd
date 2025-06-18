# calculator.py

import math
import numpy as np


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
            raise ValueError("Multiplication by zero either a or b is not possible")
        return a * b

    def divide(self, a, b):
        """Return the division of a by b.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        """Return a raised to the power of b using math.pow."""
        return math.pow(a, b)

    def sqrt(self, a):
        """Return the square root of a using numpy.sqrt."""
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return np.sqrt(a)
