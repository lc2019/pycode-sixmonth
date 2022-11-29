class Person(object):
    def __init__(self, name, dog=None):
        self.name = name
        self.dog = dog

    def work_dog(self):
        print(self.name + ' working...')
        # 多态
        self.dog.work()


class Dog(object):
    def __init__(self, name):
        self.name = name

    # 父类的方法
    def work(self):
        print(self.name + ' working...')


# 不同的子类对象都调用相同的父类方法实现不同的效果
class Pd(Dog):
    # 子类的方法
    def work(self):
        print('ooo' + self.name + ' attacking...')


class Ld(Dog):
    # 子类的方法 重写了父类的方法
    def work(self):
        print('ooo' + self.name + ' paobu...')


pd = Pd('dahuang')
p1 = Person('lc', pd)
p1.work_dog()

l1 = Ld('xiaobai')
p2 = Person('lc', l1)
p2.work_dog()
