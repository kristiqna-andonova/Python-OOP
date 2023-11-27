from unittest import TestCase, main
#from unit_testing_lab.Cat.cat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Ozzy")

    def test_correct_init(self):
        self.assertEqual("Ozzy", self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_negative_eat_method(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_positive_eat_method(self):
        exp_result = 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(exp_result, self.cat.size)

    def test_negative_sleep_method(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_positive_sleep_method(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()