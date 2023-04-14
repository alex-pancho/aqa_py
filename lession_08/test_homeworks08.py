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

class TestSubstringInMainString(unittest.TestCase):


    def test_subtring_included_to_first_place_mainstring(self):
        '''Substring is included to fist place main string'''
        str1 = "The quick brown fox jumps over the lazy dog"
        str2 = "The"
        actual_result = homeworks06.find_substring(str1, str2)
        expected_result = 0
        self.assertTrue(actual_result == expected_result, msg=f"Substring <{str2}> don't get {expected_result} index in <{str1}>")
       

    def test_subtring_included_end_mainstring(self):
        '''Substring is included to end main string'''
        str1 = "The quick brown fox jumps over the lazy dog"
        str2 = "dog"
        actual_result = homeworks06.find_substring(str1, str2)
        expected_result = 40
        self.assertEqual(actual_result, expected_result, msg=f"Substring <{str2}> don't get {expected_result} index in <{str1}>")


    def test_subtring_included_middle_mainstring(self):
        '''Substring is included to end main string without spaces'''
        str1 = "Thequickbrownfoxjumpsoverthelaz&nbspdog"
        str2 = "fox"
        actual_result = homeworks06.find_substring(str1, str2)
        expected_result = 13
        self.assertEqual(actual_result, expected_result, msg=f"Substring <{str2}> don't get {expected_result} index in <{str1}>")


    def test_subtring_included_mainstring_no_spases(self):
        '''Substring is included to end main string without spaces'''
        str1 = "Thequickbrownfoxjumpsoverthelazdog"
        str2 = "fox"
        actual_result = homeworks06.find_substring(str1, str2)
        expected_result = 13
        self.assertEqual(actual_result, expected_result, msg=f"Substring <{str2}> don't get {expected_result} index in <{str1}>")


    def test_subtring_included_ua_mainstring(self):
        '''Substring is included to end main string without spaces'''
        str1 = "Русні прийде скоро ..зда"
        str2 = "скоро"
        actual_result = homeworks06.find_substring(str1, str2)
        expected_result = 13
        self.assertEqual(actual_result, expected_result, msg=f"Substring <{str2}> don't get {expected_result} index in <{str1}>")


    def test_subtring_included_ch_mainstring(self):
        '''Substring is included to end main string without spaces'''
        str1 = "举案齐眉"
        str2 = "齐"
        actual_result = homeworks06.find_substring(str1, str2)
        expected_result = 2
        self.assertEqual(actual_result, expected_result, msg=f"Substring <{str2}> don't get {expected_result} index in <{str1}>")


    def test_subtring_is_not_included_to_mainstring(self):
        '''Substring isn't included to main string'''
        str1 = "The quick brown fox jumps over the lazy dog"
        str2 = "cat"
        actual_result = homeworks06.find_substring(str1, str2)
        expected_result = -1
        self.assertEqual(actual_result, expected_result, msg=f"Substring <{str2}> don't get {expected_result} index in <{str1}>")


class TestGetMaxLenWordLst(unittest.TestCase):

    def test_get_maxlenght_word_in_first_place_in_list(self):
        '''Getting first word with max lenght in list'''
        lst_words = ["Написати", "функцію", "яка", "приймає", "список", "слів"]    
        actual_result = homeworks06.get_maximum_length_word_list(lst_words)
        expected_result = "Написати"
        self.assertEqual(actual_result, expected_result, msg=f"Word <{actual_result}> does not match the <{expected_result}>")


    def test_get_maxlenght_word_in_last_place_in_list(self):
        '''Getting word with max lenght in last plase in list'''
        lst_words = ["функцію", "яка", "приймає", "список", "слів", "Написатитут"]    
        actual_result = homeworks06.get_maximum_length_word_list(lst_words)
        expected_result = "Написатитут"
        self.assertEqual(actual_result, expected_result, msg=f"Word <{actual_result}> does not match the <{expected_result}>")


    def test_empty_list(self):
        lst_words = []
        expected_result = "Empty list. Please, try again..."
        actual_result = homeworks06.get_maximum_length_word_list(lst_words)
        self.assertEqual(actual_result, expected_result, msg=f"Word <{actual_result}> does not match the <{expected_result}>")


    def test_get_error_due_to_diffrent_cases_in_words(self):
        '''Getting word with max lenght in last plase in list'''
        lst_words = ["слівсловасловаслова", "яка", "приймає", "список", "слів", "Написатитут"]    
        actual_result = homeworks06.get_maximum_length_word_list(lst_words)
        expected_result = "Слівсловасловаслова"
        self.assertNotEqual(actual_result, expected_result, msg=f"Word <{actual_result}> does not match the <{expected_result}>")


    def test_list_with_one_word(self):
        lst_words = ['hillel']
        expected_result = 'hillel'
        actual_result = homeworks06.get_maximum_length_word_list(lst_words)
        self.assertEqual(actual_result, expected_result)
