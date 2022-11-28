class Person(object):
    # 初始化 自动调用
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print('eat ...' + food)

    # 字符串格式化 自动调用
    def __str__(self):
        return f'{self.name}...{self.age}'

    def __del__(self):
        del self.name

c1 = Person('lc', 18)

print(c1)
c1.eat('chicken')
del c1
