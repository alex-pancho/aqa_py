# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
alien_color = 'green'
if alien_color== 'green':
    print('You got 5 points')

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
alien_color = 'red'
if alien_color== 'green':
    print('You got 5 points')
else:
    print('You got 10 points')

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
alien_color = ['green', 'yellow', 'red']
for i in alien_color:
    if i == 'green':
        print('Green? - You got 5 points')
    elif i== 'red':
        print('Red? - You got 15 points')
    else:
        print('No green? - You got 10 point')

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
pizza_toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping == 'quit':
        break
    else:
        print("Adding " + topping + " to your pizza!")
        pizza_toppings.append(topping)

print("Your pizza toppings are: ")
for topping in pizza_toppings:
    print("- " + topping)
    
# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Використовуйте цикл while. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
number = input("Enter a natural number: ")
sum = 0
i = 0
while i < len(number):
    sum += int(number[i])
    i += 1
print("Sum of digits of number: ", sum)

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Розв'язати з використанням циклу while та break
"""
sum = 0
while True: 
    number = int(input("Enter a natural number: "))
    if number == 0:
        break
    else:
        sum += number
print("Sum of entered numbers: ", sum)

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
for guesses in range(max_guesses):
    guess = int(input("Спроба №" + str(guesses + 1) + ": "))
    if guess < secret_number:
        print("Занадто мало!")
    elif guess > secret_number:
        print("Занадто багато!")
    else:
        break

if guess == secret_number:
    print("Вітаю! Ви вгадали число за " + str(guesses + 1) + " спроб!")
else:
    print("На жаль! Ви не вгадали число. Число було " + str(secret_number) + ".")

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""

fruits = ["apple", "banana", "orange", "grape", "mango"]
for i in fruits:
    if i == "orange":
        continue
    else:
        print(i)


# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i**2 for i in numbers if i%2==0]
print(result)  #  [4, 16, 36, 64, 100]
