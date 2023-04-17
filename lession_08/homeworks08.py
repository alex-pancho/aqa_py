""" Задача 1-10 - оберіть декілька домашніх завдань та покрийте їх не менш ніж 10 тестами.
Код закомітьте в гіт, надайте посилання.
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
import unittest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from lession_06.homeworks06 import *

class TestSumNumbers(unittest.TestCase):

    def test_sum_integer_numbers(self):
        """The sum of integer numbers"""
        first = 2
        second = 2
        actual_result = sum_numbers(first, second)
        expected_result = 4
        self.assertEqual(actual_result, expected_result, msg=f"The sum of the numbers {first} and {second} not equals {expected_result}")


    def test_sum_float_numbers(self):
        """The sum of float numbers"""
        first = 0.5
        second = 1.23
        actual_result = sum_numbers(first, second)
        expected_result = 1.73
        self.assertEqual(actual_result, expected_result, msg=f"The sum of the numbers {first} and {second} not equals {expected_result}")

    def test_sum_negative_numbers(self):
        """The sum of negative numbers"""
        first = -2
        second = -6
        actual_result = sum_numbers(first, second)
        expected_result = -8
        self.assertEqual(actual_result, expected_result, msg=f"The sum of the numbers {first} and {second} not equals {expected_result}")

    def test_sum_positive_and_negative_numbers(self):
        """The sum of positive and negative numbers"""
        first = 2
        second = -6
        actual_result = sum_numbers(first, second)
        expected_result = -4
        self.assertEqual(actual_result, expected_result, msg=f"The sum of the numbers {first} and {second} not equals {expected_result}")

    def test_sum_float_and_negative_numbers(self):
        """The sum of float and negative numbers"""
        first = -15
        second = 61.35
        actual_result = sum_numbers(first, second)
        expected_result = 46.35
        self.assertEqual(actual_result, expected_result, msg=f"The sum of the numbers {first} and {second} not equals {expected_result}")

class TestSubstringIndex(unittest.TestCase):

    def test_first_occurrence_substring_in_string(self):
        """Index of first occurrence of substring in string"""
        str1 = "The quick brown fox jumps over the lazy dog very quickly !&#?"
        str2 = "The"
        actual_result = find_substring(str1, str2)
        expected_result = 0
        self.assertTrue(actual_result == expected_result, msg="Index of first occurrence of substring in string must be 0")

    def test_first_occurrence_substring_in_string_without_letters(self):
        """Index of first occurrence of substring in string without letters"""
        str1 = "34 35656 754!&#3 12?"
        str2 = "?"
        actual_result = find_substring(str1, str2)
        expected_result = 19
        self.assertTrue(actual_result == expected_result, msg="Index of first occurrence of substring in string withoust letters must be 19")

    def test_first_occurrence_substring_in_string_without_spaces(self):
        """Index of first occurrence of substring in string without spaces"""
        str1 = "Theworld1032@itewsa.com?"
        str2 = "@"
        actual_result = find_substring(str1, str2)
        expected_result = 12
        self.assertTrue(actual_result == expected_result, msg="Index of first occurrence of substring in string withoust spaces must be 12")

    def test_first_occurrence_substring_in_string_with_only_special_symbols(self):
        """Index of first occurrence of substring in string with only special symbols"""
        str1 = "!№;%:?*()_+,<>"
        str2 = "+"
        actual_result = find_substring(str1, str2)
        expected_result = 10
        self.assertTrue(actual_result == expected_result, msg="Index of first occurrence of substring in string with only special symbols must be 10")

    def test_absence_substring_in_string(self):
        """Substring isn't in string"""
        str1 = "The quick brown fox jumps over the lazy dog very quickly !&#?"
        str2 = "@"
        actual_result = find_substring(str1, str2)
        expected_result = -1
        self.assertTrue(actual_result == expected_result, msg="Index of the missing substring in string must be equal to -1")

if __name__ == "__main__":
    unittest.main(verbosity=2)
