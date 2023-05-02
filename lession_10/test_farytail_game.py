import io
import unittest
import sys
import pathlib
from unittest.mock import patch
from io import StringIO
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from lession_10.play_farytail_game import *
from lession_10.play_farytail_game import choose_character, characters

class TestMessages(unittest.TestCase):

    def test_hello_intro_message(self):
        """Test hello() function"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            hello()
            expected_result = "Привіт любий друже. Гайда пограємось в просту але цікаву гру.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_result, msg="The values not identical")

    def test_message_after_choose_opponent(self):
        '''Test msg after call shoose opponen'''
        with patch('sys.stdout', new=io.StringIO()) as faker_stdout:
            message_after_choose_opponent()
            expected_result = 'Щоб ти не сумував - я підіберу тобі опонента відповідно до твоїх навичок.\n'
            self.assertEqual(faker_stdout.getvalue(), expected_result, msg="The values not identical")


class TestChooseCharacter(unittest.TestCase):
    @patch('builtins.input', side_effect=['Котигорошко'])
    def test_valid_input(self, mock_input):
        expected = {'Котигорошко': characters['Котигорошко']}
        print("sdfsdf", expected)
        actual = choose_character()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Вовк'])
    def test_invalid_input(self, mock_input):
        with self.assertRaises(StopIteration):
            choose_character()

    @patch('builtins.input', side_effect=[1])
    def test_integer_inputs(self, mock_input):
        with self.assertRaises(StopIteration):
            choose_character()

    @patch('builtins.input', side_effect=[1.2])
    def test_float_inputs(self, mock_input):
        with self.assertRaises(StopIteration):
            choose_character()

    @patch('builtins.input', side_effect=[True])
    def test_bool_inputs(self, mock_input):
        with self.assertRaises(StopIteration):
            choose_character()

    @patch('builtins.input', side_effect=['<SCRIPT>allert()</SCRIPT>'])
    def test_html_injection_inputs(self, mock_input):
        with self.assertRaises(StopIteration):
            choose_character()

    @patch('builtins.input', side_effect=['%n%n%n%n%n%n%n%n... ...%n'])
    def test_format_str_injection_inputs(self, mock_input):
        with self.assertRaises(StopIteration):
            choose_character() \

    @patch('builtins.input', side_effect=[None])
    def test_none_injection_inputs(self, mock_input):
        with self.assertRaises(StopIteration):
            choose_character()


if __name__ == "__main__":
    unittest.main(verbosity=1)