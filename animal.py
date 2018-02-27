class Animal:
    planet = 'Earth'

    def __init__(self):
        self.legs = None
        self.wings = None
        self.sound = None
        self.coordinates = None

    def update_coordinates(self, lat, long):
        self.coordinates = (lat, long)

    def make_sound(self):
        return self.sound

    @classmethod
    def get_planet(cls):
        return cls.planet

class Dog(Animal):
    def __init__(self):
        self.legs = 4
        self.wings = False
        self.sound = 'barks'

    def is_thirsty(self):
        return 'pants'

    @staticmethod
    def get_breeds():
        return ['Shitzu', 'Maltese', 'Poodle']

if __name__ == '__main__':
    import sys
    pluto = Dog()
    if len(sys.argv) > 1:
        pluto.sound = sys.argv[1]
    print(pluto.make_sound())
