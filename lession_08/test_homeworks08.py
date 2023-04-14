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

    def test_task01(self):
        actual_result = homeworks06.sum_num(0,1000)
        expected_result = 1000
        self.assertEqual(actual_result, expected_result, msg=f"Actual result <{actual_result}> doesn't equal expected result <{expected_result}>")

    def test_task02(self):
        actual_result = homeworks06.sum_num(-1,-1)
        expected_result = -2
        self.assertEqual(actual_result, expected_result, msg=f"Actual result <{actual_result}> doesn't equal expected result <{expected_result}>")
    
    def test_task03(self):
        actual_result = homeworks06.sum_num(-3,7)
        expected_result = 4
        self.assertEqual(actual_result, expected_result, msg=f"Actual result <{actual_result}> doesn't equal expected result <{expected_result}>")
    
    def test_task04(self):
        str = ['apple', 'kiwi', 'cherry']
        actual_result = homeworks06.longest_word(str)
        expected_result = str[2]
        self.assertEqual(actual_result, expected_result, msg=f"Actual result <{actual_result}> doesn't equal expected result <{expected_result}>")

    def test_task05(self):
        str = ['a', 'b', 'c']
        actual_result = homeworks06.longest_word(str)
        expected_result = str[2]
        self.assertEqual(actual_result, expected_result, msg=f"Actual result <{actual_result}> doesn't equal expected result <{expected_result}>")
    
    def test_task06(self):
        str = ['a']
        actual_result = homeworks06.longest_word(str)
        expected_result = str[0]
        self.assertEqual(actual_result, expected_result, msg=f"Actual result <{actual_result}> doesn't equal expected result <{expected_result}>")

    def test_task07(self):
        actual_result = homeworks06.digits_sum(12000345)
        expected_result = 15
        self.assertEqual(actual_result, expected_result, msg=f"Actual result <{actual_result}> doesn't equal expected result <{expected_result}>")

    def test_task08(self):
        actual_result = homeworks06.digits_sum(0)
        expected_result = 0
        self.assertEqual(actual_result, expected_result, msg=f"Actual result <{actual_result}> doesn't equal expected result <{expected_result}>")    

    def test_task09(self):
        actual_result = homeworks06.digits_sum(2147483647)
        expected_result = 46
        self.assertEqual(actual_result, expected_result, msg=f"Actual result <{actual_result}> doesn't equal expected result <{expected_result}>")   

    def test_task10(self):
        actual_result = homeworks06.digits_sum(1)
        expected_result = 1
        self.assertEqual(actual_result, expected_result, msg=f"Actual result <{actual_result}> doesn't equal expected result <{expected_result}>")  



if __name__ == "__main__":
    unittest.main()
    