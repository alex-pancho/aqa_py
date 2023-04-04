# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    max_value = 25

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result >= max_value:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1 # Increment the appropriate variable


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
#solution 1
def sum_two_numbers(num_1:int, num_2:int):
    return num_1 + num_2

# print(sum_two_numbers(1, 10))

#solution 2
def sum_two_numbers_v():
    numb_1 = int(input("Input first number: "))
    numb_2 = int(input("Input second number: "))
    return numb_1 + numb_2

# print(sum_two_numbers_v())


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
#solution 1
def mean_everage():
    """ Get mean average of list values"""
    digits_list =[i for i in range(0, 10)]
    mean_res = sum(digits_list) / len(digits_list)
    return mean_res

# print("Mean average:",mean_everage())

#solution 2

def mean_average(number_list):
    mean_resultat = sum(number_list) / len(number_list)
    return mean_resultat

some_numb_list = [2, 5, 7, 9, 2]
result = mean_average(some_numb_list)
# print(result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def get_contrary_string():
    your_string = str(input("Give me some string and I'll convert it: "))

    rever_str = ''.join(reversed(your_string))
    return rever_str

# print("Here is your reversed string:", get_contrary_string())

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def get_maximum_length_word_list(lst_words):
    if len(lst_words) == 0:
        print("Empty list. Please, try again...")
    else:
        logest_word_in_list = max(lst_words, key=len)
        return logest_word_in_list

print(get_maximum_length_word_list(["Написати", "функцію", "яка", "приймає", "список", "слів"]))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    """Get 1st index of second str"""
    index = str1.find(str2)
    return index

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
##################################-Task 7-##########################################

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##Homewor3 task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
def separate_sawer_end_sentanse(snippet_sawer_story):
    adwentures_of_tom_sawer_sentences = snippet_sawer_story.split('\n')
    return adwentures_of_tom_sawer_sentences

# print(separate_sawer_end_sentanse(adwentures_of_tom_sawer))


##################################-Task 8-##########################################
#Homewor3 task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
def get_words_final_sentance(separate_sawer_end_sentanse):
    temp = separate_sawer_end_sentanse(adwentures_of_tom_sawer)
    last_sentence = temp[-1]
    # print(type(last_sentence))
    words_in_last_sent = last_sentence.split()
    return  last_sentence,  len(words_in_last_sent)


last_sentence, words_count = get_words_final_sentance(separate_sawer_end_sentanse)
print(f"Last sentence is <{last_sentence}> and number of words in last sentence: {words_count}")
