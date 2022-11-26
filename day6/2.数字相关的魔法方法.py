# 定义的自动执行的方法

class Person(object):
    # 初始化
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        # if self.name == other.name and self.age == other.age:
        #     return True
        return self.name == other.name and self.age == other.age


p1 = Person('ll', 18)
p2 = Person('lc', 20)
p3 = Person('lc', 20)
# == 会调用对象的eq方法 如果没有重写eq方法，默认比较内存地址
print(p2 == p3)
# 判断2个对象是否相等
print(p2 is p1)
