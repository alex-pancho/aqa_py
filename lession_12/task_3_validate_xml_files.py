from pathlib import Path
import json
import csv
import xml.etree.ElementTree as ET
import logging
from my_logger import logger

# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""

def get_group_number_incoming(xml_path: str, number: int=0):
    '''
    Search in group/number and child values in timingExbytes/incoming
    '''

    if not my_xml.exists():
       raise FileNotFoundError("Файл не знайдено")

    with my_xml.open() as file:
        xml_data = file.read()
        root = ET.fromstring(xml_data)
    v = root.findall(f".//group[number='{number}']")
    for child in  v:
        try:
            value = child.find('timingExbytes/incoming')
            print(f"The chidl-values obj {value} is contains {value.text}")
            logger.info(f"The chidl-values obj {value} is contains {value.text}")
        except TypeError as g:
            print(f"Invalid type {g} error")
        
        except ValueError as t:
            print(f"Invalid value {t} error")
        
        except AttributeError as e:
            if type(value) == type(None):
                print(f"Getting error {e}")
        
        except IndexError as s:
            print(f"IndexError: {s}")
    
curr_folder_path = (Path.cwd())
my_xml = (curr_folder_path.parent / 'ideas_for_test' / 'work_with_xml' / 'groups.xml')

get_group_number_incoming(my_xml, 5)