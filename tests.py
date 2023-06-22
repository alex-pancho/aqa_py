""" Задача 1-10 - оберіть декілька домашніх завдань та покрийте їх не менш ніж 10 тестами.
Код закомітьте в гіт, надайте посилання.
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""

import unittest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from lession_06.homeworks06 import sum_two_nums

class TestTesting(unittest.TestCase):


    def test_task01(self):
        """Sum of two nums"""
        actual_result = sum_two_nums(2, 6)
        expected_result = 8
        self.assertEqual(actual_result, expected_result, f"Sum of 2 and 6 is {sum_two_nums(2, 6)}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
