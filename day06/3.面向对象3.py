class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self, n):
        for i in range(n):
            print('won...')


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_pet(self, pet):
        self.pet = pet

    def listen_dog_bark(self, n):
        self.pet.bark(n)


p1 = Person('lc', 18)
p1.add_pet(Dog('erha', 3))
p1.listen_dog_bark(3)
