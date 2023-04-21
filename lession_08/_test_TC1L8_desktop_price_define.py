import unittest
from functions_to_test import desktop_price_define


class HomeworksTesting1(unittest.TestCase):

    def test01(self):  # Equivalence partitioning.
        """
        Positive:
        Test correct values: count_month > 0, month_payment > 0
        """
        actual_result = desktop_price_define(count_month=12, month_payment=1000)
        expected_result = 12000
        self.assertEqual(actual_result, expected_result)

    def test02(self):  # Equivalence partitioning, Boundary analysis.
        """
        Positive:
        Test correct values: count_month 1, month_payment > 0
        """
        actual_result = desktop_price_define(count_month=1, month_payment=1000)
        expected_result = 1000
        self.assertEqual(actual_result, expected_result)

    def test03(self):  # Equivalence partitioning, Boundary analysis.
        """
        Positive:
        Test correct values: count_month > 0, month_payment > 1
        """
        actual_result = desktop_price_define(count_month=1000, month_payment=1)
        expected_result = 1000
        self.assertEqual(actual_result, expected_result)

    def test04(self):  # Equivalence partitioning
        """
        Negative:
        Test incorrect values: count_month > 1, month_payment < 0
        """
        actual_result = desktop_price_define(count_month=0, month_payment=0)
        self.assertIsNone(actual_result)

    def test05(self):  # Equivalence partitioning
        """
        Negative:
        Test incorrect values: count_month > 1, month_payment < 0
        """
        actual_result = desktop_price_define(count_month=-36, month_payment=-500)
        self.assertIsNone(actual_result)

    def test06(self):  # Equivalence partitioning, Boundary analysis.
        """
        Negative:
        Test incorrect values: count_month = 0, month_payment > 1
        """
        actual_result = desktop_price_define(count_month=0, month_payment=1000)
        self.assertIsNone(actual_result)

    def test07(self):  # Equivalence partitioning, Boundary analysis.
        """
        Negative:
        Test incorrect values: count_month > 1, month_payment = 1
        """
        actual_result = desktop_price_define(count_month=12, month_payment=0)
        self.assertIsNone(actual_result)

    def test08(self):  # Equivalence partitioning, Boundary analysis.
        """
        Negative:
        Test incorrect values: count_month < 0, month_payment > 1
        """
        actual_result = desktop_price_define(count_month=-1, month_payment=1000)
        self.assertIsNone(actual_result)

    def test09(self):  # Equivalence partitioning  Boundary analysis.
        """
        Negative:
        Test incorrect values: count_month > 1, month_payment < 0
        """
        actual_result = desktop_price_define(count_month=1, month_payment=-1000)
        self.assertIsNone(actual_result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
