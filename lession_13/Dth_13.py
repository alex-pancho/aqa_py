class Human:
    def __init__(self, name: str, second_name: str, date_of_birth: str, energy: int):
        self.name=name
        self.second_name=second_name
        self.date_of_birth=date_of_birth
        self.energy=energy

    def __repr__(self) -> str:
        return f"Name:{self.name}, Second name:{self.second_name}, Date of birth:{self.date_of_birth}, Energy:{self.energy}"

    def eat(self):
        if self.energy + 5 <= 100:
            self.energy+=5
        else:
            self.energy=100
        return self.energy

    def sleep(self):
        if self.energy + 15 <= 100:
            self.energy+=15
        else:
            self.energy=100
        return self.energy

    def chill(self):
        if self.energy + 15 <= 100:
            self.energy+=15
        else:
            self.energy=100
        return self.energy

    def work(self):
        if self.energy >= 50:
            self.energy-=50
        else:
            self.energy=0
        return self.energy

    def do_hm(self):
        if self.energy >= 50:
            self.energy-=50
        else:
            self.energy=0
        return self.energy


oleg_person=Human ("Oleg", "Karpatov", "05.12.1994", 100)
ihor_person=Human ("Ihor", "Mathurets", "11.03.1985", 100)
dinis_person=Human ("Dinis", "Karpenko", "22.01.1974", 100)
olha_person=Human ("Olha", "Thinchenko", "18.09.1997", 100)
marina_person=Human ("Margarita", "Voytenko", "29.05.1988", 100)

oleg_person.do_hm ()
oleg_person.eat ()

ihor_person.work ()
ihor_person.sleep ()

dinis_person.do_hm ()
dinis_person.chill ()
dinis_person.eat ()

olha_person.do_hm ()
olha_person.chill ()
olha_person.eat ()
olha_person.work ()

marina_person.work ()
marina_person.sleep ()
marina_person.chill ()

person_energy_list=[oleg_person, ihor_person, dinis_person, olha_person, marina_person]


def energy_count():
    max_energy_person=max (person_energy_list, key=lambda i: i.energy)
    print (f"{max_energy_person.name} {max_energy_person.second_name} ramaining {max_energy_person.energy} energy")


energy_count ()
