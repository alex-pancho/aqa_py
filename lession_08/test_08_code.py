import unittest
#import sys
#import pathlib
#sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from lession_06 import lession_06_code


class HomeworksTesting(unittest.TestCase):

    def test_task01(self):
        actual_result = lession_06_code.square(2)
        expected_result = 4
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()
