# Date formatter

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


# Main human class


class Human:

    """Human params"""

    def __init__(self, first_name: str, second_name: str, birth_date: tuple, sex: str, energy: int = 100):
        """Receives args human params with default energy value 100  and birth data tuple with
         three str number values then formats to pretty view.
        """
        self.first_name = first_name
        self.second_name = second_name
        self.birth_date = Date(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))
        self.sex = sex
        self.energy = energy

    # Human actions

    def eat(self) -> int:
        """adds +5 energy to energy value"""
        self.energy += 5
        return self.energy

    def sleep(self) -> int:
        """adds +10 energy to energy value"""
        self.energy += 10
        return self.energy

    def talk(self) -> int:
        """Reduces -5 energy to energy value"""
        self.energy -= 5
        return self.energy

    def walk(self) -> int:
        """Reduces -10 energy to energy value"""
        self.energy -= 10
        return self.energy

    def make_hw(self) -> int:
        """Reduces -90 energy to energy value"""
        self.energy -= 90
        return self.energy


# Humans create


man1 = Human('man1', '1man', ('2002', '11', '01'), 'm')
man2 = Human('man2', '2man', ('2003', '12', '02'), 'm')
man3 = Human('man3', '3man', ('2004', '01', '03'), 'm')
woman1 = Human('woman1', '1woman', ('2005', '02', '04'), 'w')
woman2 = Human('woman2', '2woman', ('2006', '03', '05'), 'w')
test = Human('man1', '1man', ('2002', '11', '01'), 'm')  # data for unittests

# Human actions


man1.make_hw()
man1.eat()

man2.talk()
man2.sleep()

man3.walk()
man3.make_hw()

woman1.talk()
woman1.talk()
woman1.walk()

woman2.sleep()
woman2.eat()


# Energizer define


humans = [man1, man2, man3, woman1, woman2]
max_human = max(humans, key=lambda human: human.energy)
print(f"The human with the maximum energy is {max_human.first_name} has {max_human.energy} energy points.")
