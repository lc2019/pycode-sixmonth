# 定义的自动执行的方法

class Person(object):
    # 初始化
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 字符串
    def __str__(self):
        return f'name is :{self.name},age is :  {self.age}'

    # 列表
    def __repr__(self):
        return f'name is :{self.name},age is :  {self.age}'


p1 = Person('ll', 18)
p2 = Person('lc', 20)
p3 = Person('lc', 20)
print(p1, p2)
print(p2 == p3)
