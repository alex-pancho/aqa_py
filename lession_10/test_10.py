import unittest
from lession_10_code import *
from my_logger import logger
# Тестування виключень
class TestDivide(unittest.TestCase):
    def test_divide_by_zero(self):
        "test for raise exception"
        logger.info("create exception")
        #self.assertRaises(ZeroDivisionError, calculate_sum, 10, 0)
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
