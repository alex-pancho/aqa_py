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

    def __init__(self,name:str, last_name:str, birthday:str, gender:str, energy:int = 100 ) -> None:
        self.name = name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.energy = energy


    def eat(self):
        self.energy +=5
        return self.energy
    
    def sleep(self):
        self.energy +=10
        return self.energy

    def speak(self):
        self.energy -= 5
        return self.energy

    def walk(self):
        self.energy -= 10
        return self.energy

    def do_homework(self):
        self.energy -= 90
        return self.energy


woman_1 = Human("Kate", "Bush", "30-05-1959", "female")
woman_2 = Human("Lita", "Ford", "21-01-1956", "female")
woman_3 = Human("Jennifer", "Button", "13-07-1963", "female")
man_1 = Human("Alice", "Cooper", "04-02-1948", "male")
man_2 = Human("Joe", "Perry", "12-04-1953", "male" )
man_3 = Human("Joakim", "Broden", "05-10-1980", "male" )


woman_1.do_homework()
woman_1.eat()

woman_2.sleep()
woman_2.speak()

woman_3.do_homework()
woman_3.sleep()

man_1.walk()
man_1.sleep()

man_2.sleep()
man_2.eat()
 

human_list = [woman_1, woman_2, woman_3, man_1, man_2]

def get_energy(human):
    return human.energy
    
max_energy = max(human_list, key=get_energy)

print(f"{max_energy.name} {max_energy.last_name} has max level of energy: {max_energy.energy} ")






