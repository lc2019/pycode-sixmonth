# 学生管理模块

from student import Student


# 启动sms 管理系统
class StuManSys(object):
    def __init__(self):
        #  {}用来保存所有的学生  key-stu_id  value-student对象作为值
        self.students = {}

    def start(self):
        print('sms start...')
        while True:
            # 打印菜单
            self.menu()
            select_id = input('请输出操作的选项序号：')
            if select_id.isdigit():
                # 判断是否是数字
                n = int(select_id)
                if n >= 0 and n <= 5:
                    # 输入学生信息
                    self.__oper(select_id)
                else:
                    print('不在范围内，请重新输入')
            else:
                print('输入的非法，请输入对应数字的ID')

    def menu(self):
        print('--------welcome sms v2----')
        print('1、添加学生')
        print('2、删除学生')
        print('3、查询学生')
        print('4、修改学生')
        print('5、显示所有学生')
        print('0、退出系统')
        print('-' * 20)

    # 用户操作
    def __oper(self, select_id):
        print('选择了序号: ', select_id)
        mothod_dict = {'1': self._add_student,
                       '3': self.__search_student_id,
                       '4': self.__modify_student_id,
                       '5': self.__show_all,
                       '2': self.__remove_student_id,
                       '0': exit}

        # 通过接受的id在字典中找到对应的方法并执行
        method = mothod_dict[select_id]
        # 调用方法，有参数的
        if select_id == '3' or select_id == '4' or select_id == '2':
            stu_id = input('请输入学生的id：')
            # 把学生id传递进去
            method(stu_id)
        elif select_id == '0':
            # 退出
            print('退出sms v2系统')
            method(0)
        else:
            # 无参
            method()

    def _add_student(self):
        print('添加学生')
        # 通过输入获取学生的信息
        stu_info = self.__input()
        # 创建学生对象 保存学生信息,
        stu = Student(stu_info[0], stu_info[1], stu_info[2])  # 调用学生的初始化方法
        # 保存到字典 append是list
        self.students[stu.stu_id] = stu

        # 测试
        print(self.students)

    # 查找学生
    def __search_student_id(self, stu_id):
        print(stu_id)
        # 定义一个默认值None 默认找不到
        stu = None
        if stu_id in self.students:
            stu = self.students[stu_id]
            # 显示学生信息
            self.__show_student_info(stu)
        else:
            print(f'未找到id为{stu_id}的学生')
        # 将找到的返回
        return stu

    # 修改学生
    def __modify_student_id(self, stu_id):
        print('要修改的学生id是：', stu_id)
        # 查找学生id 返回学生对象
        stu = self.__search_student_id(stu_id)

        # 判断
        if stu is not None:
            # 输入学生的信息 id name age
            news = self.__input()
            stu.stu_id = news[0]
            stu.stu_name = news[1]
            stu.stu_age = news[2]
            print('修改完成,新学生的信息是：')
            self.__show_student_info(stu)
        else:
            print(f'要修改的学生id{stu_id}不存在')

    # 删除学生-id
    def __remove_student_id(self, stu_id):
        # 查找学生
        stu = self.__search_student_id(stu_id)

        # 判断
        if stu:
            self.students.pop(stu_id)
        else:
            print(f'没找到{stu_id}的学生')

    # 显示单个学生
    def __show_student_info(self, stu):
        print(stu)  # 学生类已经重写了str方法

    # 显示所有的学生
    def __show_all(self):
        # 遍历打印所有的学生 字典
        for stu in self.students.values():
            self.__show_student_info(stu)

    # 用户输入
    def __input(self):
        stu_id = input('请输入学生的id：')
        stu_name = input('请输入学生的name：')
        stu_age = input('请输入学生的age：')
        return stu_id, stu_name, stu_age

    # 保存数据
    def __save_data(self):
        print('保存数据')

        # 以写的方式打开
        file_w = open('data', 'w')

        # 遍历所有学生的信息
        for stu in self.students.values():
            # 将学生转换为学生字符串对象
            stu_s = stu.stu_id + ' ' + stu.stu_name + ' ' + stu.stu_age + '\n'
            # 固定字符串写入文件
            file_w.write(stu_s)

        file_w.close()

    # 加载数据
    def __load_data(self):
        print('加载数据')
        # 打开文件 并处理文件异常
        file_r = None
        try:
            file_r = open('data', 'r')
        except Exception as e:
            print(e, '文件不存在')
        else:
            # 读取文件内容 按行
            content = file_r.readlines()

            # 遍历数据
            for stu_s in content:
                s_info = stu_s.split()

                # 创建学生对象保存到字典
                stu = Student(s_info[0], s_info[1], s_info[2])

                # 添加到字典
                self.students[stu.stu_id] = stu
        finally:
            if file_r is not None:
                file_r.close()
