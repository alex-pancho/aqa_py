import unittest
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from HW_Kuznetosv_8.dth_6 import *


class MyTestCase(unittest.TestCase):
    def test_task_1(self):
        """Проверка работы функции с пустым значением равным 0"""
        actual_result = ever([1, 2, 3, 4])
        expected_result = 0
        self.assertEqual(actual_result, expected_result, msg="\nРасчет среднего арифметического числа списка "
                                                             "\nАргументы: x1 (int): Список чисел "
                                                             "\nВозвращает: float: Сумма всех чисел списка деленная на их количество.")

    def test_task_2(self):
        """Проверка работы функции с значением введеным не в обратном порядке """
        actual_result = text("Известный астролог рассказал, когда свергнут режим диктатора Путина.")
        expected_result = "Известный астролог рассказал, когда свергнут режим диктатора Путина."
        self.assertEqual(actual_result, expected_result, msg="\nВывод переменной в обратном порядке"
                                                             "\nАргументы:x (str): Текст"
                                                             "\nВозвращает:str: Текст в обратном порядке")

    def test_task_3(self):
        """Проверка работы вывода не самого длинного имени"""
        actual_result = longest_word(["Alice", "Boby", "Charlie", "David", "Emma", "Frank"])
        expected_result = "Boby"
        self.assertEqual(actual_result, expected_result, msg="\nВывод самого длинного имени"
                                                             "\nАргументы:person_list (Any): Список имен"
                                                             "\nВозвращает:str: Самое длинное имя")

    def test_task_4(self):
        """Проверка вхождения второго ряда в первый"""
        actual_result = find_substring(str1, str2)
        expected_result = -1
        self.assertEqual(actual_result, expected_result,
                         msg="\nВозврат индекса первого вхождения второго ряда в первый при условии, "
                             "\nчто второй ряд является подрядом первого. \n"
                             "\nВ случае если второй ряд не является подрядом первого выводится значение -1"
                             "\nstr1 (str): Первый ряд"
                             "\nstr2 (str): Второй"
                             "\nint: Место расположение второго аргумента в первом, либо его отсутствие.")

    def test_task_5(self):
        """Проверка наличия в списке дубликатов"""
        actual_result = clear_list([3, 5, -2, -1, -3, 0, 1, 4, 5, 2])
        expected_result = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
        self.assertEqual(actual_result, expected_result, msg="\nПроверка наличия в списке дубликатов"
                                                             "\nАргументы:big_list (int): Список чисел"
                                                             "\nnew_clear_list (list): Переменная"
                                                             "\nВозвращает:list[lint]: Список чисел без дубликатов.")

    def test_task_6(self):
        """Проверка работы функции с недостающим значением в сете"""
        actual_result = list3(x1, y2)
        expected_result = {1, 2, 5}
        self.assertEqual(actual_result, expected_result,
                         msg="\nВыводит сет из обоих списков в 1, с числами которые встречаются только один раз."
                             "\nАргументы: x1 (int): Список чисел "
                             "\nx2 (int): Список чисел"
                             "\nВозвращает: int: Два сета в 1м без дубликатов")

    def test_task_7(self):
        """Проверка работы функции содержащем корректные значения """
        actual_result = uni([3, 1, 4, 5, 2, 5, 3])
        expected_result = {1, 2, 3, 4, 5}
        self.assertEqual(actual_result, expected_result, msg="\nВыводит все уникальные числа из списка."
                                                             "\nАргументы: small_list(int): Список чисел"
                                                             "\nВозвращает: int: список уникальных чисел")

    def test_task_8(self):
        """Проверка работы функции с значением равным 0"""
        actual_result = list22([3, 1, 4, 5, 2, 5, 3])
        expected_result = 0
        self.assertEqual(actual_result, expected_result, msg="\nНаходит среднее арифметическое из списка чисел."
                                                             "\nАргументы: small_list(int): Список чисел"
                                                             "\nВозвращает: int:Среднее арифметическое")

    def test_task_9(self):
        """Проверка работы функции с значением выше чем ОР"""
        actual_result = sum1(set_3, set_4)
        expected_result = 23
        self.assertEqual(actual_result, expected_result,
                         msg="\nВысчитывает сумму элементов двух множеств, которые не являются общими."
                             "\nset_3(int): Список чисел"
                             "\nset_4(int): Список чисел"
                             "\nВозвращает: int:Сумма элементов двух множеств, которые не являются общими")

    def test_task_10(self):
        """Проверка работы функции с пустым списком"""
        actual_result = frt(["apple", "banana", "orange", "grape", "mango"])
        expected_result = []
        self.assertEqual(actual_result, expected_result, msg="\nВывод на экран всех фруктов кроме апельсина."
                                                             "\nfrt (str): Список фруктов"
                                                             "\nВозвращает: (str):Вывод на экран всех фруктов кроме апельсина")


if __name__ == "__main__":
    unittest.main(verbosity=2)
#1