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


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то об'єднайте (str) або додайте їх значення (int)
sum_dict = {}

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"

# task 8. Обчисліть суму елементів двох множин, які не є спільними

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
