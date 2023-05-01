import unittest
import hw_13 as h
from hw_13 import test as test_human  # for pretty typing


class HomeWork13Tests(unittest.TestCase):

    # Create test Human

    def test0(self):
        """Create human test"""
        human = h.Human('man5', '5man', ('2012', '12', '02'), 'w')
        self.assertIsNotNone(human)

    # Attributes Tests

    def test01(self):
        """first_name test"""

        actual_result = test_human.first_name
        expected_result = 'man1'

        self.assertEqual(actual_result, expected_result)

    def test02(self):
        """second_name test"""

        actual_result = test_human.second_name
        expected_result = '1man'

        self.assertEqual(actual_result, expected_result)

    def test03(self):
        """birth_date test"""

        actual_result = format(test_human.birth_date)
        expected_result = '2002-11-1'

        self.assertEqual(actual_result, expected_result)

    def test04(self):
        """Sex test"""

        actual_result = test_human.sex
        expected_result = 'm'

        self.assertEqual(actual_result, expected_result)

    def test05(self):
        """Energy test"""

        actual_result = test_human.energy
        expected_result = 100

        self.assertEqual(actual_result, expected_result)

        #  Methods test

    def test06(self):
        """eat method test"""

        actual_result = test_human.eat()
        expected_result = 105

        self.assertEqual(actual_result, expected_result)

    def test07(self):
        """sleep method test"""

        actual_result = test_human.sleep()
        expected_result = 115

        self.assertEqual(actual_result, expected_result)

    def test08(self):
        """talk method test"""

        actual_result = test_human.talk()
        expected_result = 110

        self.assertEqual(actual_result, expected_result)

    def test09(self):
        """walk method test"""

        actual_result = test_human.walk()
        expected_result = 100

        self.assertEqual(actual_result, expected_result)

    def test10(self):
        """make_hw method test"""

        actual_result = test_human.make_hw()
        expected_result = 10

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
