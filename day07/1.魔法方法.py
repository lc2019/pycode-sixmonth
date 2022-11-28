# 魔法方法  在定义类的时候 不需要手动调用 在适当的情况下自动调用的方法

class Person(object):
    # 初始化 init
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 方法需要有一个字符串类型的返回值
    # def __str__(self):
    #     return f'姓名：{self.name},年龄:{self.age}'

    # 列表
    def __repr__(self):
        return f'姓名：{self.name},年龄:{self.age}'

p1 = Person('lc', 20)
print(p1)
p2 = Person('ll', 18)
print(p2)

persons=[p1,p2]
print(persons)
