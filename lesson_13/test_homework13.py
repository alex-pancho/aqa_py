import unittest
import homeworks_13
from homeworks_13 import Human
from homeworks_13 import first_girl

class HomeworkTest(unittest.TestCase):

    def test_first_boy(self):
        boy = Human('Eugene', 'Poronko', '1993', 'boy')
        self.assertEqual(boy.name, 'Eugene')
        self.assertEqual(boy.surname, 'Poronko')
        self.assertEqual(boy.birthday, '1993')
        self.assertEqual(boy.gender, 'boy')

    def test_second_boy(self):
        boy = Human('Edic', 'Koba', '1993', 'boy')
        self.assertEqual(boy.name, 'Edic')
        self.assertEqual(boy.surname, 'Koba')
        self.assertEqual(boy.birthday, '1993')
        self.assertEqual(boy.gender, 'boy')

    def test_third_boy(self):
        boy = Human('Vladislav', 'Sidora','1994', 'boy')
        self.assertEqual(boy.name, 'Vladislav')
        self.assertEqual(boy.surname, 'Sidora')
        self.assertEqual(boy.birthday, '1994')
        self.assertEqual(boy.gender, 'boy')

    def test_first_girl(self):
        girl = Human('Evgeniya', 'Kupenko', '1998', 'girl')
        self.assertEqual(girl.name, 'Evgeniya')
        self.assertEqual(girl.surname, 'Kupenko')
        self.assertEqual(girl.birthday, '1998')
        self.assertEqual(girl.gender, 'girl')

    def test_second_girl(self):
        girl = Human('Vitalina', 'Petrova', '1997', 'girl')
        self.assertEqual(girl.name, 'Vitalina')
        self.assertEqual(girl.surname, 'Petrova')
        self.assertEqual(girl.birthday, '1997')
        self.assertEqual(girl.gender, 'girl')

    def test_action_eat(self):
        """this is a test for eating"""
        actual_result = first_girl.eat()
        expected_result = 105
        self.assertEqual(actual_result, expected_result)

    def test_action_sleep(self):
        """this is a test for sleeping"""
        actual_result = first_girl.sleep()
        expected_result = 110
        self.assertEqual(actual_result, expected_result)

    def test_action_speak(self):
        """this is a test for speaking"""
        actual_result = first_girl.speak()
        expected_result = 95
        self.assertEqual(actual_result, expected_result)

    def test_action_walk(self):
        """this is a test for walking"""
        actual_result = first_girl.walk()
        expected_result = 90
        self.assertEqual(actual_result, expected_result)

    def test_action_homework(self):
        """this is a test for doing homework"""
        actual_result = first_girl.homework()
        expected_result = 10
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
