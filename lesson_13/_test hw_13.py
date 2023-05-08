import unittest
import hw_13 as h


class HomeWork13Tests(unittest.TestCase):

    # Create test Human

    def test01(self):
        """Create human test"""
        human = h.Human('name', 'last_name', ('2012', '12', '02'), 'w')
        self.assertIsInstance(human, h.Human)

    # Attributes Tests

    def test02(self):
        """first_name test"""

        test_human1 = h.Human('test_name', 'last_name', ('2012', '12', '02'), 'w')
        actual_result = test_human1.first_name
        expected_result = 'test_name'
        self.assertEqual(actual_result, expected_result)

    def test03(self):
        """second_name test"""

        test_human2 = h.Human('name', 'test_second_name', ('2012', '12', '02'), 'w')
        actual_result = test_human2.second_name
        expected_result = 'test_second_name'
        self.assertEqual(actual_result, expected_result)

    def test04(self):
        """birth_date test"""

        test_human3 = h.Human('name', 'second_name', ('2000', '12', '01'), 'w')
        actual_result = format(test_human3.birth_date)
        expected_result = '2000-12-1'
        self.assertEqual(actual_result, expected_result)

    def test05(self):
        """Sex test"""

        test_human4 = h.Human('name', 'second_name', ('2000', '12', '01'), 'm')
        actual_result = test_human4.sex
        expected_result = 'm'
        self.assertEqual(actual_result, expected_result)

    def test06(self):
        """Energy test"""

        test_human5 = h.Human('name', 'second_name', ('2000', '12', '01'), 'm')
        actual_result = test_human5.energy
        expected_result = 100
        self.assertEqual(actual_result, expected_result)

    #  Methods test

    def test07(self):
        """eat method test"""

        test_human6 = h.Human('name', 'second_name', ('2000', '12', '01'), 'm')
        actual_result = test_human6.eat()
        expected_result = 105
        self.assertEqual(actual_result, expected_result)

    def test08(self):
        """sleep method test"""

        test_human7 = h.Human('name', 'second_name', ('2000', '12', '01'), 'm')
        actual_result = test_human7.sleep()
        expected_result = 110
        self.assertEqual(actual_result, expected_result)

    def test09(self):
        """talk method test"""

        test_human8 = h.Human('name', 'second_name', ('2000', '12', '01'), 'm')
        actual_result = test_human8.talk()
        expected_result = 95
        self.assertEqual(actual_result, expected_result)

    def test10(self):
        """walk method test"""

        test_human8 = h.Human('name', 'second_name', ('2000', '12', '01'), 'm')
        actual_result = test_human8.walk()
        expected_result = 90
        self.assertEqual(actual_result, expected_result)

    def test11(self):
        """make_hw method test"""

        test_human9 = h.Human('name', 'second_name', ('2000', '12', '01'), 'm')
        actual_result = test_human9.make_hw()
        expected_result = 10
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
