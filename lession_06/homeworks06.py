# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number:int) ->int:
    '''Повертає результат таблички множення на задане число'''
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
        # print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1 # Increment the appropriate variable


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
#solution 1
def sum_two_numbers(num_1:int, num_2:int):
    '''Обчислення суми 2х чисел. Варіант 1'''
    return num_1 + num_2

# print(sum_two_numbers(1, 10))

#solution 2
def sum_two_numbers_v():
    '''Обчислення суми 2х чисел. Варіант 2'''
    numb_1 = int(input("Input first number: "))
    numb_2 = int(input("Input second number: "))
    return numb_1 + numb_2

# print(sum_two_numbers_v())


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
#solution 1
def mean_everage():
    '''Get mean average of list values'''
    digits_list =[i for i in range(0, 10)]
    mean_res = sum(digits_list) / len(digits_list)
    return mean_res

# print("Mean average:",mean_everage())

#solution 2

def mean_average(number_list: int):
    ''' Get mean average of list values. Var2'''
    mean_resultat = sum(number_list) / len(number_list)
    return mean_resultat

some_numb_list = [2, 5, 7, 9, 2]
result = mean_average(some_numb_list)
# print(result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def get_contrary_string():
    '''Get revers string'''
    your_string = str(input("Give me some string and I'll convert it: "))

    rever_str = ''.join(reversed(your_string))
    return rever_str

# print("Here is your reversed string:", get_contrary_string())

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def get_maximum_length_word_list(lst_words: list[str]) -> str:
    '''Get the longest word'''
    if not lst_words:
       err_description = "Empty list. Please, try again..."
    #    print("Empty list. Please, try again...")
       return err_description
    else:
       logest_word_in_list = max(lst_words, key=len)
       return logest_word_in_list


# print(get_maximum_length_word_list(["Написати", "функцію", "яка", "приймає", "список", "слів"]))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1: str, str2: str):
    """Get 1st index of second str"""
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
# print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
# print(find_substring(str1, str2)) # поверне -1

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
def separate_sawer_end_sentanse(snippet_sawer_story: str):
    '''Separate adwentures_of_tom_sawer via sentanse end'''
    adwentures_of_tom_sawer_sentences = snippet_sawer_story.split('\n')
    return adwentures_of_tom_sawer_sentences

# print(separate_sawer_end_sentanse(adwentures_of_tom_sawer))


##################################-Task 8-##########################################
#Homewor3 task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
def get_words_final_sentance(separate_sawer_end_sentanse):
    '''Виведе кількість слів останнього речення з adwentures_of_tom_sawer_sentences.'''
    temp = separate_sawer_end_sentanse(adwentures_of_tom_sawer)
    last_sentence = temp[-1]
    # print(type(last_sentence))
    words_in_last_sent = last_sentence.split()
    return  last_sentence,  len(words_in_last_sent)

''' Декомпозиція, за допомогою якої значення, повернені з функції get_words_final_sentance, присвоюються змінним last_sentence та word_count.'''
last_sentence, words_count = get_words_final_sentance(separate_sawer_end_sentanse)
# print(f"Last sentence is <{last_sentence}> and number of words in last sentence: {words_count}")


##################################-Task 9-##########################################
# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?

def calculate_photo_album_pages(number_of_photos: int, photos_per_page: int) -> int:
    '''calculate_photo_album_pages'''
    pages = number_of_photos // photos_per_page
    if number_of_photos % photos_per_page != 0:
        pages += 1
    return pages

number_of_photos = 232
photos_per_page = 8
# print(f"Igor needs {calculate_photo_album_pages(number_of_photos, photos_per_page)} pages to fit all his photos")


##################################-Task 10-##########################################
#homework 2 and task 10
# '''Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?


def calculace_fuel_and_station_stops(distanse: int, vehile_fuel_cousuming, tank_volume: int):
    '''calculace_fuel_and_station_stops'''
    trip_fuel_consuming = int(distanse / 100 * vehile_fuel_cousuming)
    quontity_petrol_refuel = int(trip_fuel_consuming / tank_volume)

    return trip_fuel_consuming, quontity_petrol_refuel


kharkov_budapesht_distance = 1600
fuel_consuming = 9
volume_fuel_tank = 48

fuel_cons, refuel = calculace_fuel_and_station_stops(kharkov_budapesht_distance, fuel_consuming, volume_fuel_tank)

# print(f"Trip fuel consumprion {fuel_cons} and refuel {refuel} liters")
#або інший варіант виводу
# print("Trip fuel consumprion", fuel_cons, "liters")
# print("Number of refueling stops:", refuel, "liters")
