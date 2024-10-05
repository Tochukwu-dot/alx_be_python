# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test for addition
    def test_addition(self):
        # Correctly include self.assertEqual(self.calc.add(...))
        self.assertEqual(self.calc.add(5, 3), 8)  # This line must be present

    # Test for subtraction
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    # Test for multiplication
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    # Test for division
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    # Test for division by zero
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
