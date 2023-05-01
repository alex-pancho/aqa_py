"""
Текстова гра на тему Українських народних казок
Правила гри:
    Гравець має обирати персонажа, за яким він буде грати. Потім гравець починає свою
    пригоду у вигляді текстових повідомлень. Гра складається з декількох етапів, на кожному з яких гравець зустрічає нових
    персонажів та переживає різні пригоди. Гравець має право вибирати, як він хоче діяти у певній
    ситуації: діалог з персонажем, бій, втеча тощо. Залежно від вибору гравця, відбуваються різні
    наслідки.

Приклади:

* Гравець обирає персонажем козака. Він зустрічає чаклуна, який накладає на нього прокляття.
    Гравець може спробувати розв'язати прокляття, знайти антидот або битися з чаклуном.
    Залежно від вибору гравця, він може отримати нову здатність або втратити частину своїх вмінь.
* Гравець обирає персонажем пересмішника. Він потрапляє в хитру ситуацію, де йому потрібно
    обдурити злодія. Гравець може скористатися своїм словесним даром, знайти слабкі місця
    злодія або спробувати зібрати команду з іншими персонажами для змагання проти злодія.

Ідеї для  тестів:

    Тест на перевірку правильності вибору персонажа гравцем.
    Тест на перевірку вибору гравцем діалогу, який приводить до нової здатності персонажа.
    Тест на перевірку вибору гравцем діалогу, який приводить до втрати здатностей персонажа.
    Тест на перевірку правильності вибору гравцем
    Тест на введення некоректної відповіді гравцем: спроба ввести символи, відмінні від "так" і "ні".
    Тест на перехід до наступної дії: перевірка, чи збільшується лічильник після завершення попередньої.
    Тест на завершення гри: перевірка, що гравець не може перейти до наступної дії, якщо він вже завершив останню.
    Тест на вибір гравцем дії: перевірка, чи збільшується лічильник правильних відповідей після кожної правильної відповіді.

Поради до написання коду:

1. Створіть словник, що містить перелік персонажів та їх характеристик, таких як ім'я,
    рівень життя, сила тощо.
2. Запросіть у гравця вибір персонажа зі списку.
3. Визначте етапи гри, наприклад, "Зустріч з першим персонажем", "Бій з монстром",
    "Вирішення головоломки" тощо.
4. Для кожного етапу гри створіть функцію, яка відповідає за обробку цього етапу.
    Функція повинна виводити текстове повідомлення, яке описує ситуацію гравця,
    а також список доступних дій, які гравець може вибрати. Наприклад,
    "Ви зустрілися з гобліном. Що ви будете робити?
    1. Почати діалог з ним. 2. Розпочати бій. 3. Спробувати втекти".
5. Для кожної дії, яку може вибрати гравець, створіть окрему функцію.
    Функція повинна перевіряти, чи є ця дія можливою в поточній ситуації,
    і виконувати відповідні дії. Наприклад, якщо гравець вибирає
    "Розпочати бій", функція повинна розпочати бій з монстром і вивести повідомлення про результат.
6. Для обробки помилок та виключень, наприклад, якщо гравець ввів
    неправильне значення, використовуйте блоки try/except.
7. Для збереження прогресу гравця у грі, зберігайте дані у файл.

Не ускладнюйте собі життя:
Достатньо 3 персонажи та 3 дії а також 3  кроки:
    1. початок(вибір героя - Котигорошко, Змій, кінь)
    2. взаємодія(комп'ютер обирає героя з тих що лишилися і пропонує дії гравцю)
    3. розв'язка ( відповідно до обраних дій та коефіцієнтів - перемога, поразка чи нічия)
І треба хоча б 9 тестів на усе це добро.
"""

import random
from my_logger import logger

herous = {
'Ursa': {'power': 52, 'health': 600, 'speed': 6, 'money': 50},
'Warlock': {'power': 14, 'health': 1200, 'speed': 4, 'money': 0},
'Luna': {'power': 42, 'health': 780, 'speed': 7, 'money': 20}
}

monsters = {
'Rohan': {'money': 150, 'health': 1500, 'power': 550, 'speed': 2},
'Goblin': {'money': 20, 'health': 300, 'power': 15, 'speed': 5}
}

def hero_skills(key_hero):
    """This function returns selected hero's skills"""
    print(f"Your Hero's Skills: \n \
    Health: {herous[key_hero]['health']}\n \
    Power: {herous[key_hero]['power']}\n \
    Speed: {herous[key_hero]['speed']}\n \
    Money: {herous[key_hero]['money']}")
    return herous.get(key_hero)

def random_monster():
    """This function is for selecting a monster randomly"""
    monster = None
    monster = random.choice(list(monsters))
    return monster

#random_monster()

def monster_skills(monster):
    """This function returns selected monster's skills"""
    print(f"Monster's Skills: \n \
    Health: {monsters[monster]['health']}\n \
    Power: {monsters[monster]['power']}\n \
    Speed: {monsters[monster]['speed']}\n \
    Money: {monsters[monster]['money']}")

def first_stage(monster, hero):
    """This function is for selection an action by a user"""
    your_action = input("What are you gooing to do? Fight, Run or Compensate?" ).capitalize()
    print('You have chosen :', your_action)
    if your_action == 'Fight':
        logger.info('User chose: Fight')
        return fight_action(monster, hero, your_action)
    elif your_action == 'Run':
        logger.info('User chose: Run')
        return run_action(monster, hero, your_action)
    elif your_action == 'Compensate':
        logger.info('User chose: Compensate')
        return compensate_action(monster, hero, your_action)
    else:
        print("Your selected action looks weird. Please try again")
        logger.info('User selected non-existent action')
        return first_stage(monster, hero, your_action)

def fight_action(monster, key_hero, your_action):
    """This is fight between selected hero and random monster"""
    if herous[key_hero]["power"] >= monsters[monster]["power"]:
        print(f'Congratulations! You won, {monster} was killed')
        logger.info(f'{key_hero} is stronger than {monster}')
        return key_hero
    else:
        print(f'Unfortunately, {monster} is stronger than {key_hero}, but today {monster} is in a good mood and let you go')
        logger.info(f'{key_hero} is weaker than {monster}')
        return monster

def run_action(monster, key_hero, your_action):
    """This is the run of life between random monster and selected hero"""
    if herous[key_hero]["speed"] > monsters[monster]["speed"]:
        print(f"Congratulations! The right choice, it's better not to put yourself at risk."
        f" {monster} can't catch up with you anymore")
        logger.info(f'{key_hero} was faster than {monster}')
        return key_hero
    else:
        print(f"You're caught, but the {monster} doesn't need you")
        logger.info(f'{key_hero} was slower than {monster}')
        return monster

def compensate_action(monster, key_hero, your_action):
    """This is compensate action between random monster and selected hero"""
    if herous[key_hero]["money"] > 0:
        monsters[monster]['money'] += herous[key_hero]["money"]
        total_amount = calculate_money(monster_money, hero_money)
        print(f"{monster} didn't touch you, but {monster} took all your money.")
        logger.info(f'{key_hero} paid off {monster}')
        return monsters[monster]['money']
    else:
        print("You can't negotiate because you have no money. Think again about what I say and choose an action")
        logger.info('The hero has no money')
        return first_stage(monster, key_hero)

def start_game():
    """This is a simple game.
    Firstly, a user needs to choose a hero (User, Warlock, Goblin), each hero has some skills (power, health, speed, money).
    Secondly, the user will meet a monster (Rohan, Goblin) and will need to choose an action (Fight, Run, Compensate).
    The game can either end in defeat or victory, depending on the chosen hero, action and hero's skills
    """
    print("Hello, my dear guest. Let's try to play the game")
    while True:
        key_hero = input("Please make a choice! You have three herous to choose from(Ursa, Warlock and Luna): ").capitalize()
        try:
            if key_hero in herous:
                print(f"You hero is {key_hero}. Congratulations! Look at your skills:")
                hero_skills(key_hero)
                logger.info(f'The user selected: {key_hero}')
                break
            else:
                raise ValueError('Something went wrong. Please try again to type a hero')
        except ValueError as mistake:
            print(mistake)
    monster = random_monster()
    print(f"Unfortunately, on the way to your goal you encountered {monster}.\nPay attention to his skills and choose an action. Be carefull!")
    logger.info(f"User met monster: {monster}")
    monster_skills(monster)
    first_stage(monster, key_hero)
    print("Thank you for your participation")

start_game()
