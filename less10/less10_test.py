import unittest 
import less10 
from less10 import InvalidInputException

    # example
    # def test_smoke_adding_function(self):
    #     "Test adding function"
    #     actual_result = less6.sum_of_two(2,3)
    #     expected_result = 5
    #     self.assertEqual(actual_result, expected_result)


class my_unittests(unittest.TestCase):

    def test_01_fight_action(self):
        "Smoke test for function of fight action"
        actual_result = less10.fight(100,50)
        expected_result = "Wow! You win!"
        self.assertEqual(actual_result, expected_result)

    def test_02_fight_action_user_loses(self):
        "If fight action if user loses"
        actual_result = less10.fight(80,100)
        expected_result = "Oops! You lose, R.I.P."
        self.assertEqual(actual_result, expected_result)

    def test_03_fight_action_draw(self):
        "If fight action results in draw"
        actual_result = less10.fight(50,50)
        expected_result = "It's a draw! Come back later"
        self.assertEqual(actual_result, expected_result)

    def test_04_fight_action_negat_nums(self):
        "If fight action if there are negative numbers"
        actual_result = less10.fight(-100,-80)
        expected_result = "Oops! You lose, R.I.P."
        self.assertEqual(actual_result, expected_result)    

    def test_05_defying_player(self):
        "How program defines character of player"
        actual_result = less10.define_player("1")
        expected_result = {"name":"Geralt", "power" : 100}
        self.assertEqual(actual_result, expected_result)

    def test_06_nonexisting_character(self):
        "If player choses non-existing character"
        self.assertRaises(InvalidInputException, less10.define_player, "10")

    def test_07_defying_opponent(self):
        "How program defines opponents"
        actual_result = less10.define_opponents("1")
        expected_result = {'2': {'name': 'Bruxa', 'power': 80}, '3': {'name': 'Werewolf', 'power': 50}}
        self.assertEqual(actual_result, expected_result)

    def test_08_defying_opponent_nonexist_char(self):
        "If player choses non-existing character"
        self.assertRaises(InvalidInputException, less10.define_opponents, "10")

    def test_09_nonexisting_action(self):
        "If player choses non-existing character"
        self.assertRaises(InvalidInputException, less10.choosing_action, "10")





if __name__ == '__main__':
    unittest.main(verbosity=2)
