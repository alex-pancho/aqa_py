import unittest
import homeworks_13 as h
from homeworks_13 import man_1   # for pretty typing


class HomeWork13Tests(unittest.TestCase):

    def test0(self):
        """Create human test"""
        human = h.Human('name', 'second_name', ('2012', '12', '02'), 'woman')
        self.assertIsNotNone(human)

    """ Attributes Tests """

    def test01(self):
        """first_name test"""

        actual_result = man_1.first_name
        expected_result = 'Taras'

        self.assertEqual(actual_result, expected_result)

    def test02(self):
        """second_name test"""

        actual_result = man_1.second_name
        expected_result = 'Shevchenko'

        self.assertEqual(actual_result, expected_result)

    def test03(self):
        """birth_date test"""

        actual_result = format(man_1.birth_date)
        expected_result = '1992-4-21'

        self.assertEqual(actual_result, expected_result)

    def test04(self):
        """Sex test"""

        actual_result = man_1.sex
        expected_result = 'man'

        self.assertEqual(actual_result, expected_result)

    def test05(self):
        """Energy test"""

        actual_result = man_1.energy
        expected_result = 100

        self.assertEqual(actual_result, expected_result)

        """  Methods test  """

    def test06(self):
        """eat method test"""

        actual_result = man_1.eat()
        expected_result = 105

        self.assertEqual(actual_result, expected_result)

    def test07(self):
        """sleep method test"""

        actual_result = man_1.sleep()
        expected_result = 110

        self.assertEqual(actual_result, expected_result)

    def test08(self):
        """talk method test"""

        actual_result = man_1.talk()
        expected_result = 95

        self.assertEqual(actual_result, expected_result)

    def test09(self):
        """walk method test"""

        actual_result = man_1.walk()
        expected_result = 90

        self.assertEqual(actual_result, expected_result)

    def test10(self):
        """make_hw method test"""

        actual_result = man_1.make_hw()
        expected_result = 10

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)