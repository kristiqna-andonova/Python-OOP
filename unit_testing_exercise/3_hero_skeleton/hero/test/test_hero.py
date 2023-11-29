from unittest import TestCase, main
from project.hero import Hero


class HeroTest(TestCase):
    def setUp(self):
        self.hero = Hero("Test", 8, 100.1, 56.0)

    def test_correct_init(self):
        self.assertEqual("Test", self.hero.username)
        self.assertEqual(8, self.hero.level)
        self.assertEqual(100.1, self.hero.health)
        self.assertEqual(56.0, self.hero.damage)

    def test_if_names_are_the_same(self):
        enemy = Hero("Test", 8, 100.1, 56.0)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_not_enough_health(self):
        self.hero.health = 0

        enemy = Hero("Test Enemy", 8, 100.1, 56.0)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.hero.health -= 1
        with self.assertRaises(Exception) as ex1:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex1.exception))

    def test_enemy_not_enough_health(self):
        enemy = Hero("Test Enemy", 8, 0, 56.0)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Test Enemy. He needs to rest", str(ex.exception))

        enemy.health -= 1
        with self.assertRaises(Exception) as ex1:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Test Enemy. He needs to rest", str(ex1.exception))

    def test_draw(self):
        enemy = Hero("Test Enemy", 8, 100.1, 56.0)

        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(8, self.hero.level)
        self.assertEqual(-347.9, self.hero.health)
        self.assertEqual(56.0, self.hero.damage)

    def test_win(self):
        enemy = Hero("Test Enemy", 1, 1, 1)

        result = self.hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(9, self.hero.level)
        self.assertEqual(104.1, self.hero.health)
        self.assertEqual(61.0, self.hero.damage)

    def test_lost(self):
        self.hero.health = 10
        self.hero.damage = 10

        enemy = Hero("Test Enemy", 100, 100, 100)
        result = self.hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(101, enemy.level)
        self.assertEqual(25, enemy.health)
        self.assertEqual(105, enemy.damage)

    def test_str(self):
        result = f"Hero Test: 8 lvl\n" \
               f"Health: 100.1\n" \
               f"Damage: 56.0\n"
        self.assertEqual(result, str(self.hero))


if __name__ == '__main__':
    main()

