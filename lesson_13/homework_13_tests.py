import unittest
import homeworks_13 as hw

class HomeworksTesting(unittest.TestCase):

    def test_task01(self):
        actual_result = hw.man_3.name
        expected_result = "Joakim"
        self.assertEqual(actual_result, expected_result, msg=f"Actual result is: {actual_result} instead of Expected result: {expected_result}")
        actual_result = hw.man_3.last_name
        expected_result = "Broden"
        self.assertEqual(actual_result, expected_result, msg=f"Actual result is: {actual_result} instead of Expected result: {expected_result}")

    def test_task02(self):
        actual_result = hw.man_3.do_homework()
        expected_result = 10
        self.assertEqual(actual_result, expected_result, msg=f"Actual result is: {actual_result} instead of Expected result: {expected_result}")

    def test_task03(self):
        actual_result = hw.man_3.eat()
        expected_result = 15
        self.assertEqual(actual_result, expected_result, msg=f"Actual result is: {actual_result} instead of Expected result: {expected_result}")
    
    def test_task04(self):
        actual_result = hw.man_3.sleep()
        expected_result = 25
        self.assertEqual(actual_result, expected_result, msg=f"Actual result is: {actual_result} instead of Expected result: {expected_result}")

    def test_task05(self):
        actual_result = hw.man_3.speak()
        expected_result = 200
        self.assertEqual(actual_result, expected_result, msg=f"Actual result is: {actual_result} instead of Expected result: {expected_result}")

    def test_task06(self):
        actual_result = hw.man_3.walk()
        expected_result = 10
        self.assertEqual(actual_result, expected_result, msg=f"Actual result is: {actual_result} instead of Expected result: {expected_result}")
        
    





if __name__ == "__main__":
    unittest.main(verbosity=2)