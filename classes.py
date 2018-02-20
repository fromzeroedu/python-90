class Animal:
    legs = 4
    print("I'm an animal")

dog = Animal()
print(f'I have {dog.legs} legs')

spider = Animal()
spider.legs = 8
print(f'I have {spider.legs} legs')
