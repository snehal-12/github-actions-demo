import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,4), 7)
        self.assertEqual(add(-5,-6), -11)
        self.assertEqual(add(2.5,1), 3.50)

    def test_subtract(self):
        """Test the subtract function."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(5.5, 2.5), 3.0)

    def test_multiply(self):
        """Test the multiply function."""
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(2.5, 2), 5.0)

    def test_divide(self):
        """Test the divide function."""
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(5, 2), 2.5)

        # Test for division by zero
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()