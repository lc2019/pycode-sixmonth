# 学生表示
#  学生的信息  id name age  使用字典来存储
#  使用容器来保存所有的字典
# sms的功能函数--增删改查


# 定义一个函数
def info_print():
    print('--------请选择功能-----')
    print('1、添加学生')
    print('2、删除学生')
    print('3、修改学生')
    print('4、查询学生')
    print('5、显示所有学生')
    print('6、退出系统')
    print('-' * 20)


# 等待存储所有学生的信息列表
info = []


# 1、添加学生信息的函数
def add_info():
    """添加学生函数"""
    # 接受用户输入学生信息
    # 1、用户输入：学号、姓名、手机号
    new_id = input("输入学号：")
    new_name = input("输入姓名：")
    new_tel = input("输入手机号：")

    # 2、判断是否添加这个学生，如果学生姓名已经存在报错提示，如果不存在则添加数据
    global info
    # 2.1 不允许姓名重复：判断用户输入的姓名如果和列表里面字典的name值是相等的，则提示姓名重复
    for i in info:
        if new_name == i['name']:
            print("此用户已经存在，请勿重复添加")
            # return 退出当前函数，后面添加信息的代码不执行
            return
    # 如果用户输入的姓名不存在，则添加该学生信息
    info_dict = {'id': new_id, 'name': new_name, 'tel': new_tel}
    # 将用户输入的数据追加到字典

    # 将这个学生的字典数据追加到列表
    info.append(info_dict)
    print(info)


# 2、删除学生的信息
def del_info():
    """删除学生"""
    # 1、用户输入要删除的学生的姓名
    del_name = input("请输入要删除的学生的姓名：")

    global info
    # 2、判断学生是否存在
    # 2.1 声明info是全局变量
    # 2.2 遍历列表
    # 2.3 判断学生是否存在，存在则执行删除信息，break：不允许重名，那么删除了一个，后面的不需要再遍历；不存在则提示
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('该学生不存在！')

    print(info)


# 3、修改学生的信息
def modify_info():
    """修改函数"""
    # 1、用户输入要修改的学生的姓名
    modify_name = input("请输入要修改的学生的姓名：")
    global info

    # 2、判断学生是否存在，如果输入的姓名存在则修改手机号，否则则提示
    for i in info:
        if modify_name == i['name']:
            i['tel'] = input("请输入新的手机号：")
            break
    else:
        print("该学生不存在")

    print(info)


# 4、查询学生信息
def search_info():
    """查询学生信息"""
    # 1、输入要查找的学生姓名
    search_name = input("请输入要查找的学生姓名：")

    global info

    # 2、判断学生是否存在，如果输入的姓名存在则显示该学生的信息，否则则提示
    for i in info:
        if search_name == i['name']:
            print("找到该学生的信息如下：")
            print(f"该学生的学号是{i['id']},姓名是{i['name']},手机号是{i['tel']}")
            break
    else:
        print("该学生不存在！")


# 5、显示所有学生信息
def print_all():
    """显示所有学生信息"""
    print('学号\t姓名\t手机号')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")


# 系统功能需要循环使用，直到用户输入6，才退出系统
while True:
    # 1、显示功能界面
    info_print()

    # 2、用户输入功能序号
    user_num = eval(input('请输入功能序号：'))

    # 3、按照用户输入的功能序号，执行不同的功能(函数)
    # 如果用户输入1，就执行添加学生的功能
    if user_num == 1:
        add_info()
        # print('添加学生')
    elif user_num == 2:
        del_info()
        # print('删除学生')
    elif user_num == 3:
        modify_info()
        # print('修改学生')
    elif user_num == 4:
        search_info()
        # print('查询学生')
    elif user_num == 5:
        print_all()
        # print('显示所有学生')
    elif user_num == 6:
        exit_flag = input("确定要退出吗？yes/no?")
        if exit_flag == 'yes':
            break
        # print('退出系统')
    else:
        print('输入的功能序号有误！')
