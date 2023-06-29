class Heroes:
    """Створили клас героїв"""
    def __init__(self, name: str, health: int, power: int) -> None:
        self.name = name
        self.health = health
        self.power = power


class Negative_characters(Heroes):
    """Створили клас негативних персонажів"""
    def __init__(self, name: str, health: int, power: int):
        super().__init__(name, health, power)


"""герої"""
kozak = Heroes("Козак", 100, 50)
otaman = Heroes("Отаман", 150, 50)
getman = Heroes("Гетьман", 200, 50)

heroes_list = [kozak, otaman, getman]

"""негативні персонажі"""
witch = Negative_characters("Відьма", 50, 20)
drakon = Negative_characters("Дракон", 50, 30)
wizard = Negative_characters("Колдун", 50, 25)

negative_characters_list = [witch, drakon, wizard]


def select_hero():
    """Функція вибору героя"""
    for i, hero in enumerate(heroes_list, 1):
        print(f"{i}. {hero.name}")
    try:
        choice = int(input("Виберіть героя: "))
        if 1 <= choice <= len(heroes_list):
            return heroes_list[choice - 1]
        else:
            print("Вибрано невірний номер героя!")
            return select_hero()
    except ValueError:
        print("Введіть номер героя!")
        return select_hero()


def select_negative_character():
    """Функція вибору негативного персонажа"""
    for i, character in enumerate(negative_characters_list, 1):
        print(f"{i}. {character.name}")
    try:
        choice = int(input("Виберіть негативного персонажа: "))
        if 1 <= choice <= len(negative_characters_list):
            return negative_characters_list[choice - 1]
        else:
            print("Вибрано невірний номер персонажа!")
            return select_negative_character()
    except ValueError:
        print("Введіть номер персонажа!")
        return select_negative_character()


def fight_or_peace(hero: Heroes, negative_character: Negative_characters):
    """Функція вибору між боєм та миром"""
    action = input("Виберіть дію (битися або миритися): ")
    if action.lower() == "битися":
        if hero.power >= negative_character.health:
            print("Вітаємо, ви перемогли!")
        else:
            print("Ви програли!")
    elif action.lower() == "миритися":
        print("Ви миритесь")
    else:
        print("Виберіть правильну дію!")


if __name__ == "__main__":
    hero = select_hero()
    negative_character = select_negative_character()
    fight_or_peace(hero, negative_character)