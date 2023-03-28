small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
set_small = set(small_list)
set_big = set(big_list)
unique_elements = set_small.symmetric_difference(set_big)
print("Unique elements between" f"{small_list}","and", f"{big_list}", "is", unique_elements)


# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
# f"sum_elemets = {sum(small_list)}, smal_list_lenght = {len(small_list)}"
sum_elemets , smal_list_lenght = sum(small_list) , len(small_list)
average_value = sum_elemets / smal_list_lenght
print("Small list avarage value is", average_value)

# task 3. Перевірте, чи є в списку big_list дублікати
if len(big_list) != set(big_list):
    print("Some dublicates is available")
else:
    print("Unique item(s) avaliable")


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
max_value = max(add_dict.values())
# print(max_value)
max_key = [key for key, dict_value in add_dict.items()
           if dict_value == max_value]
print("The keys with the maximum value is", max_key)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
my_dict= {"lesson_1":"intro", "lesson_2":"variables", "lesson_3":"slices"}
dict_items = my_dict.items()
versa_dict = {}
for key,value in dict_items:
    versa_dict[value] = key

print('My dict:', my_dict)
print('Versa versa dict:', versa_dict)


# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то об'єднайте (str) або додайте їх значення (int)
join_dict = dict(base_dict)
print(join_dict)
sum_dict = {}

for key, value in base_dict.items():
    if key in add_dict:
        if isinstance(value, str) and isinstance(add_dict[key], str):
            sum_dict[key] = value + add_dict[key]
        elif isinstance(value, int) and isinstance(add_dict[key], int):
            sum_dict[key] = value + add_dict[key]
        else:
            sum_dict[key] = value
    else:
        sum_dict[key] = value

for key, value in add_dict.items():
    if key not in sum_dict:
        sum_dict[key] = value

print(f"Base dictionary: {base_dict}\nAdd dictionary: {add_dict}\nSum dictionary: {sum_dict}")

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
new_set = set(line)
# print(type(new_set))
print(f"New set:{new_set}")

# task 8. Обчисліть суму елементів двох множин, які не є спільними
first_set = {1, 2, 3, 4, 5}
second_set = set([1, 2, 3, 4, 5, 6, 7])

differ_1 = first_set.difference(second_set)
differ_2 = second_set.difference(first_set)

sum_diff = sum(differ_1) + sum(differ_2)

print('Difference of sets is', sum_diff)


# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

final_set = set(person_list).union(set(small_list))
# print(type(final_set))
print('Set with unique elements', final_set)

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

result_ranges = {'19-22': [], '25-28': [], '32-45': []}

for x in person_list:
    name, age = x
    if age <= 19 and age <= 22:
        age_diapazon = '19-22'
    elif age <= 25 and age <= 28:
        age_diapazon = '25-28'
    elif age <= 32 and age <= 45:
        age_diapazon = '32-45'
    else:
        print("The value out of range person_list")

    result_ranges[age_diapazon].append(name)

print("Output for Task 10:", result_ranges)