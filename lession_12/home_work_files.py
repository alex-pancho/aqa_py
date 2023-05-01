from pathlib import Path
from my_logger import logger
import json
import xml.etree.ElementTree as ET


# task 1
""" Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""

path = Path(__file__)
print(path)
csv_1 = path.parent.parent / 'ideas_for_test' / 'work_with_csv' / 'r-m-c.csv'
csv_2 = path.parent.parent / 'ideas_for_test' / 'work_with_csv' / 'rmc.csv'

# У цих файлах дублікати усі рядки окрім одного. Взагалі, я подумав, що тут можно обійтись без модуля csv aлe давайте
# до суті. Після вирішення я заради інтересу вирішив подивитися, як вирішували одногрупники, там вирішується ця задача
# через set і мені теж у голову таке рішення приходило спочатку, але якщо запустити такий код, то відповідь буде
# неправильна, а саме лише перший рядок буде вважатися дублікатом. Але дублікати усі рядки окрім 3-го, можете
# подивитись навіть самі вручну, чи в моєму рішенні перед останнім in у result дописати not щоб подивитись не дублікати,
# буде саме цей рядок з файлу r-m-c.csv тоді коли в rmc.csv другий і третій однакові.
# Якщо це я неправильно зрозумів завдання і провів безтолкове "розслідування", тоді прошу вибачення)


def csv_duplicates(file_1, file_2):
    """Find duplicates in 2 csv files with different delimiters and write it to result file
    First file delimiter is ",", second file delimiter is ";" """
    try:
        with open(file_1) as csv_file_1, open(file_2) as csv_file_2:

            content_csv_1 = [line.strip().split(',') for line in csv_file_1.readlines()]
            content_csv_2 = [line.strip().split(';') for line in csv_file_2.readlines()]

        with open('result_dudnik_denys.csv', 'w') as result:
            result.writelines(','.join(line) + '\n' for line in content_csv_1 if line in content_csv_2)

    except FileNotFoundError:
        logger.error('csv file is not exist')


csv_duplicates(csv_1, csv_2)

# task 2
""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""

json_folder = path.parent.parent / 'ideas_for_test' / 'work_with_json'


def json_validator(folder):
    """Validate files in directory to json format"""

    for file in folder.glob('*.json'):
        with open(file) as json_file:
            try:
                json.load(json_file)
            except json.JSONDecodeError:
                logger.error(f'File {file} is not JSON format')


json_validator(json_folder)


# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""

xml_file = path.parent.parent / 'ideas_for_test' / 'work_with_xml' / 'groups.xml'

# Дякую за пояснення, одразу ж виправив :)


def xml_search_incoming_by_group_number(num):
    """Find in xml file parameter timingExbytes/incoming by group/number"""

    with open(xml_file) as xml_data:
        xml_tree = ET.fromstring(xml_data.read()).findall(f".//group[number='{num}']")

    if not xml_tree:
        raise ValueError(f'{num} not in xml file')

    for child in xml_tree:
        value = child.find('timingExbytes/incoming')
        if value is None:
            raise ValueError(f"{num} num in timingExbytes/incoming data is empty")
        logger.info(f'{value.text}')


xml_search_incoming_by_group_number(4)
