""" Задача 1-10 - оберіть декілька домашніх завдань та покрийте їх не менш ніж 10 тестами.
Код закомітьте в гіт, надайте посилання.
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""

import unittest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from lession_06 import homeworks05_yuliia_turovska

class HomeworksTesting08(unittest.TestCase):

    def test_sum_of_positive(self):
        """Positive:
        Sum of 3+2
        """
        actual_result = homeworks05_yuliia_turovska.total_plus(3,2)
        expected_result = 5
        self.assertEqual(actual_result, expected_result, msg= "Incorrect actual result for Sum of 3+2! Actual result should be 5")


    def test_sum_of_negative(self):
        """Sum of negative values -3 + -2"""
        actual_result = homeworks05_yuliia_turovska.total_plus(-3, -2)
        expected_result = -5
        self.assertEqual(actual_result, expected_result, msg="Incorrect actual result for Sum of -3+ -2! Actual result should be -5")



    def test_sum_of_fractional(self):
        """Sum of fractional numbers 100.1, 1000.35"""
        actual_result = homeworks05_yuliia_turovska.total_plus(100.1, 1000.35)
        expected_result = 1100.45
        self.assertEqual(actual_result, expected_result, msg= "Incorrect actual result for Sum of 100.1, 1000.35! Actual result should be 1100.45")


    def test_arithmetic_mean_positive(self):
        """returns the arithmetic mean of 5,10,15"""
        actual_result = homeworks05_yuliia_turovska.numbers_list([5,10,15])
        expected_result = 10
        self.assertEqual(actual_result, expected_result, msg= "Incorrect actual result for the arithmetic mean of 5,10,15! Actual result should be 10")


    def test_arithmetic_mean_negative(self):
        """returns the arithmetic mean of negative values -10, -20, -30, -40"""
        actual_result = homeworks05_yuliia_turovska.numbers_list([-10, -20, -30, -40])
        expected_result = -25
        self.assertEqual(actual_result, expected_result, msg= "Incorrect actual result for the arithmetic mean of negative values -10, -20, -30, -40! Actual result should be -25")


    def test_test_arithmetic_mean_fractional(self):
        """returns the arithmetic mean of fractional numbers 100.5, 1.35, 15.6, 0"""
        actual_result = homeworks05_yuliia_turovska.numbers_list([100.5, 1.2, 15.6, 0])
        expected_result = 29.325
        self.assertEqual(actual_result, expected_result, msg= "Incorrect actual result for the arithmetic mean of fractional numbers 100.5, 1.35, 15.6, 0! Actual result should be 29.325")


    def test_test_arithmetic_mean_singlenum(self):
        """returns the arithmetic mean of single number"""
        actual_result = homeworks05_yuliia_turovska.numbers_list([7])
        expected_result = 7
        self.assertEqual(actual_result, expected_result, msg= "Incorrect actual result for the arithmetic mean of nof single number 7! Actual result should be 7")


    def test_unique_numbers_list(self):
        """unique elements of numbers list [3, 1, 4, 3]"""
        actual_result = homeworks05_yuliia_turovska.unique_elements([3, 1, 4, 3])
        expected_result = set([1, 3, 4])
        self.assertEqual(actual_result, expected_result, msg= "Incorrect actual result for the unique elements of numbers list [3, 1, 4, 3]! Actual result should be 1, 3, 4")


    def test_unique_numbers_string_list(self):
        """unique elements of string and number list ['a', 'b', 'a', 'c', 'd', 'b', 1]"""
        actual_result = homeworks05_yuliia_turovska.unique_elements(['a', 'b', 'a', 'c', 'd', 'b', 1])
        expected_result = set(['a', 'b', 'c', 'd', 1])
        self.assertEqual(actual_result, expected_result, msg = "Incorrect actual result for the unique elements of string and number list ['a', 'b', 'a', 'c', 'd', 'b', 1]! Actual result should be 'a', 'b', 'c', 'd', 1")


    def test_unique_empty_list(self):
        """unique elements of empty list"""
        actual_result = homeworks05_yuliia_turovska.unique_elements([])
        expected_result = set()
        self.assertEqual(actual_result, expected_result, msg = "Incorrect actual result for the unique elements of of empty list! Actual result should be empty list")


if __name__ == "__main__":
    unittest.main(verbosity=2)

