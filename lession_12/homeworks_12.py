import json
from pathlib import Path
import csv
from my_logger import logger
import xml.etree.ElementTree as ET

# task 1
""" Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""

p=Path (__file__).parent.parent
csv_file1=p / 'ideas_for_test' / 'work_with_csv' / 'rmc.csv'
csv_file2=p / 'ideas_for_test' / 'work_with_csv' / 'r-m-c.csv'
duplicates=[]

with open (csv_file1) as csvfile:
    reader1=csv.reader (csvfile)
    csv_file1_data=[]
    for row in reader1:
        cleaned_row=[]
        for elem in row:
            cleaned_elem=elem.strip ().split (',')
            cleaned_row.append (cleaned_elem)
        csv_file1_data.append (cleaned_row)

with open (csv_file2) as csvfile:
    reader2=csv.reader (csvfile)
    csv_file2_data=[]
    for row in reader2:
        cleaned_row2=[]
        for elem in row:
            cleaned_elem2=elem.strip ().split (',')
            cleaned_row2.append (cleaned_elem2)
        csv_file2_data.append (cleaned_row2)
    for row in csv_file1_data:
        if row in csv_file2_data:
            duplicates.append (row)

result_file=open ('result.csv', 'w', newline='')
csv_writer=csv.writer (result_file)

for row in duplicates:
    csv_writer.writerow (row)

result_file.close ()

"""
# task 2
 Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні ерро

"""

json_files=p / 'ideas_for_test' / 'work_with_json'

for file in json_files.glob ('*.json'):
    with open (file, encoding='utf-8') as json_file:
        try:
            json.load (json_file)
            print (f'{file} is valid json')
        except json.decoder.JSONDecodeError:
            logger.error (f'{file} is invalid json')

# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""

xml_files=p / 'ideas_for_test' / 'work_with_xml' / 'groups.xml'

with xml_files.open () as file:
    xml_data=file.read ()
    root=ET.fromstring (xml_data)
    v=root.findall (f".//group[number]")
    values=[x.text for x in v]
    if not v:
        raise ValueError (f'Value <number> {v} </number> does not exist in file')
    else:
        for child in v:
            value=child.find (f"timingExbytes/incoming")
            if value is None:
                logger.error (f'Value <timingExbytes/incoming> {value} does not exist in file')
            else:
                logger.info (f'Value <timingExbytes/incoming> {value}')
