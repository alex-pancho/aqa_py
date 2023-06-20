import unittest
from functions_to_test import solve_igors_math_troubles


class HomeworksTesting2(unittest.TestCase):

    def test01(self):  # Equivalence partitioning.
        """
        Positive:
        Case: Calculate correct values
        """
        actual_result = solve_igors_math_troubles(photos_all=232, max_photos_on_page=8)
        expected_result = 29
        self.assertEqual(actual_result, expected_result)

    def test02(self):  # Equivalence partitioning.
        """
        Positive:
        Case: Photos don't fit fully in pages.
        Count of pages increases + 1
        """
        actual_result = solve_igors_math_troubles(photos_all=233, max_photos_on_page=8)
        expected_result = 30
        self.assertEqual(actual_result, expected_result)

    def test03(self):  # Equivalence partitioning.
        """
        Positive:
        Case: Count max fill photos on one pege reduced
        Count of pages increases
        """
        actual_result = solve_igors_math_troubles(photos_all=233, max_photos_on_page=7)
        expected_result = 34
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
