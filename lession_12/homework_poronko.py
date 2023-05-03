from pathlib import Path
import csv
import json
from my_logger import logger
import xml.etree.ElementTree as ET

# task 1
""" Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""

p = Path(__file__)
first_csv = p.parent.parent / 'ideas_for_test' / 'work_with_csv' / 'r-m-c.csv'
second_csv = p.parent.parent / 'ideas_for_test' / 'work_with_csv' / 'rmc.csv'

with open(first_csv) as first:
    redacted_first = [x.split(',') for x in first.readlines()]
    print(redacted_first)

with open(second_csv) as second:
    redacted_second = [x.split(';') for x in second.readlines()]
    print(redacted_second)

result_poronko = []
for x in redacted_first:
    if x in redacted_second:
        result_poronko.append(x)

with open('result_poronko.csv', 'w') as general_result:
    general_result.writelines(str(result_poronko))
    print(result_poronko)

# task 2
""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""

json_folder = p.parent.parent / 'ideas_for_test' / 'work_with_json'
json_files = json_folder.glob('*.json')

for file in json_files:
    with open(file, encoding="utf-8") as json_file:
        try:
            json.load(json_file)
            print(f'{file.name} is valid json')
        except json.JSONDecodeError:
            print(f"{file.name} isn't JOSN file")
            logger.error(f'{file.name} is JSON format')

# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""
xml_doc = p.parent.parent / 'ideas_for_test' / 'work_with_xml' / 'groups.xml'
print(xml_doc)
def search_by_group_number(number):
    with xml_doc.open() as file:
        xml_data = file.read()
        first_root = ET.fromstring(xml_data)
        second_root = first_root.findall(f".//group[number='{number}']")
        print(xml_data)
        print(first_root)
        print(second_root)
    for value in second_root:
        exbytes = value.find('timingExbytes/incoming')
        if exbytes is None:
            raise ValueError('timingExbytes/incoming data is absent in massive')
        logger.info(f'{exbytes.text}')
search_by_group_number(4)
