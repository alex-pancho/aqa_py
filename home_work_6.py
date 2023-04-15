# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити/доповнити.
"""


def multiplication_table(number: int) -> None:
    """Ця функція друкує табличку множення на задане число з максимальним значенням добутку 25"""
    # Initialize the appropriate variable
    multiplier = 1
    # Complete the while loop condition.
    while number > 0:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f'{number} x {multiplier} = {result}')

        # Increment the appropriate variable
        multiplier += 1


# multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def summ_two_numbers(num_1: int | float, num_2: int | float) -> int | float:
    """Ця функція обчислює суму двох чисел"""
    return num_1 + num_2


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def avg_arifmethic(*args) -> float:
    """Ця функція рахує середнє арифметичне списку чисел"""
    return sum(args) / len(args)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def ryadok_vishneviy_kolo_hati(string: str) -> str:
    """Ця функція повертає заданий рядок у зворотньмоу порядку"""
    return string[::-1]


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def long_long_word(*words) -> str:
    """Ця функція повертає найдовше слово у списку"""
    maximum = ''
    for i in words:
        if len(i) > len(maximum):
            maximum = i
    return maximum


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str_1: str, str_2: str) -> int:
    """Ця функція знаходить входження другого рядка у перший, а у випадку відсутності передасть -1"""
    return str_1.find(str_2)


# str_1 = "Hello, world!"
# str_2 = "world"
# print(find_substring(str_1, str_2))  # поверне 7
#
# str1 = "The quick brown fox jumps over the lazy dog"
# str2 = "cat"
# print(find_substring(str1, str2))  # поверне -1

# task 7
# Домашня робота 4, завдання 3


def find_duplicates(*duplicates) -> str:
    """Ця функція знаходить дублікати у заданому списку"""
    return ['Дублікатів нема', 'Дублікати є'][len(duplicates) != len(set(duplicates))]


# task 8 Домашня робота 4, завдання 5


def swap(**kwargs) -> dict:
    """Ця функція повертає словник зі зміненими місцями ключами та значеннями"""
    return {item[1]: item[0] for item in kwargs.items()}


# task 9 Домашня робота 5, завдання 10


def even_numbers(*square_nums) -> list:
    """Ця функція повертає список квадратів парних чисел з заданого списку"""
    return [i ** 2 for i in square_nums if i % 2 == 0]


# task 10 Домашня робота 5, завдання 6


def summ_all_digits(num: str) -> int:
    """Ця функція рахує суму цифр у введеному числі"""
    return sum(int(i) for i in num)


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
