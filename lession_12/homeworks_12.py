# from pathlib import Path
# import json
# import csv
# import xml.etree.ElementTree as ET
# p = Path('c:\\')
# print([x for x in p.iterdir() if x.is_dir()])
# print([x for x in p.iterdir()])
# print(p.parts)
# print(p.parent.parent)
#
# # d = Path('d:\\')
# # print([x for x in d.iterdir() if x.is_dir()])
# # print([x for x in d.iterdir()])
# # print(d.parts)
# # print(d.parent.parent)
#
#
#
#
# # task 1
# """ Візміть два файли з теки
# ideas_for_test/work_with_csv
# порівняйте на наявність дублікатів
# результат запишіть у файл result_<your_second_name>.csv
# """
# c = Path('c:\\')
# c = c.parent
#
# path_aqa_py = c / "Users" / "Alex" /"PycharmProjects" /"aqa_py"
# path_ideas_f_test = c / "Users" / "Alex" /"PycharmProjects" /"aqa_py" / "ideas_for_test" / "work_with_csv"
#
#
# def read_csv_file(filename):
#     """Зчитування даних з CSV-файлу."""
#     data = []
#     with open(filename, newline='\n', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',')
#         for row in reader:
#             data.append(row)
#             print(data)
#             # print(type(data))
#         # for row in reader:
#         #     print(', '.join(row))
#
#     return data
#
# def write_csv_file(filename, data):
#     """Функція для запису даних до CSV-файлу."""
#     with open(filename, 'w', newline='\n', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         for row in data:
#             writer.writerow(row)
#
# def check_duplicates():
#     """Перевірка наявності дублікатів."""
# path_to_r_m_c_file = c / "Users" / "alex" /"PycharmProjects" /"aqa_py" / "ideas_for_test" / "work_with_csv" / "r-m-c.csv"
# path_to_random_michaels_file = c / "Users" / "alex" /"PycharmProjects" /"aqa_py" / "ideas_for_test" / "work_with_csv" / "random-michaels.csv"
# rmc_list = read_csv_file(path_to_r_m_c_file)
# random_mich_list = read_csv_file(path_to_random_michaels_file)
#
# rmc_tuples = [tuple(sublist) for sublist in rmc_list]
# rmc_set = set(rmc_tuples)
# random_mich_tuple = [tuple(sublist_1) for sublist_1 in random_mich_list]
# random_mich_set = set(random_mich_tuple)
# duplicates = rmc_set.intersection(random_mich_set)
# write_csv_file('result_kobko.csv', list(duplicates))
#
# check_duplicates()