list_of_characters={"Козак": {"power": 4, "intellect": 2, "eloquence": 1, "life": 2},
                    "Гулап": {"power": 2, "intellect": 4, "eloquence": 1, "life": 2},
                    "Булат": {"power": 1, "intellect": 1, "eloquence": 5, "life": 2}}
list_of_orcs={"Орк обычный": {"power": 4, "intellect": 0, "eloquence": 2},
              "Слегка умный орк": {"power": 1, "intellect": 4, "eloquence": 2},
              "Доверчивый орк": {"power": 7, "intellect": 0, "eloquence": 0}}
locations_with_orcs={"Орк обычный": "Гиран", "Доверчивый орк": "Хейн", "Слегка умный орк": "Годарт"}
locations={"Гиран", "Хейн", "Годарт"}


def intro():
    print ("Приветствую дорогой странник, сегодня у нас будет увлекательное путишествие, "
           "\nнам предстоит уничтожить много орков, в конце нас ждет босс Путенойд и его усатый "
           "\nохраник.:")


intro ()


def continue_input():
    while True:
        continue1=input ("--------------------------------------------------------------"
                         "\nВведи + чтобы продолжить, либо Finish, чтобы завершить игру: ")
        if continue1 == "+":
            return
        elif continue1 == "Finish":
            print ("Очень жаль! Будем Вас ждать!")
            break
        else:
            print ("--------------------------------------------------------------"
                   "\nОшибка ввода, введите + для продолжения, либо Finish для завершения игры")


continue_input ()

print ("--------------------------------------------------------------"
       "\nСейчас нам нужно выбрать персонажа, который накажет супостата ")
for char in list_of_characters:
    print ("___________________________________________", char, "___________________________________________")
    for atrribute, value in list_of_characters[char].items ():
        print (atrribute, ":", str (value))
print ("--------------------------------------------------------------"
       "\nВыше представлены характеристики каждого из персонажей. Выбери того кто больше по душе: ")


def character_select():
    while True:
        player=input ()
        if player == "Козак":
            print ("--------------------------------------------------------------"
                   "\nОтличный выбор, помни что твой основной атрибут сила, так что кулачные бои твой конек")
            return player
        elif player == "Гулап":
            print ("--------------------------------------------------------------"
                   "\nОтличный выбор, помни твой основной атрибут интеллект,так что бери врага хитростью ")
            return player
        elif player == "Булат":
            print ("--------------------------------------------------------------"
                   "\nОтличный выбор, помни твой основной атрибут красноречие,так что можешь заставить врага сдаться ")
            return player
        elif player == "Булат":
            print ("--------------------------------------------------------------"
                   "\nОчень жаль! Будем Вас ждать! ")
            break
        else:
            print ("--------------------------------------------------------------"
                   "\nОшибка ввода, введите позывной персонажа, либо finish для завершения игры")


character_select ()

continue_input ()


def start_of_adventure():
    print ("--------------------------------------------------------------"
           "\nЧтож, теперь мы готовы к нашему путишествию, у нас есть три боевые позиции которые необходимо проверить.", locations, "Начнем мы с Хейна!")
    return


start_of_adventure ()
continue_input ()


def hein():
    print ("Вот мы и пришли к болотам Хейн! Где то тут спрятался орк...  АААА вот же он! Да этоже Доверчивый орк", list_of_orcs["Доверчивый орк"],
           "\nВижу что у него основной атрибут сила, кулаками с ним точно махать не стоит."
           "\nЧто будем делать с орком? "
           "\n---------------------------------------------------------------------------------"
           "\n---Дратся!----------------------Хитрить!----------------------Уговорим сдатся!---"
           "\nВведи действие: ")
    while True:
        choose_of_fight1=input ()
        if choose_of_fight1 == "Дратся!":
            if list_of_characters["character"]["power"] > list_of_orcs["Слегка умный орк"]["power"]:
                print ("Орк получил в бубин, поздравляю с успешной атакой!")
                for key in list_of_characters["character"]:
                    list_of_characters["character"]["life"]+=1
                    print ("Твой запас жизней +1")
                    return
            else:
                print ("Орк оказался сильнее тебя, ты ранен, твоя жизнь уменьшилась на 1")
            for key in list_of_characters["character"]:
                list_of_characters["character"]["life"]-=1
                if list_of_characters["character"]["life"] <= 0:
                    print ("Ты умер, прийдется начать сначала")
                    return
                break
        elif choose_of_fight1 == "Хитрить!":
            if list_of_characters["character"]["intellect"] > list_of_orcs["Слегка умный орк"]["intellect"]:
                print ("Обхитрил, орк упал в яму с картошкой!")
                for key in list_of_characters["character"]:
                    list_of_characters["character"]["life"]+=1
                print ("Поздравляю,твой запас жизней +1")
                return
            else:
                print ("Не обхитрил! Орк ранил тебя. Твоя жизнь уменьшилась на 1!")
            for key in list_of_characters["character"]:
                list_of_characters["character"]["life"]-=1
                if list_of_characters["character"]["life"] <= 0:
                    print ("Ты умер, прийдется начать сначала")
                    return
                break
        elif choose_of_fight1 == "Уговорим сдатся!":
            if list_of_characters["character"]["eloquence"] > list_of_orcs["Слегка умный орк"]["eloquence"]:
                print ("Орк сдался и сдал кординаты тайником с туалетами")
                for key in list_of_characters["character"]:
                    list_of_characters["character"]["life"]+=1
                    print ("Поздравляю,твой запас жизней +1")
                    return
            else:
                print ("Орк отказался сдаватся и напал на тебя! Ты отступил, твоя жизнь уменьшилась на 1!")
                for key in list_of_characters["character"]:
                    list_of_characters["character"]["life"]-=1
                    if list_of_characters["character"]["life"] <= 0:
                        print ("Ты умер, прийдется начать сначала")
                        return
                    break
        else:
            print ("Никаких, или, орк понимает только язык силы! Вводи правильное значение и мордор скоро падет!")


hein ()
