import unittest
import sys
import pathlib
import the_game
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))


class TestGame(unittest.TestCase):

    def test_curculator_minus(self):
        """Курка віднімає"""
        actual_result = the_game.curculator(5, 2, 'мінус')
        expected_result = f'Курка каже: {float(5 - 2)}\n' \
                          f'Ви отримали 1 бал!\n' \
                          f'Ви втратили 1 енергії'
        self.assertEqual(actual_result, expected_result, msg='Неправильно. 5 мінус 2 = 3.0')

    def test_curculator_plus(self):
        """Курка додає"""
        actual_result = the_game.curculator(5, 2, 'плюс')
        expected_result = f'Курка каже: {float(5 + 2)}\n' \
                          f'Ви отримали 1 бал!\n' \
                          f'Ви втратили 1 енергії'
        self.assertEqual(actual_result, expected_result, msg='Неправильно. 5 плюс 2 = 7.0')

    def test_curculator_divide(self):
        """Курка ділить"""
        actual_result = the_game.curculator(5, 2, 'ділення')
        expected_result = f'Курка каже: {float(5 / 2)}\n' \
                          f'Ви отримали 1 бал!\n' \
                          f'Ви втратили 1 енергії'
        self.assertEqual(actual_result, expected_result, msg='Неправильно. 5 поділити 2 = 2.5')

    def test_curculator_multiplication(self):
        """Курка множить"""
        actual_result = the_game.curculator(5, 2, 'помножити')
        expected_result = f'Курка каже: {float(5 * 2)}\n' \
                          f'Ви отримали 1 бал!\n' \
                          f'Ви втратили 1 енергії'
        self.assertEqual(actual_result, expected_result, msg='Неправильно. 5 помножити на 2 = 10.0')

    def test_curculator_divide_zero(self):
        """Курка ділить на нуль"""
        actual_result = the_game.curculator(5, 0, 'поділити')
        expected_result = f'Курка дзьобає Вас у лоба і правильно робить, тому що на нуль ділити не можна!\n' \
                          f'Ви втратили 10 балів!\n' \
                          f'Ви втратили 1 енергії'
        self.assertEqual(actual_result, expected_result, msg='Неправильно. На нуль ділити не можна!')

    def test_curculator_exponentiation(self):
        """Курка зводить у ступінь"""
        actual_result = the_game.curculator(5, 2, 'ступінь')
        expected_result = f'Курка каже: {float(5 ** 2)}\n' \
                          f'Ви отримали 1 бал!\n' \
                          f'Ви втратили 1 енергії'
        self.assertEqual(actual_result, expected_result, msg='Неправильно. 5 у ступіні 2 = 25.0')

    def test_palindrom_word_yes(self):
        """Слово паліндром"""
        actual_result = the_game.palindrom_word('казак')
        expected_result = f'Це паліндром!\n' \
                          f'Ваша енергія зменшилась на 2\n' \
                          f'Ви отримали 2 бали!'
        self.assertEqual(actual_result, expected_result, msg='Ахтунг! Це не паліндром!')

    def test_palindrom_word_no(self):
        """Слово паліндром"""
        actual_result = the_game.palindrom_word('python')
        expected_result = f'На жаль це не паліндром :(\n' \
                          f'Ваша енергія зменшилась на 2'
        self.assertEqual(actual_result, expected_result, msg='Ахтунг! Це паліндром!')

    def test_curculator_percent(self):
        """Курка бере відсоток першого числа від другого"""
        actual_result = the_game.curculator(5, 25, 'відсоток')
        expected_result = f'Курка каже: {(25 / 100) * 5}%\n' \
                          f'Ви отримали 1 бал!\n' \
                          f'Ви втратили 1 енергії'
        self.assertEqual(actual_result, expected_result, msg='Неправильно! 5 відсотків від 25 це 1.25!')

    if __name__ == '__main__':
        unittest.main(verbosity=2)
