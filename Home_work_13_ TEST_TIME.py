import re
from pathlib import Path
import logging

# Задаємо шлях до файлу логу
filename = Path(__file__).parent / "hblog"

# Налаштовуємо логгер для запису в файл hb.log з рівнем WARNING і вище
logging.basicConfig(filename="hb.log", level=logging.WARNING)

try:
    # Відкриваємо файл для читання
    with open(filename, mode="r") as f:
        # Зчитуємо всі рядки файлу у список
        lines = f.readlines()
except FileNotFoundError:
    # Якщо файл не знайдено, логуємо помилку і піднімаємо виключення
    logging.error("File not found.")
    raise

# Проходимося по кожному рядку логу
for line in lines:
    # Використовуємо регулярний вираз для пошуку числа в рядку, що підходить для шаблону "Heartbeat (\d+)"
    match = re.search(r"Heartbeat (\d+)", line)
    if match:
        # Якщо відповідний шаблон знайдено, зберігаємо значення серцевої активності в змінну heartbeat
        heartbeat = int(match.group(1))
        # Проводимо аналіз значення серцевої активності
        if 30 < heartbeat < 32:
            # Якщо серцева активність знаходиться між 30 і 32, логуємо WARNING повідомлення
            logging.warning(f"Heartbeat is between 30 and 32: {heartbeat}")
        elif heartbeat >= 32:
            # Якщо серцева активність дорівнює або більша за 32, логуємо ERROR повідомлення
            logging.error(f"Heartbeat is equal or greater than 32: {heartbeat}")
