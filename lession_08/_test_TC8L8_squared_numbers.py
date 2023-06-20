import unittest
from functions_to_test import squared_numbers


class TestHomeworks8(unittest.TestCase):

    def test01(self):  # Equivalence partitioning.
        """Positive:
        Case send positive numbers list
        """
        actual_result = squared_numbers(numbers_list=[1, 2, 3, 4, 5])
        expected_result = [4, 16]
        self.assertEqual(actual_result, expected_result)

    def test02(self):  # Equivalence partitioning.
        """Positive:
        Case send negative numbers list
        """
        actual_result = squared_numbers(numbers_list=[-1, -2, -3, -4, -5])
        expected_result = [4, 16]
        self.assertEqual(actual_result, expected_result)

    def test03(self):  # Equivalence partitioning.
        """
        Negative:
        Case send list with 0 values
        """
        actual_result = squared_numbers(numbers_list=[0, 0, 0])
        expected_result = [0, 0, 0]
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
