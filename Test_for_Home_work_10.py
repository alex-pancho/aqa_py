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
        with patch('builtins.input', return_value='1'):
            action = encounter('Snake')
            self.assertEqual(action, 1)

        with patch('builtins.input', return_value='invalid'):
            with self.assertRaises(ValueError):
                encounter('Snake')

    def test_battle(self):
        with patch('game.random.randint', side_effect=[5, 10]):
            result = battle('Catigoroshko', 'Snake')
            self.assertEqual(result, 'defeat')

        with patch('game.random.randint', side_effect=[10, 5]):
            result = battle('Catigoroshko', 'Snake')
            self.assertEqual(result, 'victory')

        with patch('game.random.randint', return_value=5):
            result = battle('Catigoroshko', 'Snake')
            self.assertEqual(result, 'tie')

    def select_character(self):
        actual_result = select_character(ValueError)
        expect_result = "Invalid character selection"
        self.assertEqual(actual_result, expect_result)

    def encounter(self):
        actual_result = encounter(1, 2, 3)
        expect_result = "action"
        self.assertEqual(actual_result, expect_result)
