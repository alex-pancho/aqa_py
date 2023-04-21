import unittest
from functions_to_test import find_substring


class TestHomeworks9(unittest.TestCase):

    def test01(self):  # Equivalence partitioning.
        """Positive:
        send text1 and text2 which in text1"""
        actual_result = find_substring(text1="Hello, world!", text2="world")
        expected_result = 7
        self.assertEqual(actual_result, expected_result)

    def test02(self):  # Equivalence partitioning.
        """Negative:
        send text1 and text2 which not in text1"""
        actual_result = find_substring(text1="The quick brown fox jumps over the lazy dog", text2='cat')
        expected_result = -1
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
