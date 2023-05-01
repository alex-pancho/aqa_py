import unittest
from homework_10 import *

class TestGame(unittest.TestCase):

    def test_first_selected_hero(self):
        """Ursa's skills"""
        actual_result = hero_skills('Ursa')
        expected_result = {'power': 52, 'health': 600, 'speed': 6, 'money': 50}
        self.assertEqual(actual_result, expected_result)

    def test_second_selected_hero(self):
        """Warlock's skills"""
        actual_result = hero_skills('Warlock')
        expected_result = {'power': 14, 'health': 1200, 'speed': 4, 'money': 0}
        self.assertEqual(actual_result, expected_result)

    def test_rhird_selected_hero(self):
        """Luna's skills"""
        actual_result = hero_skills('Luna')
        expected_result = {'power': 42, 'health': 780, 'speed': 7, 'money': 20}
        self.assertEqual(actual_result, expected_result)

    def test01_first_hero_fight_action(self):
        """"Result of fight between Goblin and Ursa"""
        actual_result = fight_action('Goblin', 'Ursa', 'Fight')
        expected_result = 'Ursa'
        self.assertEqual(actual_result, expected_result, f"Ursa is stronger than Goblin")

    def test02_first_hero_fight_action(self):
        """"Result of fight between Rohan and Ursa"""
        actual_result = fight_action('Rohan', 'Ursa', 'Fight')
        expected_result = 'Rohan'
        self.assertEqual(actual_result, expected_result, f"Rohan is stronger than Ursa")

    def test03_second_hero_fight_action(self):
        """"Result of fight between Goblin and Warlock"""
        actual_result = fight_action('Goblin', 'Warlock', 'Fight')
        expected_result = 'Goblin'
        self.assertEqual(actual_result, expected_result, f"Goblin is stronger than Warlock")

    def test04_second_hero_fight_action(self):
        """"Result of fight between Rohan and Warlock"""
        actual_result = fight_action('Rohan', 'Warlock', 'Fight')
        expected_result = 'Rohan'
        self.assertEqual(actual_result, expected_result, f"Rohan is stronger than Warlock")

    def test05_third_hero_fight_action(self):
        """"Result of fight between Goblin and Luna"""
        actual_result = fight_action('Goblin', 'Luna', 'Fight')
        expected_result = 'Luna'
        self.assertEqual(actual_result, expected_result, f"Luna is stronger than Goblin")

    def test06_third_hero_fight_action(self):
        """"Result of fight between Rohan and Luna"""
        actual_result = fight_action('Rohan', 'Luna', 'Fight')
        expected_result = 'Rohan'
        self.assertEqual(actual_result, expected_result, f"Rohan is stronger than Luna")

if __name__ == "__main__":
    unittest.main(verbosity=2)
