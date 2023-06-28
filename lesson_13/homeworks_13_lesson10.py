"""Розробити клас Human.
Людина має:
    Ім'я
    Прізвище
    Дату народження
    Стать
    Енергію = 100
Люди можуть:
    Їсти (Енергія +5)
    Спати (Енергія +10)
    Говорити (Енергія -5)
    Ходити (Енергія -10)
    Робити домашку (Енергія -90)
if __name__ == "__main__":
    Створити 3 чоловіків та 2 жінок, Задати кожному з них виконання
    декількох дій, вивести в кого найбільше енергії лишилося.
Створити тести на клас та на атрибути класу.
"""


class Human:
    def __init__(self, name: str, surname: str, birthdate: float, gender: str):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.energy = 100

    def eat(self):
        self.energy += 5

    def sleep(self):
        self.energy += 10

    def talk(self):
        self.energy -= 5

    def walk(self):
        self.energy -= 10

    def do_homework(self):
        self.energy -= 90




if __name__ == "__main__":
    # Створення 3 чоловіків та 2 жінок
    human1 = Human("Stan", "Smith", "1980/04/13", "male")
    human2 = Human("Francine", "Smith", "1984/11/23", "female")
    human3 = Human("Hayley", "Smith", "2004/07/05", "female")
    human4 = Human("Steve", "Smith", "2008/02/12", "male")
    human5 = Human("Roger", "Smith", "1920/12/31", "male")

    # Виконання дій для кожної людини
    human1.eat()
    human1.do_homework()
    human2.talk()
    human2.walk()
    human3.sleep()
    human3.eat()
    human4.do_homework()
    human5.eat()
    human5.talk()
    human5.talk()

    # Пошук людини з найбільшою залишковою енергією
    humans = [human1, human2, human3, human4, human5]
    max_energy = -1
    max_energy_human = None
    for human in humans:
        if human.energy > max_energy:
            max_energy = human.energy
            max_energy_human = human

    # Виведення результату
    print("The person with the most residual energy:")
    print(f"{max_energy_human.name} {max_energy_human.surname}, energy: {max_energy_human.energy}")


#Tests:
# import unittest
#
# class TestHuman(unittest.TestCase):
#     def test_create_human(self):
#         human = Human("Stan", "Smith", 1980/04/13, "male")
#         self.assertEqual(human.name, "Stan")
#         self.assertEqual(human.surname, "Smith")
#         self.assertEqual(human.birthdate, 1980/04/13)
#         self.assertEqual(human.gender, "male")
#         self.assertEqual(human.energy, 100)
#
#     def test_eat(self):
#         human = Human("John", "Doe", 1990/1/1, "male")
#         human.eat()
#         self.assertEqual(human.energy, 105)
#
#     def test_sleep(self):
#         human = Human("John", "Doe", 1990/1/1, "male")
#         human.sleep()
#         self.assertEqual(human.energy, 110)
#
#     def test_talk(self):
#         human = Human("John", "Doe", 1990/1/1, "male")
#         human.talk()
#         self.assertEqual(human.energy, 95)
#
#     def test_walk(self):
#         human = Human("John", "Doe", 1990/1/1, "male")
#         human.walk()
#         self.assertEqual(human.energy, 90)
#
#     def test_do_homework(self):
#         human = Human("John", "Doe", 1990/1/1, "male")
#         human.do_homework()
#         self.assertEqual(human.energy, 10)
#
# if __name__ == '__main__':
#     unittest.main()


import unittest

class TestHuman(unittest.TestCase):
    def setUp(self):
        self.human1 = Human("Stan", "Smith", "1980/04/13", "male")
        self.human2 = Human("Francine", "Smith", "1984/11/23", "female")
        self.human3 = Human("Hayley", "Smith", "2004/07/05", "female")
        self.human4 = Human("Steve", "Smith", "2008/02/12", "male")
        self.human5 = Human("Roger", "Smith", "1920/12/31", "male")

    def test_create_human(self):
        self.assertEqual(self.human1.name, "Stan")
        self.assertEqual(self.human1.surname, "Smith")
        self.assertEqual(self.human1.birthdate, "1980/04/13")
        self.assertEqual(self.human1.gender, "male")
        self.assertEqual(self.human1.energy, 100)

    def test_eat(self):
        self.human1.eat()
        self.assertEqual(self.human1.energy, 105)

    def test_sleep(self):
        self.human2.sleep()
        self.assertEqual(self.human2.energy, 110)

    def test_talk(self):
        self.human3.talk()
        self.assertEqual(self.human3.energy, 95)

    def test_walk(self):
        self.human4.walk()
        self.assertEqual(self.human4.energy, 90)

    def test_do_homework(self):
        self.human5.do_homework()
        self.assertEqual(self.human5.energy, 10)

if __name__ == '__main__':
    unittest.main()




