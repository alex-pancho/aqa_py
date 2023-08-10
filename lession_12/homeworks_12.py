from pathlib import Path
import csv
import json
import logging
import xml.etree.ElementTree as ET


# task 1
""" Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""
dir_path = Path('C:/study/aqa_yturovska/aqa_py/ideas_for_test/work_with_csv')
file1_path = dir_path / 'r-m-c.csv'
file2_path = dir_path / 'random.csv'

# Читання даних з файлів
with file1_path.open("r") as file1, file2_path.open("r") as file2:
    file1_data = set(file1.readlines())
    file2_data = set(file2.readlines())

# Пошук дублікатів та запис результату до файлу
duplicates = file1_data.intersection(file2_data)
result_file_path = Path(f"results_turovska.csv")
with result_file_path.open("w", newline="") as result_file:
    writer = csv.writer(result_file)
    writer.writerow(["Duplicates"])
    for line in duplicates:
        writer.writerow([line.strip()])
print(f"The result is saved to file {result_file_path}")


# task 2
""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

folder_path = Path('C:/study/aqa_yturovska/aqa_py/ideas_for_test/work_with_json')
file_list = folder_path.glob("*.json")
# Отримання списку файлів папки
for file_path in file_list:
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            json.load(file)
            print(f"{file_path.name} is a valid JSON file.")
        except json.JSONDecodeError:
            logger.error(f"{file_path.name} is an invalid JSON file.")


# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""
def xml_search(group_number: int, timing: int) -> bool:
    logging.basicConfig(level=logging.INFO)
    tree = ET.parse("ideas_for_test/work_with_xml/groups.xml")
    for group in tree.findall("group"):
        if group_number == int(group.find("number").text):
            try:
                if timing == int(group.find("timingExbytes").find("incoming").text):
                    logging.info(f"Incoming timing {timing} in group {group_number} is found.")
                    return True
            except AttributeError:
                logging.info(f"Incoming timing {timing} in group {group_number} is NOT found.")
                return False
    logging.info(f"Incoming timing {timing} in group {group_number} is NOT found.")
    return False

