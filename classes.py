class Animal:
    def __init__(self, legs):
        self.legs = legs

dog = Animal(4)
print(f'I have {dog.legs} legs')

spider = Animal(8)
print(f'I have {spider.legs} legs')
