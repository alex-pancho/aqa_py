small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print(set(small_list))

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
s_a = sum(small_list)/len(small_list)
print('середне арифметичне списку small_list: ', s_a)

# task 3. Перевірте, чи є в списку big_list дублікати
big_list_set = set(big_list)
print(len(big_list_set)==len(big_list)) # відповідь false, розміри не співпадають, дублікати є


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
max_value = max(add_dict.values())
max_dict = {k:v for k, v in add_dict.items() if v==max_value}
print (max_dict)

# або 
max_value = max(add_dict.values())
for k, v in add_dict.items(): 
    if v==max_value:
        print(k,v)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
new_dict = {v:k for k, v in add_dict.items()}
print(new_dict)    

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то об'єднайте (str) або додайте їх значення (int)
sum_dict = {}
for key in base_dict:
    if key in add_dict:
        if type(base_dict[key]) == str:
            sum_dict[key] = base_dict[key] + " " + add_dict[key]
        elif type(base_dict[key]) == int:
            sum_dict[key] = base_dict[key] + add_dict[key]
    else:
        sum_dict[key] = base_dict[key]

for key in add_dict:
    if key not in base_dict:
        sum_dict[key] = add_dict[key]

print(sum_dict)
# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
set_line = set(line)
print(set_line)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sim_set = set_1^set_2
print(sum(sim_set))

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [2, 4, 6, 8, 10, 12]
set_1 = set(list_1)
set_2 = set(list_2)
sim_set = set_1^set_2
print(sim_set)

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
age_ranges = {'10-19': [], '20-29': [], '30-39': [], '40-49': []}
for name, age in person_list:
    if age >= 10 and age <= 19:
        age_ranges['10-19'].append(name)
    elif age >= 20 and age <= 29:
        age_ranges['20-29'].append(name)
    elif age >= 30 and age <= 39:
        age_ranges['30-39'].append(name)
    elif age >= 40 and age <= 49:
        age_ranges['40-49'].append(name)

print(age_ranges)