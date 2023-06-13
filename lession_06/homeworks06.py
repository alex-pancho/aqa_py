# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 25:
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
def sum1(a,b):
    return a+b
print(sum1(5, 8))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_average(number):
    suma = sum(number)
    average = suma/len(number)
    return average
number = [2,4,6,8]
result = arithmetic_average(number)
print('середнє арифметичне: ', result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_order(ryadok):
    reverse_ryadok = ryadok[::-1]
    return reverse_ryadok
ryadok = "Ой у лузі червона калина"
result = reverse_order(ryadok)
print("Зворотній рядок виглядає так:", result)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def the_longest_word(word_list):
    longest = ""  
    for word in word_list:  
        if len(word) > len(longest):  
            longest = word  
    return longest  
word_list = ["яблуко", "груша", "апельсин", "банан", "виноград"]  
result = the_longest_word(word_list)  
print("Найдовше слово:", result)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    result = str1.find(str2)
    return result

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
"""Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?"""
def seas_square(black_sea, azov_sea): # створюємо функцію seas_square 
    return black_sea + azov_sea       # вказуємо що будемо повертати
black_sea = 436_402                   # задаємо перше значення
azov_sea = 37_800                     # задаємо друге значення
print(f"Загальна площа українських морів складає :", seas_square(black_sea, azov_sea)) #виводимо
# task 8
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
def spusok_pokupok(*args):           # створюємо функцію , при цьому уявімо що ми не знаємо скільки і чого потрібно Ірині
    vsya_summa = sum(args)           # вказуєму що рахуємо суму елементів
    return(vsya_summa)               # виводимо  всю суму
print("Загальна вартість покупок складає: ", spusok_pokupok((274*4),(218*2),(35*4),350,(21*3))) #виводимо результат нашої функції
# task 9
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
def podorozh(distance, benz_na_sto, bak, sto=100): 
    """створюємо функцію podorozh , sto - опційно задане значення"""
    benz = (distance/sto)*benz_na_sto # рахуємо кількість бензину для подорожі
    zapravka = benz/bak # рахуємо скільки разів потрібно заправитись
    return f"Нам потрібно {benz} літрів бензину, потрібно завправитись {zapravka} рази" #функція повертатиме таку f-string
print(podorozh(1600,9, 48)) # виводимо функцію зі значеннями із задачі

# task 10
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
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
def kilkist_h():                # створюємо функцію
    kilkist = adwentures_of_tom_sawer.count('h')   # пишемо що саме вона буде робити 
    return f"В нашому тексті буква h зустрічається {kilkist} разів"    # прописуємо що саме вона буде повертати
print(kilkist_h())              # друкуємо



