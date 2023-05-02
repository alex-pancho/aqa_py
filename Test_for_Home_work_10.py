from Home_work_10 import *
import unittest
import sys
import pathlib
from io import StringIO
from unittest.mock import patch
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))


class TestGame(unittest.TestCase):

    def test_select_character(self):
        """
        Test select_character function
        """
        # Test selecting a valid character
        with patch('builtins.input', return_value='Snake'):
            character = select_character()
            self.assertEqual(character, 'Snake')

        # Test selecting an invalid character
        with patch('builtins.input', return_value='invalid'):
            with self.assertRaises(ValueError):
                select_character()

    def test_select_invalid_character(self):
        """
         Test selecting an invalid character
        """
        with patch('builtins.input', return_value='InvalidCharacter'):
            with self.assertRaises(ValueError):
                select_character()

    def test_encounter(self):
        """
        Test encounter function
        """
        # Test selecting a valid action
        with patch('builtins.input', return_value=1):
            action = encounter('Snake')
            self.assertEqual(action, Action.DIALOGUE)

        with patch('builtins.input', return_value=2):
            action = encounter('Snake')
            self.assertEqual(action, Action.FIGHT)

        with patch('builtins.input', return_value=3):
            action = encounter('Snake')
            self.assertEqual(action, Action.ESCAPE)

    def test_encounter_with_catigoroshko(self):
        """
        Test encounter function with Catigoroshko enemy
        """
        with patch('builtins.input', return_value=1):
            action = encounter('Catigoroshko')
        self.assertEqual(action, Action.DIALOGUE)

        with patch('builtins.input', return_value=2):
            action = encounter('Catigoroshko')
        self.assertEqual(action, Action.FIGHT)

        with patch('builtins.input', return_value=3):
            action = encounter('Catigoroshko')
        self.assertEqual(action, Action.ESCAPE)

    def test_encounter_with_horse(self):
        """
         Test encounter function with Horse enemy
        """
        with patch('builtins.input', return_value=1):
            action = encounter('Horse')
        self.assertEqual(action, Action.DIALOGUE)

        with patch('builtins.input', return_value=2):
            action = encounter('Horse')
        self.assertEqual(action, Action.FIGHT)

        with patch('builtins.input', return_value=3):
            action = encounter('Horse')
        self.assertEqual(action, Action.ESCAPE)

    def test_encounter_with_Snake(self):
        """
        Test encounter function with Snake enemy
        """
        with patch('builtins.input', return_value=1):
            action = encounter('Snake')
        self.assertEqual(action, Action.DIALOGUE)

        with patch('builtins.input', return_value=2):
            action = encounter('Snake')
        self.assertEqual(action, Action.FIGHT)

        with patch('builtins.input', return_value=3):
            action = encounter('Snake')
        self.assertEqual(action, Action.ESCAPE)

        # Test selecting an invalid action
        with patch('builtins.input', side_effect=[0, 4, "invalid", ""]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                action = encounter("Horse")
                self.assertIsNone(action)
                self.assertIn("Invalid action selection", fake_out.getvalue())
                action = encounter("Snake")
                self.assertIsNone(action)
                self.assertIn("Invalid action selection", fake_out.getvalue())
                action = encounter("Catigoroshko")
                self.assertIsNone(action)
                self.assertIn("Invalid action selection", fake_out.getvalue())
                action = encounter("Horse")
                self.assertIsNone(action)
                self.assertIn("Invalid action selection", fake_out.getvalue())

        # Test entering an invalid input for the action selection
        with patch('builtins.input', return_value='invalid'):
            with self.assertRaises(ValueError):
                encounter('Snake')

    def test_battle(self):
        """
        Test battle function
        """
        # Test when the player defeats the enemy
        result = battle("Catigoroshko", "Snake")
        self.assertIsNotNone(result)

        # Test when the enemy defeats the player
        result = battle("Snake", "Catigoroshko")
        self.assertIsNotNone(result)

        # Test when there is a tie
        result = battle("Horse", "Horse")
        self.assertEqual(result, "tie")

    def test_battle_1(self):
        """
        Test battle function with mock dice rolls
        """
        # Test when the enemy has a higher roll
        with patch('game.random.randint', side_effect=[5, 10]):
            result = battle('Catigoroshko', 'Snake')
            self.assertEqual(result, 'defeat')

        # Test when the player has a higher roll
        with patch('game.random.randint', side_effect=[10, 5]):
            result = battle('Catigoroshko', 'Snake')
            self.assertEqual(result, 'victory')

        # Test when there is a tie
        with patch('game.random.randint', return_value=5):
            result = battle('Catigoroshko', 'Snake')
            self.assertEqual(result, 'tie')

    def test_battle_2(self):
        """
        Test battle function with mock dice rolls
        """
        def run_battle(player_roll, enemy_roll):
            """
        Helper function to run a single battle with mock dice rolls.

        Args:
        player_roll (int): Mock roll for the player.
        enemy_roll (int): Mock roll for the enemy.

        Returns:
        str: The result of the battle, as returned by the battle function.
        """
            with patch('game.random.randint', side_effect=[player_roll, enemy_roll]):
                return battle('Catigoroshko', 'Snake')
        # Test a victory for the enemy
        self.assertEqual(run_battle(5, 10), 'defeat')
        # Test a victory for the player
        self.assertEqual(run_battle(10, 5), 'victory')
        # Test a tie
        self.assertEqual(run_battle(5, 5), 'tie')

    def test_play_game(self):
        # Test that the game can be played without errors
        with patch('builtins.input', side_effect=['Snake', 2]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                play_game()
                self.assertNotIn("Invalid", fake_out.getvalue())

        # Test that the game ends with victory or defeat
        with patch('builtins.input', side_effect=['Catigoroshko', 2]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                play_game()
                result = fake_out.getvalue().split(":")[-1].strip()
                self.assertIn(result, ["victory!", "defeat."])
