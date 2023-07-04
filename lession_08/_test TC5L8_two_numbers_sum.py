import unittest
from functions_to_test import two_numbers_sum


class HomeworksTesting5(unittest.TestCase):

    def test01(self):  # Equivalence partitioning.
        """Positive:
        Case: send two positive operands"""
        actual_result = two_numbers_sum(operand_1=1, operand_2=2)
        expected_result = 3
        self.assertEqual(actual_result, expected_result)

    def test02(self):  # Equivalence partitioning.
        """Positive:
        Case: send  0 and positive operands"""
        actual_result = two_numbers_sum(operand_1=0, operand_2=2)
        expected_result = 2
        self.assertEqual(actual_result, expected_result)

    def test03(self):  # Equivalence partitioning.
        """Positive:
        Case: send 0 and positive operands"""
        actual_result = two_numbers_sum(operand_1=0, operand_2=2)
        expected_result = 2
        self.assertEqual(actual_result, expected_result)

    def test04(self):
        """Positive:
        Case: send operands equal 0"""
        actual_result = two_numbers_sum(operand_1=0, operand_2=0)
        expected_result = 0
        self.assertEqual(actual_result, expected_result)

    def test05(self):  # Equivalence partitioning.
        """Positive:
        Case: send positive and 0 operands"""
        actual_result = two_numbers_sum(operand_1=1, operand_2=0)
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    def test06(self):  # Equivalence partitioning.
        """Positive:
        Case: send negative and positive operands"""
        actual_result = two_numbers_sum(operand_1=-1, operand_2=2)
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    def test08(self):  # Equivalence partitioning.
        """Positive:
        Case: send positive and negative operands"""
        actual_result = two_numbers_sum(operand_1=1, operand_2=-2)
        expected_result = -1
        self.assertEqual(actual_result, expected_result)

    def test07(self):  # Equivalence partitioning.
        """Positive:
        Case: send two negative operands"""
        actual_result = two_numbers_sum(operand_1=-1, operand_2=-2)
        expected_result = -3
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
