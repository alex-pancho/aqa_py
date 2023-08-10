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
    '''Main class human'''
    def __init__(self, name:str, last_name:str, burthday_date:str, gender:str):
        self.name = name
        self.last_name = last_name
        self.burthday_date = burthday_date
        self.gender = gender
        self.energy = 100

# class Actions(Human):
#     # energy_level = 0

    def eat(self):
        self.energy += 5

    def talk(self):
        self.energy -=20

    def sleep(self):
        self.energy += 10

    def speak(self):
        self.energy -= 5

    def move(self):
        self.energy -= 10

    def make_homework(self):
        self.energy -= 90


if __name__ == "__main__":
    male_1 = Human("Alex", "Goole", "10-05-1980", "Male")
    male_2 = Human("Rex", "Tpogn", "10-05-1950", "Male")
    male_3 = Human("Oppo", "Bollshit", "10-05-1900", "Male")
    female_1 = Human("Sandra", "Grace", "10-05-1980", "Female")
    female_2 = Human("Alisa", "Lolla", "10-05-1970", "Male")

    male_1.sleep()
    male_1.eat()
    male_1.make_homework()
    male_2.sleep()
    male_2.move()
    male_3.eat()
    female_1.make_homework()
    female_2.speak()

    all_humans = [male_1, male_2, male_3, female_1, female_2]


    def get_energy(human):
        return human.energy
    max_energy = max(all_humans, key=get_energy)

    print(f"{max_energy.name} {max_energy.last_name} has the most energy left ({max_energy.energy})")
