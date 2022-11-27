# 面向对象
class Student(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        print(self.name + ' is running...')

    def eat(self):
        print(self.name + ' is eatting...')

    def __str__(self):
        return f'name is :{self.name}, weight is :{self.weight}'


s1 = Student('lc', 80)
s1.run()
s1.eat()
print(s1)
