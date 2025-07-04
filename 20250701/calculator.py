class Calculator:
    def __init__(self):
        self._result: float = 0

    def add(self, a: int, b: int):
        self._result = a + b

    def subtract(self, a: int, b: int):
        self._result = a - b

    def multiply(self, a: int, b: int):
        self._result = a * b

    def divide(self, a: int, b: int):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self._result = a / b

    def reset(self):
        self._result = 0

    def print_result(self):
        print(f"Result: {self._result}")


class User:
    def __init__(self):
        self.calculator = Calculator()

    def perform_calculation(self, operation, a=None, b=None):
        if operation != 'reset' and (a is None or b is None):
            raise ValueError("Both operands must be provided for this operation")
        if operation == 'add':
            self.calculator.add(a, b)
        elif operation == 'subtract':
            self.calculator.subtract(a, b)
        elif operation == 'multiply':
            self.calculator.multiply(a, b)
        elif operation == 'divide':
            self.calculator.divide(a, b)
        elif operation == 'reset':
            self.calculator.reset()
        else:
            raise ValueError("Invalid operation")

        self.calculator.print_result()


if __name__ == "__main__":
    user = User()
    user.perform_calculation('add', 5, 3)
    user.perform_calculation('subtract', 10, 4)
    user.perform_calculation('multiply', 2, 6)
    user.perform_calculation('divide', 8, 2)
    user.perform_calculation('reset')

    try:
        user.perform_calculation('divide', 8, 0)
    except ValueError as e:
        print(e)
