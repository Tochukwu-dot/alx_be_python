# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test for addition (fixing the naming and syntax)
    def test_addition(self):
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)

    # Test for subtraction
    def test_subtraction(self):
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)

    # Test for multiplication
    def test_multiplication(self):
        result = self.calc.multiply(4, 3)
        self.assertEqual(result, 12)

    # Test for division
    def test_division(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    # Test for division by zero
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
