import random

characters = {
"Котигорошко": {
"імя": "Котигорошко",
"рівень життя": 10,
"сила": 7,
"розум": 5
},
"Кінь": {
"імя": "Кінь",
"рівень життя": 12,
"сила": 6,
"розум": 6
},
"Відьмак": {
"імя": "Відьмак",
"рівень життя": 8,
"сила": 9,
"розум": 8
}
}

your_character = []
player = []

def hello ():
    return ('Привіт любий друже. Гайда пограємось в просту але цікаву гру')

def choose_character():
    while True:
        selected_char = input("Вибери одного із персонажів Котигорошко, Кінь, Відьмак! Тож, напиши твій вибір?: ")
        your_character.append(selected_char)
        # print(your_character)
        try:
            if selected_char in characters:
                print(f"Перекрасний вибір. Твій персонаж-{selected_char}. Вій має такі характеристики: {characters[selected_char]}")
                break
            else:
                raise ValueError("Обраний персонаж не знайдений в списку. Спробуйте ще раз!")
        except ValueError as e:
            print(e)

    return your_character


# choose_character()


def random_player():
    print("sdf->>>>>")
    exists_character = choose_character()
    players = list(characters.values())
    chosen_player = random.choice(players)
    print("gg->", chosen_player['імя'])
    if exists_character != chosen_player:
        return chosen_player


random_player()



def choose_stage():
    print("")
    pass


def meeting_stage(player:str) ->str:
    print(f"Ви зустрілися з {player['імя']}. Його рівень життя: {player['рівень життя']}, сила: {player['сила']}, розум: {player['розум']}.")
    action = input("Що ви будете робити?\n1. Почати діалог з ним.\n2. Розпочати бій.\n3. Спробувати втекти.\nВиберіть один із трьох варіантів(1,2,3):")
    if action == "1":
        # print("Ви почали діалог.")
        speak_with_me(player['імя'])
    elif action == "2":
        lets_fight(your_character, player)
    # elif action == "3":
    #     print("Ви спробували втекти, але не вдалося.")


# rnd_player = random_player()
# meeting_stage(rnd_player)


def speak_with_me():
    plesant_greetings = ['Привіт друже,', "Дуже радий зустрічі,", 'О, я такий радий тебе зустріти. Тримай цукерку, ']
    unpleasant_greetings = ["Чому витрищився?", "Зійди з мого шляху", "Іди броди"]
    escape_list = ["Ви втекли від персонажа. Тепер він ваш опонент", "Вас наздогнав персонаж.Йой що буде", "Тікаючи, ви перечепилися і впали."]
    print(f"Ти обрав варіант розмови із {player['імя']} Його рівень життя: {player['рівень життя']}, сила: {player['сила']}, розум: {player['розум']}.")
    action_for_speak = input("1.Ввічливо привітатися?\n2.Щось зухвало буркнути.\n3.Проігнорувати і втікти\n3.Виберіть один із трьох варіантів(1,2,3):")
    if action_for_speak == '1':
        x_peasant = random.choice(plesant_greetings)
        print(f"{x_peasant},{player['імя']}. Я,{your_character['імя']}.Радий зустрічі із тобою")
    elif action_for_speak == '2':
        x_unplesant = random.choice(unpleasant_greetings)
        print(f"{x_unplesant}{player['імя']}. О-о-о, як ти смієш так розмовляти, поганецю. Я, могутній {player['імя']} і таких слів не пробачу")
    elif action_for_speak == '3':
        x_escape = random.choice(escape_list)
        print(f"WOW, {x_escape}")

speak_with_me()


def lets_fight(your_character, player):
    print(f"Нажаль, ти обрав варіант ескалації та хочеш побитися із {player['імя']}.Його рівень життя: {player['рівень життя']}, сила: {player['сила']}, розум: {player['розум']}")
    print(f"Нагадую, що ти обрав персонаж {your_character['імя']}.Його рівень життя: {your_character['рівень життя']}, сила: {your_character['сила']}, розум: {your_character['розум']}")
    print(f"Бій буде тривати до останньої краплі життя")

    if your_character['рівень життя'] <= 0:
        print("Ви не можете розпочати бій, бо ви мертві!")
        return
    elif player['рівень життя'] <= 0:
        print(f"{player['імя']} вже мертвий. Немає сенсу з ним битися!")
        return

    # розпочинаємо бій
    while your_character['рівень життя'] > 0 and player['рівень життя'] > 0:
        # гравець атакує опонента
        print(f"Ви атакуєте {player['імя']} і завдаєте {your_character['сила']} пошкоджень!")
        player['рівень життя'] -= your_character['сила']

        # перевірка чи опонент вже помер
        if player['рівень життя'] <= 0:
            print(f"Ви перемогли {player['імя']}! Отримуєте {player['досвід']} досвіду!")
            player['досвід'] += player['досвід']
            return

        # опонент атакує гравця
        print(f"{player['імя']} атакує вас і завдає {player['сила']} пошкоджень!")
        player['рівень життя'] -= player['сила']

        # перевірка чи гравець вже помер
        if your_character['рівень життя'] <= 0:
            print(f"{player['імя']} переміг вас! Ви програли!")
            return


lets_fight(your_character, player)