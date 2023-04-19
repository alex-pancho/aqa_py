# task 1
""" Задача
1 надрукувати табличку множення на задане число,
2 але лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
#Варіант1
def multiplication_table(number):
    """
    The function takes a number and returns a multiplication table for that number
    """
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number or multiplier > number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1
    return(result)

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

##Варіант2. Мені здається тут більш логічне рішення
def multiplication_table(entry_number):
    iteration_number = 1
    result = 1

    while result < 25:
        print(f"{entry_number}x{iteration_number}={result}")
        result = entry_number * iteration_number
        iteration_number += 1
        if result >= 25:
            break

multiplication_table(3)



# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def total_plus(number_1, number_2):
    """
    The function takes two numbers and returns their sum.
    """
    total_sum = number_1 + number_2
    print(f"The sum of {number_1}+{number_2}={total_sum}")
    return(total_sum)

total_plus(2,3)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def numbers_list(list1):
    """
    The function takes a list with numbers and returns their arithmetic mean.
    """
    numbers_list_len = len(list1)
    numbers_list_sum = sum(list1)
    total_number = numbers_list_sum / numbers_list_len
    print(f"The average of numbers list is {total_number}")
    return(total_number)

numbers_list([5,2,1,11])

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(my_string):
    """
    The function takes a string and returns it in reverse.
    """
    my_reverse_string = my_string[::-1]
    print(f"Reverse of the string is: {my_reverse_string}")
    return(my_reverse_string)

reverse_string("Hello. How r u?")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_list_word(words_list):
    """
    The function takes a list of words and returns the longest word in the list.
    """

    longest_word = words_list[0]
    for i in words_list:
        if len(i) > len(longest_word):
            longest_word = i
    print(f"The key with max value is: {longest_word}")
    return longest_word

longest_list_word(["a", "elephant", "ab", "abc", "abcde", "abcd"])

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    """
    The function takes two strings and returns the index of the first occurrence of the second string in the first string,
    if the second string is a substring of the first string, and -1 if the second string is not a substring of the first string.
    """
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7 Знайдіть всі унікальні елементи в списку small_list
def unique_elements(small_list):
    """
     The function takes a list and returns all unique elements
    """
    small_list_set = set(small_list)
    return small_list_set

small_list = [3, 1, 4, 5, 2, 5, 3]
unique_elements_list = unique_elements(small_list)
print (f"All unique elements from the 'small_list' are: \n {unique_elements_list}")

# task 8 Перевірте, чи є в списку big_list дублікати
def duplicates_check(big_list):
    """
    This function takes a list and checks if there is a duplicates in the list.
    """
    big_set = set(big_list)
    if len(big_set) < len(big_list):
        print("There are duplicate/s in the 'big_list'")
        return True
    else:
        print("There are no duplicates in the 'big_list'")
        return False

big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
duplicates_check(big_list)

# task 9. Напишіть програму, яка знаходить суму всіх цифр натурального числа.
def number_sum(number):
    """
    This function takes a string and calculates the sum of its digits.
    It returns the sum of digits.
    """

def number_sum(number):
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    return sum

result = number_sum('12345')
print("Sum of digits in number: ", result)


# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
#Обчисліть суму елементів двох множин, які не є спільними
def uncommon_num(set_1, set_2):
    """
    This function takes two sets and calculates the sum of elements in the two sets that are not common.
    """
    uncommon_set = set_1 ^ set_2
    return sum(uncommon_set)

result = uncommon_num({1, 2, 3, 4, 5}, {4, 6, 5, 10})
print(f"The sum of elements in 2 sets that are not сommon is {result}")
