from animal_app.animal import Animal

class Dog(Animal):
    def __init__(self):
        self.legs = 4
        self.wings = False
        self.sound = 'barks'

    def is_thirsty(self):
        import pdb; pdb.set_trace()
        water_level = 0
        return 'pants: ' + water_level

    @staticmethod
    def get_breeds():
        return ['Shitzu', 'Maltese', 'Poodle']
