import unittest
import sys
import pathlib
import home_work_13_dudnik
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))


class TestHomeWork13(unittest.TestCase):

    def test_energy_never_less_0(self):
        """If humans makes actions which reduce energy, their energy can`t be less than 0"""
        precondition = home_work_13_dudnik.arya.make_home_work()
        actual_result = home_work_13_dudnik.arya.make_home_work()
        expected_result = "Arya you don't have enough energy to perform this action"
        self.assertEqual(actual_result, expected_result)

        precondition = home_work_13_dudnik.frodo.make_home_work(), home_work_13_dudnik.frodo.walk()
        actual_result = home_work_13_dudnik.frodo.walk()
        expected_result = "Frodo you don't have enough energy to perform this action"
        self.assertEqual(actual_result, expected_result)

    def test_energy_never_over_100(self):
        """If humans makes actions which increase energy, their energy can`t be more than 100"""
        actual_result = home_work_13_dudnik.sansa.sleep()
        expected_result = 100
        self.assertEqual(actual_result, expected_result)

        precondition = home_work_13_dudnik.sansa.sleep()
        actual_result = home_work_13_dudnik.sansa.sleep()
        expected_result = 100
        self.assertEqual(actual_result, expected_result)

        precondition = home_work_13_dudnik.sam.speak()
        actual_result = home_work_13_dudnik.sam.sleep()
        expected_result = 100
        self.assertEqual(actual_result, expected_result)
