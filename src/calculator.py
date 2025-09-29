"""
A simple calculator module for demonstrating CI/CD with Python.
"""


class Calculator:
    """A basic calculator class with arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b  # This line is too long and will cause flake8 to fail because it exceeds the line length limit

    def subtract(self, a: float, b: float) -> float:
        """Subtract second number from first."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide first number by second."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """Raise base to the power of exponent."""
        return base ** exponent


def main():
    """Main function for command-line usage."""
    calc = Calculator()
    print("Calculator Demo")
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"3 * 7 = {calc.multiply(3, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2^8 = {calc.power(2, 8)}")


if __name__ == "__main__":
    main()
