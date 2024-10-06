import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(3,2), 1)
        self.assertEqual(self.calc.subtract(1,-1), 0)
        self.assertEqual(self.calc.subtract(0,0), 0)
        self.assertEqual(self.calc.subtract(2.5,2), .5)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2,3), 6)
        self.assertEqual(self.calc.multiply(2,-2), -4)
        self.assertEqual(self.calc.multiply(-2,-2), 4)
        self.assertEqual(self.calc.multiply(0,3), 0)

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(3,3), 1)
        self.assertEqual(self.calc.divide(0,3), 0)
        self.assertEqual(self.calc.divide(3,-3), -1)
        self.assertEqual(self.calc.divide(-3,-3), 1)
# Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == '__main__':
    unittest.main()