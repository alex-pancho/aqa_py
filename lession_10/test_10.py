import unittest
from lession_10_code import *

class TestDivide(unittest.TestCase):
    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, calculate_sum, 10, 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
