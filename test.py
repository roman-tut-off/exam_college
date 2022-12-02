import unittest
from main import sum_digit


class TestSum(unittest.TestCase):
    def test_empty(self):
        with self.assertRaises(TypeError):
            sum_digit('')

    def test_str(self):
        with self.assertRaises(TypeError):
            sum_digit('qwerty')

    def test_float(self):
        with self.assertRaises(TypeError):
            sum_digit('132.5')

    def test_int(self):
        self.assertEqual(sum_digit('123'), 6)


if __name__ == '__main__':
    unittest.main()
