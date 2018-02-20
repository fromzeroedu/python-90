class Animal:
    def __init__(self, legs):
        self.legs = legs
        self.moving = False

    def start_moving(self):
        self.moving = True

    def stop_moving(self):
        self.moving = False

    def moving_status(self):
        if self.moving is True:
            return f'The animal is moving'
        else:
            return f'The animal is stopped'

dog = Animal(4)
print(f'I have {dog.legs} legs')

spider = Animal(8)
print(f'I have {spider.legs} legs')

spider.start_moving()
print(spider.moving_status())
