# Списки
## створення списків - пустий і зі значеннями
blank_list = []
big_list = [7, 336, 61, "--==--", 'spam', 'dev', 1.23]
# індексація, зрізи

## порівняння списків
a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3, 4]
a < c
## вилучення значень
big_list.pop()
## методи списків
# додавання у список
big_list.append(4)
big_list.extend([5,6,7])
big_list.insert(1, "223")
# пошук, перевірка значень
value = 61
big_list.index(value)
big_list.count(value)
# впорядкування даних
big_list.sort()  #['abc', 'ABD', 'aBe']
big_list.reverse()
# зміни
big_list.copy()
big_list.clear()

# comprehensions and List Iteration
small_list = [x**2 for x in range(5)]


# Словники
## створення словників
blank_dict =  {}
small_dict = {'name':'Mary', 'second': 'Ann', 'age': 18}
big_dict= {'user': {'name':'Bob', 'second': 'Hand', 'age': 40},
           'is_blocked': False,
           'salary': 10000}

## додавання значень в словник
## методи словника
big_dict.keys()
big_dict.values()
big_dict.items()
big_dict.copy()
big_dict.clear()
big_dict.update({"key":"value"})
big_dict.get("key", "default")
big_dict.pop("key", "default")  #.popitem() -  видалення випадкового елемента

# порівняння словників Dictionary Comparisons
# Example: Word Counts
text = ('this is sample text with several words '
        'this is more sample text with some different words')
# без колекцій
# з колекціями
# from collections import Counter

# Zipped key/value tuples form (ahead)
zipped = dict(zip(['a', 'b', 'c'], [1, 2, 3]))

# Сети (набори)
my_blank_set = set()
## перетворення в набір
numbers = list(range(4)) + list(range(5, 10))
set(numbers)

## операції з наборами
# порівняння
# підмножина. Еквівалентом методу issubset() є оператор <=
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(set_a <= set_b)
# обєднання  with the '|' operator or with the set type’s 'union' method
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b
# перетин 'intersection' and with the '&' operator
set_a = {1, 2, 3}
set_b = {3, 4, 5}
intersection_set = set_a & set_b  # {3}
# симетрична різниця
set_a = {1, 2, 3}
set_b = {3, 4, 5}
symmetric_difference_set = set_a ^ set_b  # {1, 2, 4, 5}


# кортежі Tuples
student_tuple = ()

# Елементи Tuple можуть бути будь-якого типу, включаючи числа, рядки, списки та інші Tuple. Наприклад:
my_tuple = ("apple", 3.14, [1, 2, 3], (4, 5, 6))

# Для доступу до елементів Tuple можна використовувати індексацію, яка починається з 0. Наприклад:
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])  # "banana"

# Інші корисні операції з Tuple:
# Отримання довжини Tuple:
my_tuple = (1, 2, 3)
print(len(my_tuple))  # 3

# Злиття двох Tuple:
tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana", "cherry")
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, "apple", "banana", "cherry")

# Перевірка наявності елемента в Tuple:
my_tuple = (1, 2, 3)
print(1 in my_tuple)  # True
print(4 in my_tuple)  # False

# Повторення Tuple:
my_tuple = ("apple", "banana", "cherry")
print(my_tuple * 2)  # ("apple", "banana", "cherry", "apple", ...