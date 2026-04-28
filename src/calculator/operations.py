
class Calculator:

    # Basic arithmetic operations
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        return a / b



calc = Calculator()
print(calc.add(2, 3))        # Output: 5
print(calc.subtract(10, 5))  # Output: 5
print(calc.multiply(2, 3))   # Output: 6
print(calc.divide(10, 2))    # Output: 5
