class Animal:
    def __init__(self):
        self.legs = None
        self.wings = None
        self.sound = None
        self.coordinates = None

    def update_coordinates(self, lat, long):
        self.coordinates = (lat, long)

    def make_sound(self):
        return self.sound

class Dog(Animal):
    def __init__(self):
        self.legs = 4
        self.wings = False
        self.sound = 'barks'

    def is_thirsty(self):
        return 'pants'

fido = Dog()
print(fido.make_sound())
print(fido.is_thirsty())
fido.update_coordinates(4, 6)
print(fido.coordinates)
