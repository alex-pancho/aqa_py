from random import randint, choice

heroes = {
            "Котигорошко": {"power": 50,
                            "shield": 10,
                            "helth": 100,
                            "home": "поле",
                            "side": "heroes",
                            "friends": None
                            },
            "Помор": {"power": 30,
                            "shield": 20,
                            "helth": 100,
                            "home": "берег",
                            "side": "heroes",
                            "friends": None
                            },
            "Вернигора": {"power": 60,
                            "shield": 0,
                            "helth": 100,
                            "home": "гори",
                            "side": "heroes",
                            "friends": None
                            },
            }

neutrals = {
            "Кінь": {"power": 5,
                            "shield": 20,
                            "helth": 100,
                            "home": "поле",
                            "side": "neutrals",
                            "friends": None
                            },
            "Морський Вовк": {"power": 10,
                            "shield": 10,
                            "helth": 100,
                            "home": "берег",
                            "side": "neutrals",
                            "friends": None
                            },
            "Грізлі": {"power": 20,
                            "shield": 0,
                            "helth": 100,
                            "home": "гори",
                            "side": "neutrals",
                            "friends": None
                            },
            }

darks = {
            "Польовик": {"power": 10,
                            "shield": 50,
                            "helth": 50,
                            "home": "поле",
                            "side": "darks",
                            "friends": None
                            },
            "Водяник": {"power": 20,
                            "shield": 30,
                            "helth": 70,
                            "home": "берег",
                            "side": "darks",
                            "friends": None
                            },
            "Печерник": {"power": 20,
                            "shield": 0,
                            "helth": 100,
                            "home": "гори",
                            "side": "darks",
                            "friends": None
                            },
            }

locations = [
            "дорога", "поле", "берег", "гори"
            ]

actions = [
           "розійтися", "дружити", "битися"
          ]

def select_player():
    """Вибір з списку позитивних персонажів"""
    # Завдання - додати можливість обирати також зі списку
    # негативних персонажів
    char_list = [h for h in heroes]
    select = input(f"Оберіть персонажа: {', '.join([h for h in heroes])}: ").capitalize()
    if select not in char_list:
        print(f"Персонажа {select} немає спробуйте ще раз")
        return select_player()
    player = heroes.pop(select)
    return player

def select_actions(actions_tuple):
    act_a = actions_tuple[0], actions[actions_tuple[0]]
    act_b = actions_tuple[-1], actions[actions_tuple[-1]]
    select = int(input(f"Оберіть номер дії: {act_a} або {act_b}"))
    return select

def actions_processing(action, player, enemy):
    if action == 0:
        print("ви мило розійшлися")
        return player, enemy
    elif action == 1:
        if player["friends"] is None:
            player["friends"] = enemy
            print("Ви подружилися")
        else:
            print("У вас є друг, ви мило розійшлися")
    else:
        player["power"] -= enemy["power"]
        enemy["power"] -= player["power"]
        print(f"Стався бій, тепер у вас {player['power']} життя, у ворга життя {enemy['power']}")

    return player, enemy

def select_locations():
    return choice(locations)

def select_enemy():
    """Компютер робить вибір з списку залишившихся персонажів"""
    # Завдання - додати можливість  зі списку
    # нейтралів обирати персонаж компютеру
    enemy_1 = choice(list(heroes.items()))
    enemy_2 = choice(list(darks.items()))
    #enemy_3 = xxx
    number = randint(1, 2)
    if number == 1:
        enemy = heroes.pop(enemy_1[0])
        return enemy
    else:
        enemy = darks.pop(enemy_2[0])
        return enemy

def meet_hero_and_enemy(player, enemy):
    if player["side"] == enemy["side"] or enemy["side"] == "neutrals":
        actions = (0, 1)
    else:
        actions = (0, 2)
    return actions



def game():
    player = select_player()
    print("Ваші данні:", player)
    enemy = select_enemy()
    print("Ваш суперник:", enemy)
    actions = meet_hero_and_enemy(player, enemy)
    s_actions = select_actions(actions)
    player, enemy = actions_processing(s_actions, player, enemy)

if __name__ == "__main__":
    game()
