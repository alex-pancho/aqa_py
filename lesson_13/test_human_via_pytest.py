import sys
from pathlib import Path
import pytest
from lesson_13 import *
from lesson_13.homeworks_13 import Human

# hmwrk = (Path.cwd() / 'homeworks_13.py')
# from hmwrk import Human

class TestHuman:
    def test_human_initialization(self):
        '''validate correct atribute initialization'''
        human = Human("Alex", "Goole", "10-05-1980", "Male")
        assert human.name == "Alex"
        assert human.last_name == "Goole"
        assert human.burthday_date == "10-05-1980"
        assert human.gender == "Male"
        assert human.energy == 100


    def test_eat(self):
        '''verifying human.eat function'''
        human = Human("Alex", "Goole", "10-05-1980", "Male")
        human.eat()
        assert human.energy == 105


    def test_sleep(self):
        '''verifying human.sleep function'''
        human = Human("Alex", "Goole", "10-05-1980", "Male")
        human.sleep()
        assert human.energy == 110


    def test_speak(self):
        '''verifying human.speak function'''
        human = Human("Alex", "Goole", "10-05-1980", "Male")
        human.speak()
        assert human.energy == 95


    def test_move(self):
        '''verifying human.move function'''
        human = Human("Alex", "Goole", "10-05-1980", "Male")
        human.move()
        assert human.energy == 90


    def test_make_homework(self):
        '''verifying human.homewoerk function'''
        human = Human("Alex", "Goole", "10-05-1980", "Male")
        human.make_homework()
        assert human.energy == 10


    def test_max_energy(self):
        '''verifying human.max energy function'''
        male_1 = Human("Alex", "Goole", "10-05-1980", "Male")
        male_2 = Human("Rex", "Tpogn", "10-05-1950", "Male")
        male_3 = Human("Oppo", "Bollshit", "10-05-1900", "Male")
        female_1 = Human("Sandra", "Grace", "10-05-1980", "Female")
        female_2 = Human("Alisa", "Lolla", "10-05-1970", "Male")

        #call a bunch of functions
        male_1.sleep()
        male_1.eat()
        male_1.make_homework()
        male_2.sleep()
        male_2.move()
        male_3.eat()
        female_1.make_homework()
        female_2.speak()

        all_humans = [male_1, male_2, male_3, female_1, female_2]

        max_energy = max(all_humans, key=lambda h: h.energy)

        assert max_energy.name == "Oppo"
        assert max_energy.last_name == "Bollshit"
        assert max_energy.energy == 105


if __name__ == "__main__":
    pytest.main()
