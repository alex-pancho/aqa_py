import sys

list_of_characters={"Козак": {"power": 4, "intellect": 2, "eloquence": 1, "life": 2},
                    "Гулап": {"power": 2, "intellect": 4, "eloquence": 1, "life": 2},
                    "Булат": {"power": 1, "intellect": 1, "eloquence": 5, "life": 2}}
list_of_orcs={"Орк обычный": {"power": 4, "intellect": 0, "eloquence": 2},
              "Слегка умный орк": {"power": 2, "intellect": 4, "eloquence": 2},
              "Доверчивый орк": {"power": 7, "intellect": 0, "eloquence": 0}}
locations={"Гиран", "Хейн", "Годарт"}
my_character={}


def intro():
    print ("Приветствую дорогой странник, сегодня у нас будет увлекательное путишествие, "
           "\nнам предстоит уничтожить много орков, в конце нас ждет босс Путенойд и его усатый "
           "\nохраник.:")


intro ()


def continue_input():
    while True:
        try:
            continue1=input ("--------------------------------------------------------------------"
                             "\nВведи + чтобы продолжить, либо Finish, чтобы завершить игру: ")
            if continue1 != "+" and continue1 != "Finish":
                raise ValueError ("--------------------------------------------------------------------------"
                                  "\nОшибка ввода, введите + для продолжения, либо Finish для завершения игры")
            elif continue1 == "+":
                return
            elif continue1 == "Finish":
                print ("Очень жаль! Будем Вас ждать!")
                sys.exit ()
        except ValueError as e:
            print (e)


continue_input ()


def char_show():
    print ("--------------------------------------------------------------"
           "\nСейчас нам нужно выбрать персонажа, который накажет супостата ")
    for char in list_of_characters:
        print ("_________________________________________", char, "__________________________________________")
        for atrribute, value in list_of_characters[char].items ():
            print (atrribute, ":", str (value))
    print ("--------------------------------------------------------------"
           "\nВыше представлены характеристики каждого из персонажей. Выбери того кто больше по душе. ")


char_show ()


def character_select():
    while True:
        try:
            player=input ("Выбираю: ")
            if player not in list_of_characters:
                raise ValueError ("Некорректный выбор персонажа, выберите Козак, Гулап или Булат")
            if player == "Козак":
                print ("--------------------------------------------------------------"
                       "\nОтличный выбор, помни что твой основной атрибут сила, так что кулачные бои твой конек")
                my_character.update ({player: list_of_characters[player]})
                return
            elif player == "Гулап":
                print ("--------------------------------------------------------------"
                       "\nОтличный выбор, помни твой основной атрибут интеллект,так что бери врага хитростью ")
                my_character.update ({player: list_of_characters[player]})
                return
            elif player == "Булат":
                print ("--------------------------------------------------------------"
                       "\nОтличный выбор, помни твой основной атрибут красноречие,так что можешь заставить врага сдаться ")
                my_character.update ({player: list_of_characters[player]})
                return
        except ValueError as e:
            print (e)


character_select ()
continue_input ()


def start_of_adventure():
    print ("--------------------------------------------------------------"
           "\nЧтож, теперь мы готовы к нашему путишествию, у нас есть три боевые позиции которые необходимо проверить.", locations, "Начнем мы с Хейна!")
    continue_input ()
    print ("Ага вижу впереди подозрительную активность, похоже это Слегка умный орк.", list_of_orcs["Слегка умный орк"],
           "Обрати внимание что основной атрибут орка интелект"
           "\nНе чего с ним говорить! Бей в лоп!")
    return


start_of_adventure ()
continue_input ()


def hein():
    while True:
        try:
            choose_of_fight1=input ("----------------------------------------------"
                                    "\n     Напиши что будем делать с орком"
                                    "\n----------------------------------------------"
                                    "\n                                             "
                                    "\n___Бить!____Дурить!____Заставлять сдаватся!___"
                                    "\nБудем - ")
            if choose_of_fight1 != "Бить!" and choose_of_fight1 != "Дурить!" and choose_of_fight1 != "Заставлять сдаватся!":
                raise ValueError ("Ошибка ввода команды. Для продолжения введите либо Бить! либо Дурить! либо Заставлять сдаватся!")
            elif choose_of_fight1 == "Бить!":
                for name, value in my_character.items ():
                    if value["power"] >= list_of_orcs["Слегка умный орк"]["power"]:
                        print ("Орк получил в бубин, поздравляю с успешной атакой!")
                        for key in my_character:
                            my_character[key]["life"]+=1
                            print ("Твой запас жизней +1: Всего жизней:", my_character[key]["life"])
                            return
                    else:
                        for key in my_character:
                            my_character[key]["life"]-=1
                            print ("Орк оказался сильнее тебя, ты ранен, твоя жизнь уменьшилась на 1. Всего жизней:", my_character[key]["life"])
                            if my_character[key]["life"] == 0:
                                print ("Ты исчерпал запас жизней, прийдется начать сначала")
                                return
            elif choose_of_fight1 == "Дурить!":
                for name, value in my_character.items ():
                    if value["intellect"] >= list_of_orcs["Слегка умный орк"]["intellect"]:
                        print ("Обхитрил, орк упал в яму с картошкой!")
                        for key in my_character:
                            my_character[key]["life"]+=1
                            print ("Твой запас жизней +1: Всего жизней:", my_character[key]["life"])
                            return
                    else:
                        for key in my_character:
                            my_character[key]["life"]-=1
                            print ("Не обхитрил! Орк ранил тебя. Твоя жизнь уменьшилась на 1! Всего жизней:", my_character[key]["life"])
                            if my_character[key]["life"] == 0:
                                print ("Ты исчерпал запас жизней, прийдется начать сначала")
                                return
            elif choose_of_fight1 == "Заставлять сдаватся!":
                for name, value in my_character.items ():
                    if value["eloquence"] >= list_of_orcs["Слегка умный орк"]["eloquence"]:
                        print ("Орк сдался и сдал кординаты тайником с туалетами")
                        for key in my_character:
                            my_character[key]["life"]+=1
                            print ("Твой запас жизней +1: Всего жизней:", my_character[key]["life"])
                            return
                    else:
                        for key in my_character:
                            my_character[key]["life"]-=1
                            print ("Орк отказался сдаватся и напал на тебя! Ты отступил, твоя жизнь уменьшилась на 1!", my_character[key]["life"])
                            if my_character[key]["life"] == 0:
                                print ("Ты исчерпал запас жизней, прийдется начать сначала")
                                return
        except ValueError as e:
            print (e)


hein ()
continue_input ()


def start_of_adventure_stage2():
    print ("--------------------------------------------------------------"
           "\nТак этому розьбийныку! Так, время двигать дальше! Впереди нас ждет солнечный Гиран")
    print ("Ага вижу Обыного орка", list_of_orcs["Орк обычный"], "Довольно сильный персонаж, бей по слабым местам!")


start_of_adventure_stage2 ()
continue_input ()


def giran():
    while True:
        try:
            choose_of_fight1=input ("----------------------------------------------"
                                    "\n     Напиши что будем делать с орком"
                                    "\n----------------------------------------------"
                                    "\n                                             "
                                    "\n___Бить!____Дурить!____Заставлять сдаватся!___"
                                    "\nБудем - ")
            if choose_of_fight1 != "Бить!" and choose_of_fight1 != "Дурить!" and choose_of_fight1 != "Заставлять сдаватся!":
                raise ValueError ("Ошибка ввода команды. Для продолжения введите либо Бить! либо Дурить! либо Заставлять сдаватся!")
            elif choose_of_fight1 == "Бить!":
                for name, value in my_character.items ():
                    if value["power"] >= list_of_orcs["Орк обычный"]["power"]:
                        print ("Орк получил в бубин, поздравляю с успешной атакой!")
                        for key in my_character:
                            my_character[key]["life"]+=1
                            print ("Твой запас жизней +1: Всего жизней:", my_character[key]["life"])
                            return
                    else:
                        for key in my_character:
                            my_character[key]["life"]-=1
                            print ("Орк оказался сильнее тебя, ты ранен, твоя жизнь уменьшилась на 1. Всего жизней:", my_character[key]["life"])
                            if my_character[key]["life"] == 0:
                                print ("Ты исчерпал запас жизней, прийдется начать сначала")
                                return
            elif choose_of_fight1 == "Дурить!":
                for name, value in my_character.items ():
                    if value["intellect"] >= list_of_orcs["Орк обычный"]["intellect"]:
                        print ("Обхитрил, орк упал в яму с картошкой!")
                        for key in my_character:
                            my_character[key]["life"]+=1
                            print ("Твой запас жизней +1: Всего жизней:", my_character[key]["life"])
                            return
                    else:
                        for key in my_character:
                            my_character[key]["life"]-=1
                            print ("Не обхитрил! Орк ранил тебя. Твоя жизнь уменьшилась на 1! Осталось жизней: ", my_character[key]["life"])
                            if my_character[key]["life"] == 0:
                                print ("Ты исчерпал запас жизней, прийдется начать сначала")
                                return
            elif choose_of_fight1 == "Заставлять сдаватся!":
                for name, value in my_character.items ():
                    if value["eloquence"] >= list_of_orcs["Орк обычный"]["eloquence"]:
                        print ("В плен сдалось стадо орков, ты лучший!")
                        for key in my_character:
                            my_character[key]["life"]+=1
                            print ("Твой запас жизней +1: Всего жизней:", my_character[key]["life"])
                            return
                    else:
                        for key in my_character:
                            my_character[key]["life"]-=1
                            print ("Орк не захотел сдаватся и открыл огонь по тебе, ты ранен! Теряешь 1 жизнь!Осталось жизней: ", my_character[key]["life"])
                            if my_character[key]["life"] == 0:
                                print ("Ты исчерпал запас жизней, прийдется начать сначала")
                                return
        except ValueError as e:
            print (e)


giran ()
continue_input ()


def start_of_adventure_stage3():
    print ("--------------------------------------------------------------"
           "\nКак же сладко, когда орк страдает! Не такли?! Так впереди контрнаступ, атакуем в сторону Годарта")
    print ("Ага вижу Доверчивогой орка", list_of_orcs["Доверчивый орк"], "Он явно напуган! В плен сволоцюгу!")


start_of_adventure_stage3 ()

continue_input ()


def godart():
    while True:
        try:
            choose_of_fight1=input ("----------------------------------------------"
                                    "\n     Напиши что будем делать с орком"
                                    "\n----------------------------------------------"
                                    "\n                                             "
                                    "\n___Бить!____Дурить!____Заставлять сдаватся!___"
                                    "\nБудем - ")
            if choose_of_fight1 != "Бить!" and choose_of_fight1 != "Дурить!" and choose_of_fight1 != "Заставлять сдаватся!":
                raise ValueError ("Ошибка ввода команды. Для продолжения введите либо Бить! либо Дурить! либо Заставлять сдаватся!")
            elif choose_of_fight1 == "Бить!":
                for name, value in my_character.items ():
                    if value["power"] >= list_of_orcs["Доверчивый орк"]["power"]:
                        print ("Орк получил в бубин, поздравляю с успешной атакой!")
                        for key in my_character:
                            my_character[key]["life"]+=1
                            print ("Твой запас жизней +1: Всего жизней:", my_character[key]["life"])
                            return
                    else:
                        for key in my_character:
                            my_character[key]["life"]-=1
                            print ("Орк оказался сильнее тебя, ты ранен, твоя жизнь уменьшилась на 1. Всего жизней:", my_character[key]["life"])
                            if my_character[key]["life"] == 0:
                                print ("Ты исчерпал запас жизней, прийдется начать сначала")
                                return
            elif choose_of_fight1 == "Дурить!":
                for name, value in my_character.items ():
                    if value["intellect"] >= list_of_orcs["Доверчивый орк"]["intellect"]:
                        print ("Обхитрил, орк упал в яму с картошкой!")
                        for key in my_character:
                            my_character[key]["life"]+=1
                            print ("Твой запас жизней +1: Всего жизней:", my_character[key]["life"])
                            return
                    else:
                        for key in my_character:
                            my_character[key]["life"]-=1
                            print ("Не обхитрил! Орк ранил тебя. Твоя жизнь уменьшилась на 1! Осталось жизней:", my_character[key]["life"])
                            if my_character[key]["life"] == 0:
                                print ("Ты исчерпал запас жизней, прийдется начать сначала")
                                return
            elif choose_of_fight1 == "Заставлять сдаватся!":
                for name, value in my_character.items ():
                    if value["eloquence"] >= list_of_orcs["Доверчивый орк"]["eloquence"]:
                        print ("В плен сдалось стадо орков, ты лучший!")
                        for key in my_character:
                            my_character[key]["life"]+=1
                            print ("Твой запас жизней +1: Всего жизней:", my_character[key]["life"])
                            return
                    else:
                        for key in my_character:
                            my_character[key]["life"]-=1
                            print ("Орк не захотел сдаватся и открыл огонь по тебе, ты ранен! Теряешь 1 жизнь!Осталось жизней: ", my_character[key]["life"])
                            if my_character[key]["life"] == 0:
                                print ("Ты исчерпал запас жизней, прийдется начать сначала")
                                return
        except ValueError as e:
            print (e)


godart ()


def win():
    print ("Поздравляю! Все орки побеждены! Мордор пал!")


win ()
