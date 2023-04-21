import unittest
import sys 
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
#from lession_06 import lession_06_code
from lession_06.lession_06_code import *
from lession_06.homeworks06 import avg_arifmethic

class HomeworksTesting(unittest.TestCase):

    PI = 3.14

    def test_task01(self):
        """Square of 2"""
        actual_result = square(2)
        expected_result = 4
        self.assertEqual(actual_result, expected_result, f"Square of 2 is {square(2)}")

    def test_task02(self):
        """Square of 3"""
        actual_result = square(3)
        expected_result = 9
        self.assertEqual(actual_result, expected_result)

    def test_task03(self):
        """avg_arifmethic, positive num"""
        actual_result = avg_arifmethic(1,1,1,1,1,1,1)
        expected_result = 1
        self.assertEqual(actual_result, expected_result)
        self.assertTrue(actual_result==expected_result, msg="")
        self.assertEqual(self.PI, 3.14)

if __name__ == "__main__":
    unittest.main(verbosity=1)
