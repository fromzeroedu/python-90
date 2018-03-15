import os, sys
import unittest

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
    ))

from animal_app.animal import Animal

class TestAnimal(unittest.TestCase):

    def test_legs(self):
        animal = Animal()
        animal.legs = 4
        self.assertEqual(animal.legs, 4)

    def test_coordinates(self):
        animal = Animal()
        animal.update_coordinates(15, 4)
        self.assertEqual(animal.coordinates, (15,4))

if __name__ == '__main__':
    unittest.main()
