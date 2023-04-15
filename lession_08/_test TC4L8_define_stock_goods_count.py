import unittest
from functions_to_test import define_stock_goods_count


class HomeworksTesting4(unittest.TestCase):

    def test01(self):  # Equivalence partitioning.
        """
        Positive:
        Case: Calculate result send default values
        """
        actual_result = define_stock_goods_count(goods_all=375291, first_and_second=250449, second_and_third=222950)
        expected_result = {'first_stock': 152341, 'second_stock': 98108, 'third_stock': 124842}
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
