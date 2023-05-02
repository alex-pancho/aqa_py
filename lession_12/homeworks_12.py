import csv
from pathlib import Path
import json
import xml.etree.ElementTree as ET
from lession_12_logger import logger

# task 1
""" Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""

p = Path(__file__)
csv_folder = p.parent.parent / "ideas_for_test" / "work_with_csv"
f1 = csv_folder / "rmc.csv"
f2 = csv_folder / "random.csv"


with open(f1, newline='\n') as f:
        reader = csv.reader(f, delimiter=',')
        f1_list = (list(reader))
        f1_tuple = (tuple(info) for info in f1_list)
        f1_set = set(f1_tuple)

with open(f2, newline='\n') as f:
        reader = csv.reader(f, delimiter=',')
        f2_list = (list(reader))
        f2_tuple = (tuple(info) for info in f2_list)
        f2_set = set(f2_tuple)

common = f1_set.intersection(f2_set)

with open('result_oliinyk.csv', 'w') as response_file:
        writer = csv.writer(response_file)
        for row in common:
                writer.writerow(row)
        

# task 2
""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""
json_folder = p.parent.parent / "ideas_for_test" / "work_with_json"

pathlist = json_folder.glob('*.json')
for file in pathlist:
    with open(file, encoding="utf-8") as json_file:
        try:
            json.load(json_file)
            print(f'{file.name} is valid json')
        except json.JSONDecodeError:
            logger.error(f'{file.name} is invalid file format')

                
# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""

xml_file = p.parent.parent / "ideas_for_test" / "work_with_xml"/ "groups.xml"

with xml_file.open() as file:
    xml_data = file.read()
root = ET.fromstring(xml_data)
for number in range(6):
    numbers = root.findall(f".//group[number='{number}']")
    if not numbers:
        raise ValueError(f'Value <number> {number} </number> does not exist in file')
    else:
        for child in numbers:
            value = child.find('timingExbytes/incoming')
            if value is None:
                raise ValueError(f'Value <number> {number} </number> / timingExbytes/ incoming does not exist in file')
            else:
                logger.info(f'Value <number> {number} </number> / timingExbytes/ incoming: {value.text}')
                print(value.text)


# with xml_file.open() as file:
#     xml_data = file.read()
# root = ET.fromstring(xml_data)
# for number in range(6):
#     if number == 3:
#          continue
#     values = root.findall(f".//group[number='{number}']")
#     if not values:
#         raise ValueError(f'Value <number> {number} does not exist in file')  
#     else:
#         for child in values:
#             value = child.find('timingExbytes/incoming')
#             if value is None:
#                 continue
#             else:
#                 logger.info(f'Value <number> {number} / timingExbytes/ incoming: {value.text}')
#                 print(value.text)






