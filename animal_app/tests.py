import os, sys
import unittest

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
    ))

from animal_app.animal import Animal
from animal_app.canine.dog import Dog

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal = Animal()

    def test_legs(self):
        self.animal.legs = 4
        self.assertEqual(self.animal.legs, 4)

    def test_coordinates(self):
        self.animal.update_coordinates(15, 4)
        self.assertEqual(self.animal.coordinates, (15,4))

class TestDog(unittest.TestCase):

    def setUp(self):
        self.dog = Dog()

    def test_legs(self):
        self.assertEqual(self.dog.legs, 4)

    def test_sound(self):
        self.assertEqual(self.dog.sound, 'barks')

if __name__ == '__main__':
    unittest.main()
