import unittest
from lession_10_code import *
from my_logger import logger
# Тестування виключень
class TestDivide(unittest.TestCase):
    def test_divide_by_zero(self):
        """test for raise exception"""
        logger.info("divide, 10, 0")
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

    def test_sum(self):
        """test for raise exception"""
        logger.info("calculate_sum, 10, 0")
        self.assertRaises(InvalidInputException, calculate_sum, 10, "0")


if __name__ == '__main__':
    unittest.main(verbosity=2)
