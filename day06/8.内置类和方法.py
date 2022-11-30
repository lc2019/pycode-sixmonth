class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 把对象当作字典使用
    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def sleep(self):
        print('sleeping...')


p = Person('lc', 18)
print(p.__class__ is Person)
print(p.__dict__)  # 显示对象的属性名和值 {'name': 'lc', 'dog': 18}
# 设置对象的属性值
p.__setattr__('name', 'll')
print(p.__getattribute__('name'))

p['name'] = 'lulu'
print(p.name)
