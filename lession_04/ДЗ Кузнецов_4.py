# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]

print("# task 1", set(small_list))

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
x = sum(small_list)
y = len(small_list)
def list22(x, y):
return x/y
print("# task 2 ", f)

# task 3. Перевірте, чи є в списку big_list дублікати
nlist = []
for item in big_list:
    if item not in nlist:
        nlist.append(item)
print("# task 3 ", nlist)

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

key_val = add_dict.items()
print("# task 4.", max(key_val))


# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

new_dict = {}
for k, v in base_dict.items():
    new_dict[v] = k
print("# task 5 ", new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то об'єднайте (str) або додайте їх значення (int)

basee_dict = {}
sum_dict = base_dict.copy()
for key, value in add_dict.items():
    if key in sum_dict:
        if isinstance(sum_dict[key], int):
            sum_dict[key] += value
        elif isinstance(sum_dict[key], str):
            sum_dict[key] += ", "
    else:
        sum_dict[key] = value
print("# task 6.", sum_dict)


# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
from collections import Counter
c = Counter(line)
print("# task 7.", c)



# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum1 = set_1 ^ set_2
print("# task 8.", sum(sum1))




# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

x1 = [1, 2, 3, 4]
y2 = [3, 4, 5, 6]

list1 = set(x1)
list2 = set(y2)
list3 = list1 ^ list2
print("# task 9.", list3)


# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),('David', 28), ('Emma', 22), ('Frank', 45)]
result = {'10-19': [], '20-29': [], '30-39': [], '40-49': []}
for name, age in person_list:
    if age < 20:
        result['10-19'].append(name)
    elif age < 30:
        result['20-29'].append(name)
    elif age < 40:
        result['30-39'].append(name)
    else:
        result['40-49'].append(name)
print("# task 10. Список персонала согласно возраста:", result)







