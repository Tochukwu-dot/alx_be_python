# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to return the product of two numbers, referencing class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Example usage
if __name__ == "__main__":
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}")  # Output: 15

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"Product: {product_result}")  # Output: 50
