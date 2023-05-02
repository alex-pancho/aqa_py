import random

characters = {
"Котигорошко": {"імя": "Котигорошко","рівень життя": 10,"сила": 7,"розум": 5},
"Кінь": {"імя": "Кінь","рівень життя": 12,"сила": 6,"розум": 6},
"Відьмак": {"імя": "Відьмак","рівень життя": 8,"сила": 9,"розум": 8}
}


def hello ():
    '''Intro MSG'''
    hello_msg = print('Привіт любий друже. Гайда пограємось в просту але цікаву гру.')
    return hello_msg

# hello()

your_character = {}

def choose_character():
    '''Get character'''
    global your_character
    while True:
        selected_char = input("Вибери одного із персонажів Котигорошко, Кінь, Відьмак! Тож, напиши твій вибір?: ")
        try:
            if selected_char in characters:
                print(f"Перекрасний вибір. Твій персонаж-{characters[selected_char]['імя']}. У нього такі характеристики: рівень життя-{characters[selected_char]['рівень життя']},\n"
                      f"сила-{characters[selected_char]['сила']}, розум-{characters[selected_char]['розум']}")
                your_character[selected_char] = characters[selected_char]
                break
            else:
                raise ValueError("Обраний персонаж не знайдений в списку. Спробуйте ще раз!")
        except ValueError as e:
            print(e)

    return your_character

# choose_character()

def message_after_choose_opponent():
    '''MSG'''
    no_dissapoint_msg = print('Щоб ти не сумував - я підіберу тобі опонента відповідно до твоїх навичок.')
    return no_dissapoint_msg

# message_after_choose_opponent()

opponent = {}
def random_opponent():
    '''Get random character for ruture game'''
    global opponent
    exists_character = your_character
    opponents = list(characters.values())
    chosen_opponent = random.choice(opponents)
    while chosen_opponent == exists_character:
        chosen_opponent = random.choice(opponents)
    opponent = chosen_opponent
    print(f"Юххху...Знайшов. Значить так - твій опонент буде {opponent['імя']}. У нього такі характеристики: рівень життя - {opponent['рівень життя']}, "
          f"сила - {opponent['сила']}, розум - {opponent['розум']}")
    return opponent


# random_opponent()


def meeting_stage(opponent):
    '''Action during meeting'''
    while True:
        print(f"Якщо ти зустрінешся з {opponent['імя']}, то що плануєш робити?")
        try:
            action = input(f"1. Почати діалог.\n2. Спробувати набити пику.\nВибери один із 2-х варіантів(1,2):")
            if action in ['1', '2']:
                if action == "1":
                    return speak_with_me()
                elif action == "2":
                    return lets_fight(opponent, your_character)
            else:
                print("Некоректний, ввід. Будь-ласка, виберіть варіант 1 або 2")
        except ValueError:
            print("Неправильний ввід. Спробуйте ще раз!")
        except IndexError:
            print("Неправильний індекс. Спробуйте ще раз!")
        except TypeError:
            print("Введіть від 1 до 3 включно")

# opponent = random_opponent()
# meeting_stage(opponent)


def speak_with_me():
    '''Get conversation between characters'''
    pleasant_greetings = ['Привіт друже,', "Дуже радий зустрічі,", 'О, я такий радий тебе зустріти. Тримай цукерку шановний, ']
    unpleasant_greetings = ["Чому витріщився?", "Зійди з мого шляху", "Іди броди"]
    escape_list = ["Ти втік від опонента. Вітаю", "Тебе наздогнав персонаж. Йой що буде. Тримайся", "Тікаючи, ти перечепився і впав зі скелі."]
    opponent = random_opponent()
    print(f"Ти обрав варіант розмови із опонентом {opponent['імя']}. Нагадаю, шо його рівень життя: {opponent['рівень життя']}, сила: {opponent['сила']}, розум: {opponent['розум']}.")
    while True:
        try:
            action_for_speak = input(
                "Що б хотів зробити далі?\n1.Може ввічливо привітатися?\n2.А може шось зухвало буркнути?\n"
                "3.А може, ну його - просто проігнорувати і втікти?\nВиберіть один із трьох варіантів(1,2,3):")
            if action_for_speak in ['1', '2', '3']:
                if action_for_speak == '1':
                    x_pleasant = random.choice(pleasant_greetings)
                    return print(f"{x_pleasant} {opponent['імя']}.")
                elif action_for_speak == '2':
                    x_unplesant = random.choice(unpleasant_greetings)
                    return print(f"{x_unplesant} {opponent['імя']}. О-о-о, як ти смієш так розмовляти, поганцю. Я, могутній {opponent['імя']} і таких слів не пробачу.")
                elif action_for_speak == '3':
                    x_escape = random.choice(escape_list)
                    return print(f"WOW, {x_escape}")
            else:
                print("Введіть від 1 до 3 включно")
        except ValueError:
            print("Неправильний ввід value. Спробуйте ще раз!")
        except IndexError:
            print("Неправильний індекс. Спробуйте ще раз!")
        except TypeError:
            print("Неправильний тип. Спробуйте ще раз!")


# speak_with_me(opponent)

def lets_fight(opponent, your_character):
    '''Getting fight scene'''
    print(f"Нажаль, ти обрав варіант ескалації та хочеш побитися із {opponent['імя']}. Його рівень життя: {opponent['рівень життя']}, сила: {opponent['сила']}, розум: {opponent['розум']}")
    try:
        if your_character['рівень життя'] <= 0:
            print("Ви не можете розпочати бій, бо ви мертві!")
            return
        elif opponent['рівень життя'] <= 0:
            print(f"{opponent['імя']} вже мертвий. Немає сенсу з ним битися!")
            return

        # розпочинаємо бій
        while your_character['рівень життя'] > 0 and opponent['рівень життя'] > 0:
            # гравець атакує опонента
            print(f"Ви атакуєте {opponent['імя']} і завдаєте {your_character['сила']} пошкоджень!")
            opponent['рівень життя'] -= your_character['сила']

            # перевірка чи опонент вже помер
            if opponent['рівень життя'] <= 0:
                print(f"Ви перемогли {opponent['імя']}! Отримуєте {opponent['досвід']} досвіду!")
                your_character['досвід'] += opponent['досвід']
                return

            # опонент атакує гравця
            print(f"{opponent['імя']} атакує вас і завдає {opponent['сила']} пошкоджень!")
            your_character['рівень життя'] -= opponent['сила']

            # перевірка чи гравець вже помер
            if your_character['рівень життя'] <= 0:
                print(f"{opponent['імя']} переміг вас! Ви програли!")
                return

    except:
        print('Дякуємо за гру. Приходьте коли захочете зіграти знову :)')


# lets_fight(your_character, opponent)


def main():
    '''Main function with applied functions'''
    hello()
    choose_character()
    message_after_choose_opponent()
    meeting_stage(random_opponent())
    # speak_with_me()
    # lets_fight()

#
# if __name__ == '__main__':
#     main()