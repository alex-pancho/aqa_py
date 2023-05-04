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
    """This is Human class"""
    def __init__(self, name:str, surname:str, birthday:str, gender:str, energy: int = 100):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.gender = gender
        self.energy = energy

    def eat(self) -> int:
        """Plus energy after eating"""
        self.energy += 5
        return self.energy

    def sleep(self) -> int:
        """Plus energy after sleep"""
        self.energy += 10
        return self.energy

    def speak(self) -> int:
        """Minus energy after comunication"""
        self.energy -= 5
        return self.energy

    def walk(self) -> int:
        """Minus energy after walking"""
        self.energy -= 10
        return self.energy

    def homework(self) -> int:
        """Minus energy after doing homework"""
        self.energy -= 90
        return self.energy

first_boy = Human('Eugene', 'Poronko', '1993', 'boy')
second_boy = Human('Edic', 'Koba', '1993', 'boy')
third_boy = Human('Vladislav', 'Sidora','1994', 'boy')
first_girl = Human('Evgeniya', 'Kupenko', '1998', 'girl')
second_girl = Human('Vitalina', 'Petrova', '1997', 'girl')

first_boy.eat()
first_boy.sleep()

second_boy.sleep()
second_boy.walk()

third_boy.eat()
third_boy.homework()

first_girl.eat()
first_girl.walk()

second_girl.speak()
second_girl.eat()

persons = [first_boy, second_boy, third_boy, first_girl, second_girl]
max_energy = max(persons, key=lambda human: human.energy)
print('This person has more energy than others:', max_energy.name)
