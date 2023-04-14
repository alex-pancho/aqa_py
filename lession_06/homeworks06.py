# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_num(a, b):
    return (a + b)
sum_num(4,5)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def avg_num(*data):
    for num in data:
        return sum(num) / len(num)
avg_num([2,2,2,2])

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse(text):
    return text[::-1]
reverse('Would you tell me, please, which way I ought to go from here?')

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(word_list):
    word_len = []
    for x in word_list:
        word_len.append((len(x), x))
    word_len.sort()
    return word_len[-1][1]

longest_word(['apple', 'kiwi', 'cherry'])


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)
 
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

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

def upper_count(text:str)-> int:
    """ Function counts how many words in the text begin with a capital letter"""
    return sum(word[0].isupper() for word in text)
upper_count("Couldn't be much more from the heart\n"
             "Forever trusting who we are\n"
              "And nothing else matters")


def characters_set(line:str)-> set:
    """Set of all characters included in the given string"""
    return set(list(line))

characters_set("Something's wrong, shut the light, heavy thoughts tonight")

def color_game(*colors:list)-> str:
    """Awarding points depending on the selected color"""
    for color in colors:
        if color == 'green':
            print('You just earned 5 points')
        elif color == 'red':
            print('You just earned 15 points')
        else:
            print('You just earned 10 points')

color_game('green', 'yellow', 'red')

def digits_sum(number:int) -> int:
    """Calculate the sum of all digits of a natural number"""
    sum = 0
    while(number > 0):
        dig = number % 10
        sum = sum + dig
        number = number//10
    return sum

digits_sum(12345)


    