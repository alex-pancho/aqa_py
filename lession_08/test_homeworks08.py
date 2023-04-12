""" Задача 1-10 - оберіть декілька домашніх завдань та покрийте їх не менш ніж 10 тестами.
Код закомітьте в гіт, надайте посилання.
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""


import unittest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from lession_06 import homeworks06

class HomeworksTesting(unittest.TestCase):

    def test_subtring_is_included_to_first_place_mainstring_positive_case(self):
        '''Substring is included to main string'''
        str1 = "The quick brown fox jumps over the lazy dog"
        str2 = "The"
        actual_result = homeworks06.find_substring(str1, str2)
        expected_result = 0
        self.assertEqual(actual_result, expected_result, f"Substring {str2} is located in {str1}")

    def test_subtring_is_not_included_to_mainstring_negative_case(self):
        '''Substring isn't included to main string'''
        str1 = "The quick brown fox jumps over the lazy dog"
        str2 = "cat"
        actual_result = homeworks06.find_substring(str1, str2)
        expected_result = -10
        self.assertEqual(actual_result, expected_result, f"Substring {str2} isn't located in {str1}")