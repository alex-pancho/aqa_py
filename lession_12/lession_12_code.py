from pathlib import Path
import json
import csv
import xml.etree.ElementTree as ET

# Бібліотека pathlib та її модуль Path

p = Path('c:\\')
print([x for x in p.iterdir() if x.is_dir()])
p = p / "tp_testing_code" / "hillel" / "aqapy" / "lession_12"
print([x for x in p.iterdir()])
# Methods - Перевірка існування файлів та папок, ітерування та інше
# print(p.parts)  # частини шляху
# print(p.parent) # hillel\aqapy
# print(p.parent.parent) # hillel
# print(Path(__file__).parent.parent)
# print(p.parents[0])
# print(p.parents[1])
# print(p.parents[2])
# print(p.parents[3])
# print(p.parents[-2])
p = p / "file.txt"
print(p)
print(p.suffixes)
print((p.parent).suffixes) ## УВАГА бере суфікси зі шляху!!!
print("stem:", p.stem) # Частина назви без розширення
print(p.name)
print(Path.cwd()) # current work dir
print(Path(__file__)) # curreent file path
print(p.home())  # user home
print(p.exists())
print(p.is_dir())
print(p.is_file())
print([x for x in p.parent.iterdir()])
print([x for x in p.parent.glob('*.py')])
# .mkdir(mode=0o777, parents=False, exist_ok=False)
#print((p.parent / "hillel" / "hw").mkdir(parents=True))
# Читання та запис у файл, режими роботи
# with p.open('r', encoding="utf-8") as file:
#     f = file.read()
# f = f.replace("сонечко", "віконечко")
# print(f)
# with p.open('w', encoding="utf-8") as file:
#     file.write(f)
#p.write_text("ok ok ", encoding="utf-8") #

# Модулі для роботи з окремими типами
# json
j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(j)
jjjsss = json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True, indent=4)
print(jjjsss)
js = p.parent / "try.json"
# with js.open('w', encoding="utf-8") as file:
#     file.write(jjjsss)
print(js)
with js.open() as file:
    alpha = file.read()
print(alpha)
#alpha = alpha + "}"
try:
    my_read_json = json.loads(alpha)
except json.decoder.JSONDecodeError:
    my_read_json = ""

print(my_read_json)
# csv
csv_file = p.parent.parent / "ideas_for_test" / "work_with_csv" / "random-michaels.csv"
print(csv_file)
with open(csv_file, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')#
    for row in spamreader:
        print(row)
# xml
my_xml = p.parent / "group.xml"
with my_xml.open() as file:
    xml_data = file.read()
root = ET.fromstring(xml_data)
number = 0
v = root.findall(f".//group[number='{number}']")
values = [ x.text for x in v ]
for child in  v:
    value = child.find('timingExbytes/micro')
    if value is None:
        raise ValueError("опис що чи чому значення нема")
    print(value.text)
