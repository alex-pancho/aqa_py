import unittest
from functions_to_test import numbers_list_average


class HomeworksTesting6(unittest.TestCase):

    def test01(self):  # Equivalence partitioning.
        """ Positive:
        Case send positive numbers list
        """
        actual_result = numbers_list_average(numbers_list=[1, 2, 3, 4, 5])
        expected_result = 3
        self.assertEqual(actual_result, expected_result)

    def test02(self):  # Equivalence partitioning.
        """ Positive:
        Case send negative numbers list
        """
        actual_result = numbers_list_average(numbers_list=[-1, -2, -3, -4, -5])
        expected_result = -3
        self.assertEqual(actual_result, expected_result)

    def test03(self):  # Equivalence partitioning.
        """ Positive:
        Case send list with all values equal 0
        """
        actual_result = numbers_list_average(numbers_list=[0, 0, 0])
        expected_result = 0
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
