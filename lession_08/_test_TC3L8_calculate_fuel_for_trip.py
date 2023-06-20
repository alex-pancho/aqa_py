import unittest
from functions_to_test import calculate_fuel_for_trip


class HomeworksTesting3(unittest.TestCase):

    def test01(self):  # Equivalence partitioning.
        """
        Positive:
        Case: Calculate result send distance
        """
        actual_result = calculate_fuel_for_trip(distance=1600)
        expected_result = [144.0, 3]
        self.assertEqual(actual_result, expected_result)

    def test02(self):  # Equivalence partitioning.
        """
        Positive:
        Case: Calculate result send changed distance
        """
        actual_result = calculate_fuel_for_trip(distance=3200)
        expected_result = [288.0, 6]
        self.assertEqual(actual_result, expected_result)

    def test03(self):  # Equivalence partitioning.
        """
        Positive:
        Case: Calculate result send changed tank volume
        """
        actual_result = calculate_fuel_for_trip(distance=1600, tank_volume=96)
        expected_result = [144.0, 1]
        self.assertEqual(actual_result, expected_result)

    def test04(self):  # Equivalence partitioning.
        """
        Positive:
        Case: Calculate result send changed fuel efforts
        """
        actual_result = calculate_fuel_for_trip(distance=1600, efforts=18)
        expected_result = [288.0, 6]
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
