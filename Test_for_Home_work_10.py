from Home_work_10 import *
import unittest
import sys
import pathlib
from unittest.mock import patch
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))


class TestGame(unittest.TestCase):

    def test_select_character(self):
        with patch('builtins.input', return_value='Snake'):
            character = select_character()
            self.assertEqual(character, 'Snake')

        with patch('builtins.input', return_value='invalid'):
            with self.assertRaises(ValueError):
                select_character()

    def test_encounter(self):
        with patch('builtins.input', return_value=1):
            action = encounter('Snake')
            self.assertEqual(action, Action.DIALOGUE)

        with patch('builtins.input', return_value=2):
            action = encounter('Snake')
            self.assertEqual(action, Action.FIGHT)

        with patch('builtins.input', return_value=3):
            action = encounter('Snake')
            self.assertEqual(action, Action.ESCAPE)

        with patch('builtins.input', return_value='invalid'):
            with self.assertRaises(ValueError):
                encounter('Snake')

    def test_battle_1(self):
        with patch('game.random.randint', side_effect=[5, 10]):
            result = battle('Catigoroshko', 'Snake')
            self.assertEqual(result, 'defeat')

        with patch('game.random.randint', side_effect=[10, 5]):
            result = battle('Catigoroshko', 'Snake')
            self.assertEqual(result, 'victory')

        with patch('game.random.randint', return_value=5):
            result = battle('Catigoroshko', 'Snake')
            self.assertEqual(result, 'tie')

    def test_battle_2(self):
        def run_battle(player_roll, enemy_roll):
            with patch('game.random.randint', side_effect=[player_roll, enemy_roll]):
                return battle('Catigoroshko', 'Snake')

        self.assertEqual(run_battle(5, 10), 'defeat')
        self.assertEqual(run_battle(10, 5), 'victory')
        self.assertEqual(run_battle(5, 5), 'tie')
