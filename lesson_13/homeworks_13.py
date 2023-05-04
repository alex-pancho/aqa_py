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

class Date:
    formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = self.formats[code]
        return fmt.format(d=self)


class Human:

    """Human's parameters"""

    def __init__(self, first_name: str, second_name: str, birth_date: tuple, sex: str, energy: int = 100):
        """Receives args human parameters with default energy value 100  and birth data tuple with
         three str number values then formats to correct view.
        """
        self.first_name = first_name
        self.second_name = second_name
        self.birth_date = Date(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))
        self.sex = sex
        self.energy = energy


    def eat(self) -> int:
        """add +5 to energy"""
        self.energy += 5
        return self.energy

    def sleep(self) -> int:
        """adds +10 to energy"""
        self.energy += 10
        return self.energy

    def talk(self) -> int:
        """reduces -5 energy"""
        self.energy -= 5
        return self.energy

    def walk(self) -> int:
        """Reduces -10 energy """
        self.energy -= 10
        return self.energy

    def make_hw(self) -> int:
        """Reduces -90 energy"""
        self.energy -= 90
        return self.energy


man_1 = Human('Taras', 'Shevchenko', ('1992', '04', '21'), 'man')
man_2 = Human('Petro', 'Petrenko', ('1991', '03', '02'), 'man')
man_3 = Human('Mykola', 'Lahernyi', ('1990', '04', '18'), 'man')
woman_1 = Human('Nataly', 'Zayceva', ('1994', '02', '04'), 'woman')
woman_2 = Human('Tamara', 'Ivanova', ('1993', '01', '04'), 'woman')


man_1.make_hw()
man_1.eat()

man_2.talk()
man_2.sleep()

man_3.walk()
man_3.make_hw()

woman_1.talk()
woman_1.walk()

woman_2.sleep()
woman_2.eat()

humans = [man_1, man_2, man_3, woman_1, woman_2]
max_human = max(humans, key=lambda human: human.energy)
print(f"The human with the maximum energy is {max_human.first_name} has {max_human.energy} energy points.")
