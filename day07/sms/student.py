# 学生模块 实现学生类的定义 保存学生信息

class Student(object):
    def __init__(self, stu_id, stu_name, stu_age):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_age = stu_age

    # 格式化
    def __str__(self):
        return '| ' +self.stu_id.ljust(5) + self.stu_name.ljust(10) + self.stu_age.ljust(3) + ' |'

# 测试
# tom = Student('1','lc','12')
# print(tom)