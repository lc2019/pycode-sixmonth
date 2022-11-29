class Person(object):
    # 初始化 自动调用
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(self.name + ' eat ...')


class Stu(Person):
    def __init__(self, name, age, gender, grade):
        # self.name = name
        # self.age = age
        # self.gender = gender
        # 使用父类的属性
        super(Stu, self).__init__(name, age, gender)
        self.grade = grade

    def study(self):
        print(self.name + ' study ...')


s = Stu('lc', 18, '男', '中二')
s.eat()
s.study()
