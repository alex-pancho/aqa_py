

class Person:
    population = 0
    def __init__(self, name):
        self.name = name.title()
        self.add_population()

    @classmethod
    def add_population(cls):
        cls.population += 1

    @staticmethod
    def sum(a, b):
        return a + b

    def __str__(self) -> str:
        return f"Its {self.name}"

    def __int__(self) -> int:
        return self.population

class Horse:
    def run(self):
        return ("Я біжу")

    def say(self):
        return ("I'm Horse")

class Eagle:
    def fly(self):
        return ("Я лечу")

    def say(self):
        return ("I'm Eagle")

class Peasus(Eagle, Horse):

    def say(self):
        a = Eagle.say(self)
        b = Horse.say(self)
        return f"{a} та {b}"

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def __str__(self) -> str:
        return f"{self.name} has salary: {self.salary}"


if __name__ == "__main__":
    first_man = Person("adam")
    # print(first_man.population)
    second_man = Person("eva")
    # print(second_man.population)
    # print(first_man.population)
    third_man = Person("kain")
    # print(first_man.population)

    # print(Person.sum(1, 1))
    # print(str(first_man), int(first_man))
    my_little_pegasus = Peasus()
    my_little_pegasus.fly()
    my_little_pegasus.run()
    # print(my_little_pegasus.say())
    four_man = Employee("avel", 23990)
    print(four_man)
    print()