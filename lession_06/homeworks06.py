# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
# def multiplication_table(number):
#     # Initialize the appropriate variable
#     multiplier = 1

#     # Complete the while loop condition.
#     while multiplier <= number:
#         result = number * multiplier
#         # десь тут помила, а може не одна
#         if  result > "25":
#             # Enter the action to take if the result is greater than 25
#             pass
#         print(str(number) + "x" + str(multiplier) + "=" + str(result))

#         # Increment the appropriate variable
#         multi += 1

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

def sum_numbers(first, second):
    """
    Function summarizes two numbers
    Args:
        first (integer or float): number
        second (integer or float): number
    Returns:
        integer : number (sum of first and second numbers)
    """
    return first + second

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    """
    Function that takes two strings and returns the index of the first
    occurrence of the second string in the first string
    Args:
        str1 (string): first line
        str2 (string): second line
    Returns:
        integer : index
    """
    index = str1.find(str2)
    return index

#     return -1

# str1 = "Hello, world!"
# str2 = "world"
# print(find_substring(str1, str2)) # поверне 7

# str1 = "The quick brown fox jumps over the lazy dog"
# str2 = "cat"
# print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
