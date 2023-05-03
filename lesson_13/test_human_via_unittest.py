import unittest
from lesson_13 import *
from lesson_13.homeworks_13 import Human

class TestHuman(unittest.TestCase):
    def test_attributes(self):
        from lesson_13.homeworks_13 import Human
        john = Human("John", "Doe", "2000-01-01", "male")
        self.assertEqual(john.name, "John")
        self.assertEqual(john.last_name, "Doe")
        self.assertEqual(john.burthday_date, "2000-01-01")
        self.assertEqual(john.gender, "male")
        self.assertEqual(john.energy, 100)

    def test_eat(self):
        john = Human("John", "Doe", "2000-01-01", "male")
        john.eat()
        self.assertEqual(john.energy, 105)

    def test_sleep(self):
        john = Human("John", "Doe", "2000-01-01", "male")
        john.sleep()
        self.assertEqual(john.energy, 110)

    def test_speak(self):
        john = Human("John", "Doe", "2000-01-01", "male")
        john.talk()
        self.assertEqual(john.energy, 95)

    def test_walk(self):
        john = Human("John", "Doe", "2000-01-01", "male")
        john.move()
        self.assertEqual(john.energy, 90)

    def test_do_homework(self):
        john = Human("John", "Doe", "2000-01-01", "male")
        john.make_homework()
        self.assertEqual(john.energy, 10)


if __name__ == "__main__":
    unittest.main()
