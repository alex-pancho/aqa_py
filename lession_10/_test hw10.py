import unittest
import hw10_game as h


class TestHomeWorks10(unittest.TestCase):

    # select hero tests

    def test01_select_hero(self):  # Equivalence partitioning
        """Positive:
        Case send correct hero key args.
        Expected:
        AI hero, Player hero, available heroes list."""

        actual_result = h.select_hero('a', {'a': 'key1', 'b': 'key2', 'c': 'key3'})
        expected_result_1 = ('key1', 'key2', ['key3'])
        expected_result_2 = ('key1', 'key3', ['key2'])
        self.assertIn(actual_result, [expected_result_1, expected_result_2])

    def test02_select_hero(self):  # Equivalence partitioning
        """Positive:
        Case send correct hero key args.
        Expected:
        AI hero, Player hero, available heroes list."""

        actual_result = h.select_hero('b', {'a': 'key1', 'b': 'key2', 'c': 'key3'})
        expected_result_1 = ('key2', 'key1', ['key3'])
        expected_result_2 = ('key2', 'key3', ['key1'])
        self.assertIn(actual_result, [expected_result_1, expected_result_2])

    def test03_select_hero(self):  # Equivalence partitioning
        """Positive:
        Case send correct hero key args.
        Expected:
        AI hero, Player hero, available heroes list."""

        actual_result = h.select_hero('c', {'a': 'key1', 'b': 'key2', 'c': 'key3'})
        expected_result_1 = ('key3', 'key2', ['key1'])
        expected_result_2 = ('key3', 'key1', ['key2'])
        self.assertIn(actual_result, [expected_result_1, expected_result_2])

    def test04_select_hero(self):  # Equivalence partitioning
        """Negative:
        Case send incorrect hero key args.
        """

        actual_result = h.select_hero('d', {'a': 'key1', 'b': 'key2', 'c': 'key3'})
        self.assertIsNone(actual_result)

    def test05_select_hero(self):  # Equivalence partitioning
        """Negative:
        Case send incorrect hero key args.
        """

        h.select_hero('d', {'a': 'key1', 'b': 'key2', 'c': 'key3'})
        self.assertRaises(KeyError)

    # is_ai_gues_answered tests

    def test01_is_ai_guess_answered(self):
        """
        Positive:
        Correct number answer
        """
        actual_result = h.is_ai_guess_answered(user_answer='121', ai_hero=h.warrior)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test02_is_ai_guess_answered(self):
        """
        Positive:
        Incorrect number answer
        """
        actual_result = h.is_ai_guess_answered(user_answer='11', ai_hero=h.warrior)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test03_is_ai_guess_answered(self):
        """
        Positive:
        Incorrect not number answer
        """
        h.is_ai_guess_answered(user_answer='test', ai_hero=h.warrior)
        self.assertRaises(ValueError)

    # contact tests

    def test01_contact(self):
        """
        Positive:
        Battle win player send (strong test hero)
        """
        actual_result = h.contact(player_hero=h.pm, ai_hero=h.warrior, user_answer='F')
        expected_result = h.pm.name
        self.assertEqual(actual_result, expected_result)

    def test02_contact(self):
        """
        Positive:
        Battle win AI send (strong test hero)
        """
        actual_result = h.contact(player_hero=h.warrior, ai_hero=h.pm, user_answer='F')
        expected_result = h.pm.name
        self.assertEqual(actual_result, expected_result)

    def test03_contact(self):
        """
        Positive:
        Test run option
        """
        actual_result = h.contact(player_hero=h.warrior, ai_hero=h.pm, user_answer='R')
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test04_contact(self):
        """
        Negative :
        Send incorrect user answer
        """
        actual_result = h.contact(player_hero=h.warrior, ai_hero=h.pm, user_answer='test')
        self.assertIsNone(actual_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
