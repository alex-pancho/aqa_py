from pathlib import Path
import json
import csv
import xml.etree.ElementTree as ET
from my_logger import logger

""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""

curr_folder_path = (Path.cwd())
path_work_json_dir = (curr_folder_path.parent / 'ideas_for_test' / 'work_with_json')

def validate_json_files_in_dir(path):
    '''
    Syntax validation json files in directory
    '''
    folder = path
    for file in folder.glob("*.json"):
        with open(file, "r") as f:
            try:
                json.load(f)
            except json.JSONDecodeError as error:
                logger.error(f"The file {file} from dir{folder} contains invalid JSON syntax: {error}")


validate_json_files_in_dir(path_work_json_dir)