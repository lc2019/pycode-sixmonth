class Person(object):
    __instance = None  # 类属性
    __is_first = True

    # 单例模式 对象都是唯一
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        # 如果创建不会在创建实例
        return cls.__instance

    def __init__(self, name, age):
        if self.is_first:
            self.name = name
            self.age = age
            self.__is_first = False


# 调用new申请内存 调用init填入数据
p1 = Person('lc', 18)
p2 = Person('ll', 18)
print(p1, p2)
print(p1 is p2)  # True
