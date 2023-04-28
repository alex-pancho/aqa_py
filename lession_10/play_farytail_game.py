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

def hello ():
    return ('Привіт любий друже. Гайда пограємось в просту але цікаву гру')

def choose_character():
    while True:
        your_character = []
        selected_char = input("Вибери одного із персонажів Котигорошко, Кінь, Відьмак! Тож, напиши твій вибір?: ")
        your_character.append(selected_char)
        print(your_character)
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
    player = random.choice(list(characters.values()))
    if exists_character != player:
        return player

# random_player()



def choose_stage():
    print("")
    pass


def meeting_stage(player:str) ->str:
    print(f"Ви зустрілися з {player['імя']}. Його рівень життя: {player['рівень життя']}, сила: {player['сила']}, розум: {player['розум']}.")
    action = input("Що ви будете робити?\n1. Почати діалог з ним.\n2. Розпочати бій.\n3. Спробувати втекти.\nВиберіть один із трьох варіантів(1,2,3):")
    if action == "1":
        print("Ви почали діалог.")
    elif action == "2":
        # stage_two(player, characters)
        print("sss")
        pass
    elif action == "3":
        print("Ви спробували втекти, але не вдалося.")


rnd_player = random_player()
meeting_stage(rnd_player)


def speak_with_me():
    plesant_greetings = ['Привіт друже,', "Дуже радий зустрічі,", 'О, я такий радий тебе зустріти. Тримай цукерку, ']
    unpleasant_greetings = ["Чому витрищився?", "Зійди з мого шляху", "Іди броди"]
    escape_list = ["Ви втекли від персонажа. Тепер він ваш опонент", "Вас наздогнав персонаж.Йой що буде", "Тікаючи, ви перечепилися і впали."]
    print(f"Ти обрав варіант розмови із {rnd_player}")
    action_for_speak = input("1.Ввічливо привітатися?\n2.Щось зухвало буркнути.\n3.Проігнорувати і втікти\n3.Виберіть один із трьох варіантів(1,2,3):")
    if action_for_speak == '1':
        x_peasant = random.choice(plesant_greetings)
        print(f"{x_peasant}{rnd_player}")
        print(f'Я,{rnd_player}.Радий зустрічі,теж')
    elif  action_for_speak == '2':
        x_unplesant = random.choice(unpleasant_greetings)
        print(f"{x_unplesant}{rnd_player}")
        print(f'Як ти смієш так розмовляти, Поганець. Я, могутній {rnd_player} і таких слів не пробачу")')
    elif action_for_speak == '3':
        x_escape = random.choice(escape_list)
        print(f"WOW, {x_escape}")

speak_with_me()



# stage_one("Ппп")

# def stage_two(player, characters):
#     opponent = random.choice(list(characters.values()))
#     if opponent["ім'я"] == player["ім'я"]:
#         stage_two(player, characters)
#     elif:
#     print(f"Ви зустрілися з {opponent['імя']}.Його рівень життя: {opponent}")
#

# stage_two(player, characters):