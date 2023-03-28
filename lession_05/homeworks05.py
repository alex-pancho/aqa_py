# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
alien_color = ['red','green', 'yellow']
 # for x in alien_color:
 #    if x == 'green':
 #        print("Congrats! You already earned 5 points")
 #        break
 #    else:
 #        print("Try again!")

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
fife, ten, fifteen = 5, 10, 15
# for x in alien_color:
#     if x == 'green':
#         print(f"Congrats! You already earned {fife} points")
#         continue
#     else:
#         print(f"Congrats! You already earned {ten} points")
# не розумію умову, зробив таску 2 як зрозумів + задав запитання Олександру

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
# for x in alien_color:
#     if x == 'green':
#         print(f"Congrats! You already earned {fife} points")
#     elif x == 'red':
#         print(f"Congrats! You already earned {fifteen} points")
#     else:
#         print(f"Congrats! You already earned {ten} points")


# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
# pizza_topping = []
# add_ingredient_prompt = 'Print ingridient for your best pizza ever'
# exit_prompt = 'pring <quit> to finish order: '
#
# while True:
#     ingredient = str(input(f"{add_ingredient_prompt} or {exit_prompt}"))
#     if ingredient != 'quit':
#         print(f"Following ingridient < {ingredient} > will be added to your pizza")
#         pizza_topping.append(ingredient)
#     else:
#         print("Excellent, we'll cook your pizza with requested ingredients", pizza_topping)
#         break


# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Використовуйте цикл while. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
num = int(input("Input rignt digit: "))
digit_summ = 0

while num > 0:
    last_digit = num % 10
    digit_summ = digit_summ + last_digit
    num //= 10

print("Digits summ is: ", digit_summ)


# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Розв'язати з використанням циклу while та break
"""


# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ["Відповідь вставте сюди"]
print(result)  #  [4, 16, 36, 64, 100]