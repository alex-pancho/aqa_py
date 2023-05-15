import unittest
from homeworks_10 import Heroes, Negative_characters, select_hero, select_negative_character, fight_or_peace


class TestHomeworks10(unittest.TestCase):
    def setUp(self):
        # Ініціалізуємо об'єкти для тестів
        self.hero1 = Heroes("Taras", 100, 50)
        self.hero2 = Heroes("Mykola", 150, 50)
        self.negative_character1 = Negative_characters("Vladimir", 50, 20)
        self.negative_character2 = Negative_characters("Drakon", 50, 30)

    def test_select_hero(self):
        # Перевірка вибору героя
        self.assertEqual(select_hero(), self.hero1)

    def test_select_negative_character(self):
        # Перевірка вибору негативного персонажа
        self.assertEqual(select_negative_character(), self.negative_character1)

    def test_fight_or_peace(self):
        # Перевірка битви між героєм та негативним персонажем
        self.assertEqual(fight_or_peace(self.hero1, self.negative_character1), "Миритися")
        self.assertEqual(fight_or_peace(self.hero1, self.negative_character2), "Битися")

    def test_hero_initialization(self):
        # Перевірка ініціалізації героя
        self.assertEqual(self.hero1.name, "Taras")
        self.assertEqual(self.hero1.health, 100)
        self.assertEqual(self.hero1.power, 50)

    def test_negative_character_initialization(self):
        # Перевірка ініціалізації негативного персонажа
        self.assertEqual(self.negative_character1.name, "Vladimir")
        self.assertEqual(self.negative_character1.health, 50)
        self.assertEqual(self.negative_character1.power, 20)

    def test_hero_selection(self):
        # Перевірка правильного вибору героя
        selected_hero = select_hero()
        self.assertIn(selected_hero, [self.hero1, self.hero2])

    def test_negative_character_selection(self):
        # Перевірка правильного вибору негативного персонажа
        selected_character = select_negative_character()
        self.assertIn(selected_character, [self.negative_character1, self.negative_character2])

    def test_fight_result(self):
        # Перевірка результату битви
        self.assertEqual(fight_or_peace(self.hero1, self.negative_character1), "Миритися")
        self.assertEqual(fight_or_peace(self.hero2, self.negative_character2), "Битися")


    def test_power_less_than_enemy_health(self):
        # Перевірка, коли сила героя менша за здоров'я негативного персонажа
        self.assertEqual(fight_or_peace(self.hero1, self.negative_character2), "Миритися")

    def test_power_equal_to_enemy_health(self):
        # Перевірка, коли сила героя дорівнює здоров'ю негативного персонажа
        self.assertEqual(fight_or_peace(self.hero2, self.negative_character1), "Битися")


if __name__ == '__main__':
    unittest.main()