import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_f_add(self):
        alpha = 10
        beta = 5
        result = self.calc.f_add(alpha, beta)
        self.assertEqual(result, 15)

    def test_f_subtract(self):
        alpha = 10
        beta = 5
        result = self.calc.f_subtract(alpha, beta)
        self.assertEqual(result, 5)

    def test_f_multiply(self):
        alpha = 10
        beta = 5
        result = self.calc.f_multiply(alpha, beta)
        self.assertEqual(result, 50)

    def test_f_divide(self):
        alpha = 10
        beta = 5
        result = self.calc.f_divide(alpha, beta)
        self.assertEqual(result, 2)

    def test_f_divide_by_zero(self):
        alpha = 10
        beta = 0
        with self.assertRaises(ValueError):
            self.calc.f_divide(alpha, beta)

    def test_f_square_root(self):
        alpha = 25
        result = self.calc.f_square_root(alpha)
        self.assertEqual(result, 5)

    def test_f_square_root_negative(self):
        alpha = -25
        with self.assertRaises(ValueError):
            self.calc.f_square_root(alpha)

if __name__ == '__main__':
    unittest.main()
