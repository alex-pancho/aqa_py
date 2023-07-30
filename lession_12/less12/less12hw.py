from pathlib import Path
from my_logger import logger
import json
import csv
import xml.etree.ElementTree as ET


p = Path("d:\\")
p = p / "QA python" / "less12" / "ideas_for_test"


json_task = p / "work_with_json"
for jsons in json_task.glob("*.json"):
    with open(jsons, encoding="utf-8") as file:
        try:
            json.load(file)
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON recieved: {jsons}")



csv_task = p / "work_with_csv"

csv1 = csv_task / "random.csv"
with open(csv1, "r", newline="\n") as file_csv1:
    csv_list1 = list(csv.reader(file_csv1, delimiter=","))
#print(csv_list1)

csv2 = csv_task / "r-m-c.csv"
with open(csv1, "r", newline="\n") as file_csv2:
    csv_list2 = list(csv.reader(file_csv2, delimiter=","))
#print(csv_list2)

csv_set1 = set(map(tuple, csv_list1))
csv_set2 = set(map(tuple, csv_list2))

duplicates = csv_set1.intersection(csv_set2)
#print(duplicates)

my_result = p.parent / "result_starun.csv"
with open(my_result, "w") as res_file:
    writer = csv.writer(res_file)
    writer.writerows(duplicates)



xml_task = p / "work_with_xml"
my_xml = xml_task / "groups.xml"

with my_xml.open() as file:
    xml_data = file.read()
root = ET.fromstring(xml_data)

def find_micro_by_number(number):
    v = root.findall(f".//group[number='{number}']")
    #values = [x.text for x in v]
    for child in v:
        value = child.find("timingExbytes/micro")
        return(value.text)

logger.info(f"timingExbytes/micro for group/number is {find_micro_by_number(0)}")
    