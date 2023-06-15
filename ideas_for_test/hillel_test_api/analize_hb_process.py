from pathlib import Path
import re
from my_logger import logger
from datetime import datetime


def analyze_hblog_data():
    '''Main func for analizing data from hblog file'''
    hblog_file = Path(__file__).parent.parent / "heartbeat" / "hblog"  # Шлях до файлу hblog

    # Зчитування даних з файлу hblog
    with open(hblog_file, "r") as file:
        hblog_data = file.readlines()

    # Знайти унікальні ідентифікатори
    keys = find_unique_keys(hblog_data)

    # Аналіз та обробка даних для кожного ідентифікатора
    for key in keys:
        filtered_data = [line for line in hblog_data if key in line]

        if not filtered_data:
            continue  # skipp if no id

        # Сортування даних за ідентифікатором
        sorted_data = sorted(filtered_data, key=lambda line: extract_timestamp(line))

        # Аналіз різниці в часі між послідовними рядками
        for i in range(len(sorted_data) - 1):
            line1 = sorted_data[i]
            line2 = sorted_data[i + 1]

            timestamp1 = extract_timestamp(line1)
            timestamp2 = extract_timestamp(line2)

            time_difference = timestamp2 - timestamp1

            if 30 < time_difference < 32:
                # log_warning(key, timestamp1, time_difference) # фукція яка записує warnings в кастомний файл
                logger.warning(f"Key: <{key}>,Timestamp: {timestamp1}, Difference(in sec): {time_difference}")
            elif time_difference >= 32:
                # log_error(key, timestamp1, time_difference) #запис errors в кастомний файл
                logger.error(f"Key: <{key}>,Timestamp: {timestamp1}, Difference(in sec): {time_difference}")


def find_unique_keys(hblog_data):
    '''Find unique keys in hblog_data(reading from file hblog)'''
    keys = set()
    pattern = r"Key (\S+)"

    for line in hblog_data:
        match = re.search(pattern, line)
        if match:
            key = match.group(1)
            keys.add(key)

    return list(keys)


def extract_timestamp(line):
    '''Getting Timestamp '''
    pattern = r"Timestamp (\d+:\d+:\d+)"
    match = re.search(pattern, line)
    if match:
        timestamp_str = match.group(1)
        # Парсинг рядка Timestamp у форматі HH:MM:SS
        hours, minutes, seconds = map(int, timestamp_str.split(":"))
        # Повернення значення Timestamp у секундах
        return hours * 3600 + minutes * 60 + seconds

    return 0  # Значення за замовчуванням

# def log_warning(key, timestamp, time_difference):
#     # Запис в журнал (warning)
#     print(f"Warning: Key: '{key}', Timestamp {timestamp}, Difference: {time_difference} seconds")
#
# def log_error(key, timestamp, time_difference):
#     # Запис в журнал (error)
#     print(f"Error: Key '{key}', Timestamp {timestamp}, Difference: {time_difference} seconds")

if __name__ == '__main__':
    print(analyze_hblog_data())