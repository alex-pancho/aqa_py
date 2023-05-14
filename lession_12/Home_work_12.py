import xml.etree.ElementTree as ET
import logging
import json
from pathlib import Path
import csv
import pathlib
xml_path = "ideas_for_test/work_with_xml/groups.xml"
if not pathlib.Path(xml_path).exists():
    print(f"FILE {xml_path} FILE DOES NOT EXIST")


p = Path("c:\\")
folder_path = Path("aqa_py", "lession_12", "ideas_for_test", "work_with_csv")
result_file = f"result_Ihor_M.csv".replace("<", "_").replace(">", "")

file_paths = [f for f in folder_path.glob("*.csv")]
header = ["File 1", "File 2", "Duplicate Lines"]
rows = []

# настройка логгера
logging.basicConfig(level=logging.INFO)

# task 1
""" Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""

for i in range(len(file_paths)):
    for j in range(i + 1, len(file_paths)):
        file1 = file_paths[i]
        file2 = file_paths[j]

        with open(file1) as f1, open(file2) as f2:
            lines1 = set(f1.readlines())
            lines2 = set(f2.readlines())
            duplicates = sorted(list(lines1.intersection(lines2)))
            if duplicates:
                rows.append([file1.name, file2.name, "\n".join(duplicates)])

with open(result_file, "w", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(rows)


# task 2
""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""

folder_path = Path("ideas_for_test/work_with_json")

for file_path in folder_path.glob("*.json"):
    with open(file_path) as f:
        try:
            json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON format in {file_path.name}: {str(e)}")


# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""

xml_path = Path("ideas_for_test/work_with_xml/groups.xml")


def find_timingExbytes(xml_path, group_number):
    with open(xml_path) as f:
        root = ET.fromstring(f.read())

    xpath = f".//group[number='{group_number}']"
    group = root.find(xpath)
    if group is None:
        logging.info(f"No group with number {group_number}")
        return None
    timingExbytes = group.find("timingExbytes")
    if timingExbytes is None:
        logging.info(f"No timingExbytes element for group {group_number}")
        return None
    incoming = timingExbytes.find("incoming")
    if incoming is None:
        logging.info(f"No incoming element for group {group_number}")
        return None
    return incoming.text


group_number = 5
result = find_timingExbytes(xml_path, group_number)
if result is not None:
    logging.info(
        f"Value of timingExbytes/incoming for group {group_number}: {result}")
