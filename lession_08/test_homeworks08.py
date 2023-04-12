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

    def test_find_substrin_positive(self):
        str1 = "The quick brown fox jumps over the lazy dog"
        str2 = "cat"
        actual_result = homeworks06.find_substring(str1, str2)
        expected_result = -1
        self.assertEqual(actual_result, expected_result, f"Substring {str2} isn't located in {str1}")
