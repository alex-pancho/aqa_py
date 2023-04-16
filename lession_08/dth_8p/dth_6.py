import unittest

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        if result > 25:
            #print(str(number) + "x" + str(multiplier) + "=" + str(result), "Значение выше 25")
            break
        else:
            #print(str(number) + "x" + str(multiplier) + "=" + str(result))
            multiplier += 1
multiplication_table(1)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def f(x1: int, x2: int):
    """
    Складывает два числа и возвращает их сумму.
    Аргументы:
    x1 (int): Первое слагаемое.
    x2 (int): Второе слагаемое.
    Возвращает:
    int: Сумма двух аргументов.
    """
    return x1 + x2
result = f(6, 5)
#print("# task 2", result)

# task 3
x1 = [1, 2, 3, 4]
def ever(x1):
    """
    Разчет среднего арифметического числа списка
    Аргументы:
    x1 (int): Список чис
    Возвращает:
    float: Сумма всех чисел списка деленная на их количество.
    """
    if len(x1) == 0:
        return 0
    else:
        return sum(x1) / len(x1)
#print("# task 3", ever(x1))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
x = "Известный астролог рассказал, когда свергнут режим диктатора Путина."
def text(x) -> str:
    """
    Вывод переменной в обратном порядке
    Аргументы:
    x (str): Текст
    Возвращает:
    str: Текст в обратном порядке
    """
    return x[::-1]
#print("# task 4", text(x))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
person_list = ["Alice", "Boby", "Charlie", "David", "Emma", "Frank"]

def longest_word(person_list):
    """
    Вывод самого длинного имени
    Аргументы:
    person_list (Any): Список имен
    Возвращает:
    str: Самое длинное имя
    """
    return max(person_list, key=len)
#print("# task 5", longest_word(person_list))
# task 6

"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    """
    Возврат индекса первого вхождения второго ряда в
    первый при условии, что второй ряд является подрядом первого.
    В случае если второй ряд не является подрядом первого выводится значение -1.
    Аргументы:
    str1 (str): Первый ряд
    str2 (str): Второй
    Возвращает:
    int: Место расположение второго аргумента в первом, либо его отсутствие.
    """
    if str1.find(str2):
        return str1.find(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
#print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
#print("# task 6", find_substring(str1, str2)) # поверне -1

# task 7
"""Перевірте, чи є в списку big_list дублікати"""
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
new_clear_list = []
def clear_list(new_clear_list)-> int:
    """
    Проверка наличия в списке дубликатов
    Аргументы:
    big_list (int): Список чисел
    new_clear_list (list): Переменная
    Возвращает:
    list[lint]: Список чисел без дубликатов.
    """
    for i in big_list:
        if i not in new_clear_list:
            new_clear_list.append(i)
    return new_clear_list
#print("# task 7", clear_list(new_clear_list))
# task 8. Обчисліть суму елементів двох множин, які не є спільними

set_3 = {1, 2, 3, 4, 5}
set_4 = {4, 6, 5, 10}
def sum1(set_3, set_4):
    """
    Вычсчитывает сумму элементов двух множеств, которые не являются общими
    Аргументы:
    set_3(int): Список чисел
    set_4(int): Список чисел
    Возвращает:
    int: Сумма элементов двух множеств, которые не являются общими.
    """
    return sum(set_3 ^ set_4)
#print("# task 8", sum(set_3 ^ set_4))


# task 9 Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

x1 = [1, 2, 3, 4]
y2 = [3, 4, 5, 6]
def list3(x1, y2):
    """
    Выводит сет из обоих списков в 1, с числами которые встречаються только один раз.
    Аргументы:
    x1 (int): Список чисел
    x2 (int): Список чисел
    Возвращает:
    int: Два сета в 1м без дубликатов
    """
    list1 = set(x1)
    list2 = set(y2)
    return list1 ^ list2
#print("# task 9", list3(x1 ,y2))
# task 10
"""
Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
def frt(fruits):
    result = []
    for fruit in fruits:
        if fruit != "orange":
            result.append(fruit)
    return result

# task 11. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
def uni(small_list):
    return set(small_list)
#print(uni(small_list))

# task 12. Знайдіть середнє арифметичне всіх елементів у списку small_list
def list22(small_list):
    z = sum(small_list)
    y = len(small_list)
    return z/y
#print("# task 2 ", list22(small_list))

# task 13. Перевірте, чи є в списку big_list дублікати
def dup(big_list):
    nlist = []
    for item in big_list:
        if item not in nlist:
            nlist.append(item)
    return nlist
#print("# task 3 ", dup(big_list))

