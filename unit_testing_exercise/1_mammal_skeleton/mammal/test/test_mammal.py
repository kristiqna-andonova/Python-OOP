from unittest import TestCase, main
from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self):
        self.mammal = Mammal("Lion", "Cat", "Arrr")

    def test_correct_init(self):
        self.assertEqual("Lion", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("Arrr", self.mammal.sound)

    def test_make_sound(self):
        self.assertEqual("Lion makes Arrr", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_get_info(self):
        self.assertEqual("Lion is of type Cat", self.mammal.info())


if __name__ == "__main__":
    main()
