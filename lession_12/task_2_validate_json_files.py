from pathlib import Path
import json
import csv
import xml.etree.ElementTree as ET
from logger_error_level import logger

""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""

c = Path('c:\\')
c = c.parent
path_work_json_dir = c / "Users" / "Alex" /"PycharmProjects" /"aqa_py" / "ideas_for_test" / "work_with_json"

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