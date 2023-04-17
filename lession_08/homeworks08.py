import unittest
import sys 
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from lession_06.homeworks06 import*

class HWTestings (unittest.TestCase):
    def test_task01 (self):
        """the sum of two positive numbers"""
        actual_result = sum1(10, 5)
        expected_result = 15
        self.assertEqual(actual_result, expected_result, f"Sum of 10 and 5 is {sum1(10,5)}")
    
    def test_task02 (self):
        """the sum of two negative numbers"""
        actual_result = sum1(-10, -5)
        expected_result = -15
        self.assertEqual(actual_result, expected_result, "Sum of -10 and -5 is -15")
    
    def test_task03 (self):
        """the sum of positive and negative numbers """
        actual_result = sum1(-10,10)
        expected_result = 0
        self.assertEqual(actual_result, expected_result, "Sum of -10 and 10 is 0")
    
    def test_task04 (self):
        """the sum of one number and 0"""
        actual_result = sum1(10,0)
        expected_result = 10
        self.assertEqual(actual_result, expected_result, "Sum of 10 and 0 is 10")

    def test_task05 (self):
        """the sum of two zeros"""
        actual_result = sum1(0,0)
        expected_result = 0
        self.assertTrue(actual_result==expected_result, "Sum of two zeros is zero")

    def test_task06 (self):
        """sum of two float numbers"""
        actual_result = sum1(0.25, 0.75)
        expected_result = 1
        self.assertTrue(actual_result==expected_result, "Sum of 0.25 and 0.75 is 1")
    def test_task07 (self):
        """Arithmetic average of positive numbers"""
        actual_result = arithmetic_average([2,4,6,8])
        expected_result = 5
        self.assertEqual(actual_result, expected_result, "Average of 2,4,6,8 is 5")

    def test_task08 (self):
        """Arithmetic average of negative numbers"""
        actual_result = arithmetic_average([-2,-4,-6,-8])
        expected_result = -5
        self.assertEqual(actual_result,expected_result, "Average of -2,-4,-6,-8 is -5")
    
    def test_task09 (self):
        """Arithmetic average of positive and negative numbers"""
        actual_result = arithmetic_average([-5,5])
        expected_result = 0
        self.assertEqual(actual_result,expected_result, "Average of -5 and 5 is 0")
    
    def test_task10 (self):
        """Arithmetic average of zeros"""
        actual_result = arithmetic_average([0,0,0,0])
        expected_result = 0
        self.assertEqual(actual_result,expected_result, "Average of zeros is zero")
    
    def test_task11 (self):
        """Arithmetic average of float numbers"""
        actual_result = arithmetic_average([0.25, 0.75])
        expected_result = 0.5
        self.assertEqual(actual_result, expected_result, "Average of 0.25 and 0.75 is 0.5")
        
if __name__=="__main__":
    unittest.main(verbosity = 2)
