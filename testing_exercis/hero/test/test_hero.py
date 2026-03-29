from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    username = "Test Hero"
    level = 10
    health = 100.5
    damage = 20.5

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_class_attribute_types(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_heroes_same_names(self):
        self.enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as e:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(e.exception))

    def test_hero_zero_or_negative_health(self):
        self.hero.health = 0
        enemy = Hero("Enemy", self.level, self.health, self.damage)
        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

        self.hero.health = -1
        enemy = Hero("Enemy", self.level, self.health, self.damage)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_enemy_hero_zero_or_negative_health(self):
        enemy = Hero("Enemy", self.level, 0, self.damage)
        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(e.exception))

        enemy.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        result = self.hero.battle(enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(-104.5, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_battle_win(self):
        enemy = Hero("Enemy", 2, 10, 10)

        result = self.hero.battle(enemy)

        self.assertEqual("You win", result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(85.5, self.hero.health)
        self.assertEqual(25.5, self.hero.damage)

    def test_battle_lose(self):
        enemy = Hero("Enemy", 100, 1000, 1000)
        self.hero.health = 10
        self.hero.damage = 10

        result = self.hero.battle(enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(101, enemy.level)
        self.assertEqual(905, enemy.health)
        self.assertEqual(1005, enemy.damage)

    def test_str(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
                   f"Health: {self.health}\n" \
                   f"Damage: {self.damage}\n"
        actual = str(self.hero)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
