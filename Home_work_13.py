class Human:
    """
    Class representing a human.

    Attributes:
    -----------
    name : str
        The first name of the human.
    surname : str
        The last name of the human.
    date_of_birth : str
        The date of birth of the human in the format 'YYYY-MM-DD'.
    gender : str
        The gender of the human, either 'Male' or 'Female'.
    energy : int
        The energy level of the human. It is initially set to 100.

    Methods:
    --------
    eat()
        Increases the energy level of the human by 5.
    sleep()
        Increases the energy level of the human by 10.
    talk()
        Decreases the energy level of the human by 5.
    walk()
        Decreases the energy level of the human by 10.
    do_homework()
        Decreases the energy level of the human by 90.
    """

    def __init__(self, name, surname, date_of_birth, gender):
        """
        Initialize a new Human object.

        Parameters:
        -----------
        name : str
            The first name of the human.
        surname : str
            The last name of the human.
        date_of_birth : str
            The date of birth of the human in the format 'YYYY-MM-DD'.
        gender : str
            The gender of the human, either 'Male' or 'Female'.
        """
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.energy = 100

    def eat(self):
        """Increases the energy level of the human by 5."""
        self.energy += 5

    def sleep(self):
        """Increases the energy level of the human by 10."""
        self.energy += 10

    def talk(self):
        """Decreases the energy level of the human by 5."""
        self.energy -= 5

    def walk(self):
        """Decreases the energy level of the human by 10."""
        self.energy -= 10

    def do_homework(self):
        """Decreases the energy level of the human by 90."""
        self.energy -= 90


if __name__ == "__main__":
    # Create 3 males and 2 females and perform some actions on them
    human1 = Human('John', 'Doe', '1990-01-01', 'Male')
    human2 = Human('Mark', 'Smith', '1985-06-03', 'Male')
    human3 = Human('Jack', 'Williams', '1995-12-12', 'Male')
    human4 = Human('Mary', 'Johnson', '1988-03-08', 'Female')
    human5 = Human('Lucy', 'Lee', '1992-09-20', 'Female')

    human1.eat()
    human2.talk()
    human3.walk()
    human4.do_homework()
    human5.sleep()
    human1.walk()

    humans = [human1, human2, human3, human4, human5]
    # Find the human with the most energy remaining
    most_energy = max(humans, key=lambda x: x.energy)
    print(f'{most_energy.name} {most_energy.surname} has the most energy remaining: {most_energy.energy}')


def test_human():
    """Test the Human class and its attributes and methods."""
    human = Human('John', 'Doe', '1990-01-01', 'Male')
    assert human.name == 'John'
    assert human.surname == 'Doe'
    assert human.date_of_birth == '1990-01-01'
    assert human.gender == 'Male'
    assert human.energy == 100

    human.eat()
    assert human.energy == 105

    human.sleep()
    assert human.energy == 115

    human.talk()
    assert human.energy == 110

    human.walk()
    assert human.energy == 100

    human.do_homework()
    assert human.energy == 10


print('All tests pass')

test_human()
