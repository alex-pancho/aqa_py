from pathlib import Path
import datetime
from lession_10 import my_logger

filename = Path(__file__).parent / "hblog"

# Давайте порахуємо кількість варнінгів та критичних помилок
warning_count, critical_count = 0, 0

with open(filename, mode="r") as f:

    # Прочитаємо дані з файлу, нам треба лише таймстемп але ми візьмемо і ключ. Кожен новий удар закінчується на
    # 0300 і починається з 0003, тому щоб зменшити об`єм файлу, та не зберігати повністю все - ми будемо брати тільки
    # новий удар, тобто той рядок у якого ключ починається з 0003, це скоротить об`єм який будемо зберігати у 11 разів,
    # адже новий удар наступає кожен 11-ий рядок. До того ж щоб було зручно було рахувати час ми перевернемо наш список.
    # P.S. Так, можна було б для цього перетворення використати і модуль csv, але мені здається, що нащо коли можна
    # обійтись без нього. До того з-за наявності оцієї частини у файлі (101, len 36) не можна її винести як
    # окремий стовбець цілою. Ще можна було б потім конвертувати в словник і шукати за ключем 'Timestamp' але це ще
    # одне перетворення і ще один цикл, а так я ми знаходимо 'Timestamp' у файлі і сплітуємо рядок, то знаємо, що час
    # буде завжди під індексом 1.

    content = [x.strip()[x.find('Timestamp'):x.find('|')].split() for x in f.readlines() if '0003' in x][::-1]

# Після того як ми прочитали потрібні нам дані і зберегли їх - порахуємо різницю наступного і початкового рядку
# (виключаючи останній рядок, щоб не вийти за межі списку, адже його різниця з минулим і так порахується)
# і те чи виходять вони за певні межі часу і в залежності від цього будем логувати варнінг чи ерор.

content_dicts = []

for i in range(len(content)):
    for j in range(len(content[i])):
        if j == 0:
            content_dicts.append({content[i][j]: content[i][j + 1]})
        if j % 2 == 0:
            content_dicts[i].setdefault(content[i][j], content[i][j + 1])

today = datetime.datetime.strftime(datetime.datetime.today(), '%Y-%m-%d')

for i in range(len(content_dicts[:-1])):
    start = datetime.datetime.strptime(today + ' ' + content_dicts[i]['Timestamp'], '%Y-%m-%d %H:%M:%S')
    end = datetime.datetime.strptime(today + ' ' + content_dicts[i + 1]['Timestamp'], '%Y-%m-%d %H:%M:%S')
    if datetime.timedelta(seconds=30) < end - start < datetime.timedelta(seconds=32):
        my_logger.logger.warning(f'Warning! Heartbeat difference is {end - start}. Time of incident {end}')
        warning_count += 1
    if datetime.timedelta(seconds=32) <= end - start:
        my_logger.logger.error(f'Critical! Heartbeat difference is {end - start}. Time of incident {end}')
        critical_count += 1

print(f'Усього варнінгів: {warning_count}', f'Усього критичних помилок: {critical_count}')
