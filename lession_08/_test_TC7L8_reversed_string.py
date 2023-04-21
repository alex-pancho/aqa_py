import unittest
from functions_to_test import reversed_string


class HomeworksTesting7(unittest.TestCase):

    def test01(self):
        """
        Positive:
        Case send string
        """
        actual_result = reversed_string(text='!evoL 1 nohtyP')
        expected_result = 'Python 1 Love!'
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)

