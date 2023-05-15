class LifeActions:

    energy = 100

    def eat(self):
        self.energy += 5
        return self.energy

    def sleep(self):
        self.energy += 10
        return self.energy

    def speak(self):
        self.energy -= 5 
        return self.energy

    def walk(self):
        self.energy -= 10
        return self.energy     

    def homework(self):
        self.energy -= 90
        return self.energy


class Human(LifeActions):

    def __init__(self, name:str, lastName:str, birthDate, sex:str, energy=LifeActions.energy)  -> None:
        self.name = name
        self.lastName = lastName
        self.sex = sex
        self.birthDate = birthDate
        self.energy = energy

    def __repr__(self) -> str:
        return f"Name: {self.name}, \nLast Name: {self.lastName}, \nBirth date: {self.birthDate}, \nSex: {self.sex}, \nENERGY: {self.energy}"
    

all_energies = {}

AnnJones = Human("Ann","Jones", "01/01/2000", "female")
AnnJones.eat()
AnnJones.sleep()
AnnJones.homework()
all_energies["AnnJones"] = AnnJones.energy

TaylorSwift = Human("Taylor","Swift", "01/01/1990", "female")
TaylorSwift.eat()
TaylorSwift.speak()
TaylorSwift.walk()
all_energies["TaylorSwift"] = TaylorSwift.energy

DavidWilliams = Human("David","Williams", "01/01/1991", "male")
DavidWilliams.sleep()
DavidWilliams.speak()
DavidWilliams.homework()
all_energies["DavidWilliams"] = DavidWilliams.energy

MichaelEvans = Human("Michael","Evans", "01/01/1997", "male")
MichaelEvans.walk()
MichaelEvans.sleep()
MichaelEvans.homework()
all_energies["MichaelEvans"] = MichaelEvans.energy

TomThomas = Human("Tom","Thomas", "01/01/1985", "male")
TomThomas.homework()
TomThomas.eat()
TomThomas.walk()
all_energies["TomThomas"] = TomThomas.energy

print(all_energies)
print(f"{max(all_energies)} has the most of energy left")