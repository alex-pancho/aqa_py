import unittest
import sys
import pathlib
import home_work_6
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))


class HomeWorksTesting(unittest.TestCase):

    def test_summ_two_numbers_positive_nums(self):
        """Test summ of two numbers with use only positive nums"""
        actual_result = home_work_6.summ_two_numbers(50, 37)
        expected_result = 87
        self.assertEqual(actual_result, expected_result, msg=f"invalid summ, num_1 + num_2 != expected_result")
        self.assertIsInstance(actual_result, (int, float), msg="type of test data is not int or float")

    def test_summ_two_numbers_negative_num(self):
        """Test summ of two numbers when one from numbers is negative"""
        actual_result = home_work_6.summ_two_numbers(-19, 25)
        expected_result = 6
        self.assertEqual(actual_result, expected_result, msg="invalid summ, num_1 + num_2 != expected_result")
        self.assertIsInstance(actual_result, (int, float), msg="type of test data is not int or float")

    def test_summ_two_numbers_zeroes(self):
        """Test summ of two numbers with zeroes"""
        actual_result = home_work_6.summ_two_numbers(0, 0)
        expected_result = 0
        self.assertEqual(actual_result, expected_result, msg='invalid summ, 0 + 0 must be 0')

    def test_summ_two_numbers_negative_summ(self):
        """Test summ of two numbers when their summ is negative number"""
        actual_result = home_work_6.summ_two_numbers(-7, -2)
        expected_result = -9
        self.assertEqual(actual_result, expected_result, msg='invalid summ, num_1 + num_2 != expected_result')
        self.assertIsInstance(actual_result, (int, float), msg="type of test data is not int or float")

    def test_summ_two_numbers_float(self):
        """Test summ of two numbers when 1 or 2 numbers are float type"""
        actual_result = home_work_6.summ_two_numbers(-1.6, 4)
        expected_result = 2.4
        self.assertEqual(actual_result, expected_result, msg='invalid summ, num_1 + num_2 != expected_result')
        self.assertIsInstance(expected_result, float, msg='expected result is not float type')

        actual_result = home_work_6.summ_two_numbers(2.2, 4.5)
        expected_result = 6.7
        self.assertEqual(actual_result, expected_result, msg='invalid summ, num_1 + num_2 != expected_result')
        self.assertIsInstance(expected_result, float, msg='expected result is not float type')

    def test_find_duplicates_yes(self):
        """Positive scenario test when duplicates in data"""
        actual_result = home_work_6.find_duplicates(1, 3, 5, 7, 'python', 1, 'python')
        expected_result = 'Дублікати є'
        self.assertEqual(actual_result, expected_result, msg='Дублікатів нема')

    def test_find_duplicate_no(self):
        """Positive scenario test when duplicates not in data"""
        actual_result = home_work_6.find_duplicates('My', 'name', 'is', 'Denys')
        expected_result = 'Дублікатів нема'
        self.assertEqual(actual_result, expected_result, msg='Дублікати є')

    def test_find_substring_yes(self):
        """Positive scenario test when string_1 contain string_2"""
        actual_result = home_work_6.find_substring('my cat is big', 'cat')
        expected_result = 3
        self.assertEqual(actual_result, expected_result, msg='string_2 not in string_1')

    def test_find_substring_no(self):
        """Positive scenario test when string_1 not contain string_2"""
        actual_result = home_work_6.find_substring('my cat is big', 'dog')
        expected_result = -1
        self.assertEqual(actual_result, expected_result, msg='string_2 in string_1')

    def test_of_type_even_numbers(self):
        """Test type of returned data for squares even numbers"""
        actual_result = home_work_6.even_numbers(1, 2, 3, 4, 5)
        expected_result = list
        self.assertIsInstance(actual_result, expected_result, msg='returned data not in list type')


if __name__ == "main":
    unittest.main(verbosity=2)
