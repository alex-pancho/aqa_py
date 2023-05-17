# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    """Print multiplication table up to max value 25"""
    multiplier = 1

    while multiplier <= 25:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(4)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_nums(x, y):
    """Calculating the sum of two numbers"""
    summa = x + y
    return print(f"Сума числа {x} та {y} дорівнює {summa}.")
#sum_two_nums(3, 7)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
numbers_list = [1, 2, 3, 4]

def arithmetical_mean(numbers):
    """Calculate arithmetical mean"""
    return print(f"{sum(numbers) / len(numbers)}")

#arithmetical_mean(numbers_list)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(string_to_reverse):
    """Reverse a string"""
    return string_to_reverse[::-1]

string = "Купила мама коника"
reversed = reverse_string(string)
print(reversed)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
word_list = ["one", "a", "quartern", "engage"]
def longest_word(words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
#print(f"Найдовше слово в списку: {longest_word(word_list)}.")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    """Check substring index"""
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1

#str1 = "Hello, world!"
#str2 = "world"
#print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
def upper_count(text):
    """Counts number of uppercase letters in a text"""
    upper_counter = 0
    for i in text:
        if i.isupper():
            upper_counter += 1
    print(f"В тексті {upper_counter} слів починається з великої літери.")

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Cras volutpat, arcu vitae efficitur euismod, metus tortor rutrum ex, quis tempus lectus nunc a ligula. 
Etiam ultricies rhoncus imperdiet. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
Nam tortor dui, semper at enim sit amet, iaculis pharetra nisl. Sed non aliquet lorem. In rhoncus orci urna, vel tempus nulla varius a. 
Aliquam consequat semper nulla quis auctor. Integer aliquet elit eget mattis tristique. Duis vitae lectus orci. 
Nam blandit enim mauris, non rhoncus orci tempor sit amet. Sed non nunc dolor.
 Aenean scelerisque ligula felis, nec rhoncus risus pellentesque tempus. In hac habitasse platea dictumst."""
upper_count(text)


def set_difference_sum(set1, set2):
    """Calculate the summ of different values in two sets"""
    set_1_difference = set_1.difference(set_2)
    set_2_difference = set_2.difference(set_1)
    sum_differ = sum(set_1_difference) + sum(set_2_difference)
    print(f"Сума значень двох множин, які не є спільними: {sum_differ}.")

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
set_difference_sum(set_1, set_2)

def calculate_digits(number: int) -> int:
    """Calculate the summ of all digits in a number."""
    total_sum = 0
    for digit in str(number):
        total_sum += int(digit)
    print(f"Сума цифр числа {number} дорівнює {total_sum}.")
    return total_sum

calculate_digits(12345)


def switch_keys_values(basedict):
    get_keys = set(basedict.keys())
    get_values = set(basedict.values())
    new_dict = dict(zip(get_values, get_keys))
    return print("Словник в якому ключі та значення замінені місцями: ", new_dict)

original_dict = {'One' : '1', 'Two' : "2", "Three" : "3"}

switch_keys_values(original_dict)