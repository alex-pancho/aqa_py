class Date:
    """Class for birthdays"""

    formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
    }

    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'dmy'
        fmt = self.formats[code]
        return fmt.format(d=self)


class Human:
    """Just human"""

    def __init__(self, name: str, surname: str, birthday: tuple, sex: str, energy: int = 100):
        self.name = name
        self.surname = surname
        self.birthday = Date(int(birthday[0]), int(birthday[1]), int(birthday[2]))
        self.sex = sex
        self.energy = energy

    def eat(self) -> int:
        """Human can eat and restore energy if energy less than 100"""
        if self.energy <= 95:
            self.energy += 5
        elif 100 >= self.energy > 95:
            self.energy = 100
        return self.energy

    def sleep(self) -> int:
        """Human can sleep and restore energy if energy less than 100"""
        if self.energy <= 90:
            self.energy += 10
        elif 100 >= self.energy > 90:
            self.energy = 100
        return self.energy

    def speak(self) -> int | str:
        """Human can speak if he/she have minimum 5 energy"""
        if self.energy >= 5:
            self.energy -= 5
            return self.energy
        elif 0 <= self.energy < 5:
            return f"{self.name} you don't have enough energy to perform this action"

    def walk(self) -> int | str:
        """Human can speak if he/she have minimum 10 energy"""
        if self.energy >= 10:
            self.energy -= 10
            return self.energy
        elif 0 <= self.energy < 10:
            return f"{self.name} you don't have enough energy to perform this action"

    def make_home_work(self) -> int | str:
        if self.energy >= 90:
            self.energy -= 90
            return self.energy
        elif 0 <= self.energy < 90:
            return f"{self.name} you don't have enough energy to perform this action"


frodo = Human("Frodo", "Baggins", ("22", "09", "2968"), "male", 100)
sam = Human("Sam", "Gamgee", ("06", "04", "2980"), "male", 100)
aragorn = Human("Aragorn", "Son of Arathorn", ("01", "03", "2931"), "male", 100)
arya = Human("Arya", "Stark", ("16", "03", "287"), "female", 100)
sansa = Human("Sansa", "Stark", ("12", "02", "289"), "female", 100)


def humans_actions():

    frodo.make_home_work()
    frodo.eat()
    frodo.sleep()

    sam.speak()
    sam.sleep()

    aragorn.make_home_work()
    aragorn.sleep()

    arya.make_home_work()
    arya.sleep()
    arya.sleep()

    sansa.speak()
    sansa.speak()
    sansa.speak()

    humans = {frodo.name: frodo.energy,
              sam.name: sam.energy,
              aragorn.name: aragorn.energy,
              arya.name: arya.energy,
              sansa.name: sansa.energy}


    max_human_energy = sorted(humans.items(), key=lambda param: (param[1], param[0]), reverse=True)
    print(f"{max_human_energy[0][0]} have {max_human_energy[0][1]} energy")


if __name__ == '__main__':
    humans_actions()
