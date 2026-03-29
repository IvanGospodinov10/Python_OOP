from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.m = Mammal("test", "Dog", "Bark")


    def test_init(self):
        self.assertEqual("test", self.m.name)
        self.assertEqual("Dog", self.m.type)
        self.assertEqual("Bark", self.m.sound)

        # test class private attribute
        self.assertEqual("animals", self.m._Mammal__kingdom)

    def test_make_sound(self):
        result = self.m.make_sound()
        self.assertEqual("test makes Bark", result)

    def test_get_kingdom(self):
        result = self.m.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        result = self.m.info()
        self.assertEqual("test is of type Dog", result)

if __name__ == '__main__':
    main()