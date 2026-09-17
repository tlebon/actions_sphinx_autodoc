class Calculator:
    """
    A simple utility class for basic arithmetic operations.

    This class demonstrates how to use docstrings that are recognized
    by Sphinx's autodoc extension.
    """

    def add(self, a: float, b: float) -> float:
        """
        Adds two numbers.

        :param a: The first number.
        :param b: The second number.
        :return: The sum of a and b.
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Subtracts the second number from the first.

        :param a: The first number (minuend).
        :param b: The second number (subtrahend).
        :return: The difference between a and b.
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Multiplies two numbers.

        :param a: The first number.
        :param b: The second number.
        :return: The product of a and b.
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Divides the first number by the second.

        :param a: The first number (dividend).
        :param b: The second number (divisor).
        :raises ValueError: If b is zero.
        :return: The quotient of a and b.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
