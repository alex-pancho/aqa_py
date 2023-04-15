import unittest
from functions_to_test import keys_to_values_changing


class TestHomeWorks10(unittest.TestCase):

    def test01(self):
        """Positive:
        Case send correct dict args"""
        actual_result = keys_to_values_changing(args_dict={'a': 1, 'b': 2, 'c': 3})
        expected_result = {1: 'a', 2: 'b', 3: 'c'}
        self.assertEqual(actual_result, expected_result)


if __name__ == 'main':
    unittest.main(verbosity=2)
