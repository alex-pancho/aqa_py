# task 1
""" Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""

from pathlib import Path
import csv
import json
import xml.etree.ElementTree as ET
from lession_10 import hw_10_logger as l
import threading

p = Path(__file__)
csv_file1 = p.parent.parent / "ideas_for_test" / "work_with_csv" / "r-m-c.csv"
csv_file2 = p.parent.parent / "ideas_for_test" / "work_with_csv" / "rmc.csv"
with open(csv_file1, newline='\n') as csvfile1:
    spam_reader = csv.reader(csvfile1, delimiter=',', quotechar='"')
    csv_set1 = set(tuple(row) for row in spam_reader)
with open(csv_file2, newline='\n') as csvfile2:
    spam_reader2 = csv.reader(csvfile2, delimiter=';', quotechar='"')
    csv_set2 = set(tuple(row) for row in spam_reader2)
inter_section_csv = csv_set1.intersection(csv_set2)
with open("result_lahernyi.csv", "w", newline='') as result_file:
    writer = csv.writer(result_file)
    writer.writerows(inter_section_csv)


# task 2
""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""
json_folder_path = p.parent.parent / "ideas_for_test" / "work_with_json"
localizations_en = json_folder_path / "localizations_en.json"
localizations_ru = json_folder_path / "localizations_ru.json"
login = json_folder_path / "login.json"
swagger = json_folder_path / "swagger.json"

def json_validator(file_path) -> dict:
    """Отримує шлях до файла та повертає файл dict, перетворений з json.
      Якщо json не корректний то виникає помилка """
    with file_path.open() as file:
        action = file.read()
    try:
        json_file = json.loads(action)
        print(file_path.name, "OK")
        return json_file
    except json.decoder.JSONDecodeError:
        print(file_path.name, "BROKEN")
        l.logger.error(f'Incorrect arg {file_path.name} received')
json_files = [localizations_en, localizations_ru, login, swagger]
for files in json_files:
    thread = threading.Thread(target=json_validator, args=(files,))
    thread.start()



# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""

def incoming_find(number: int) -> str:
    """
    Отримує число arg, потім шукає "вхідні" значення у файлі xml, а потім повертає значення str
     У випадку, якщо номер не знайдено або значення «вхідного» порожнього значення ValueError зростає
    """
    xml_path = p.parent.parent / "ideas_for_test" / "work_with_xml" / "groups.xml"
    with xml_path.open() as xml_file:
        xml_data = xml_file.read()
    root = ET.fromstring(xml_data)

    values = root.findall(f".//group[number='{number}']")
    if not values:
        raise ValueError(f'"incoming" value {number} doesn\'t exist in file')  # Check number arg exists
    else:
        for child in values:
            value = child.find('timingExbytes/incoming')
            if value is None:
                raise ValueError(f'"incoming" value in group number {number} doesn\'t exist')
            else:
                l.logger.info(f'Search result is: {value.text}')
                return value.text


incoming_find(4)


