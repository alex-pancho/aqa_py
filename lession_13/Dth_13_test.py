import unittest
import sys
import Dth_13 as homework


class MyTestCase (unittest.TestCase):
    def test_task_1(self):
        actual_result=homework.oleg_person.name
        expected_result="Oleg"
        self.assertEqual (actual_result, expected_result, msg=f"Test failed: correct result is: {expected_result}")

    def test_task_2(self):
        actual_result=homework.ihor_person.date_of_birth
        expected_result="11.03.1985"
        self.assertEqual (actual_result, expected_result, msg=f"Test failed: correct result is: {expected_result}")

    def test_task_3(self):
        actual_result=homework.ihor_person.work ()
        expected_result=15
        self.assertEqual (actual_result, expected_result, msg=f"Test failed: correct result is: {expected_result}")

    def test_task_4(self):
        actual_result=homework.dinis_person.eat ()
        expected_result=75
        self.assertEqual (actual_result, expected_result, msg=f"Test failed: correct result is: {expected_result}")

    def test_task_5(self):
        actual_result=homework.ihor_person.do_hm ()
        expected_result=0
        self.assertEqual (actual_result, expected_result, msg=f"Test failed: correct result is: {expected_result}")

    def test_task_6(self):
        actual_result=homework.marina_person.chill ()
        expected_result=95
        self.assertEqual (actual_result, expected_result, msg=f"Test failed: correct result is: {expected_result}")

    def test_task_7(self):
        actual_result=homework.olha_person.eat ()
        expected_result=25
        self.assertEqual (actual_result, expected_result, msg=f"Test failed: correct result is: {expected_result}")

    def test_task_8(self):
        actual_result=homework.marina_person.sleep ()
        expected_result=100
        self.assertEqual (actual_result, expected_result, msg=f"Test failed: correct result is: {expected_result}")

    def test_task_9(self):
        actual_result=homework.olha_person.work ()
        expected_result=0
        self.assertEqual (actual_result, expected_result, msg=f"Test failed: correct result is: {expected_result}")

    def test_task_10(self):
        actual_result=homework.oleg_person.eat ()
        expected_result=60
        self.assertEqual (actual_result, expected_result, msg=f"Test failed: correct result is: {expected_result}")

    if __name__ == "__main__":
        unittest.main (verbosity=2)
