# 学生信息 id name age 使用字典保存
# 使用列表保存多个学生的信息
# 功能函数-增删改查
# 显示所有的学生

import sys


def info_print():
    print('--------学生管理系统 V1.0-----')
    print('1、添加学生')
    print('2、删除学生')
    print('3、修改学生')
    print('4、查询学生')
    print('5、显示所有学生')
    print('6、退出系统')
    print('----------------------------')


# 等待存储所有学生的信息的字典
info = []


# 用户输入提取
def intput_info():
    # 接受用户输入学生信息
    # 1、用户输入：学号、姓名、手机号
    stu_id = input("输入学号：")
    stu_name = input("输入姓名：")
    stu_tel = input("输入手机号：")
    # 返回多个数据会组包成一个数组
    return stu_id, stu_name, stu_tel


def oper(select):
    # 3、按照用户输入的功能序号，执行不同的功能(函数)
    # 如果用户输入1，就执行添加学生的功能
    if select == 1:
        add_info()
        # print('添加学生')
    elif select == 2:
        del_id = input('输入要删除的学生的id: ')
        del_info(del_id)
        # print('删除学生')
    elif select == 3:
        modify_id = input('输入要修改的学生的id: ')
        modify_info(modify_id)
        # print('修改学生')
    elif select == 4:
        query_id = input('输入要查询的学生的id: ')
        search_info(query_id)
        # print('查询学生')
    elif select == 5:
        show_all()
        # print('显示所有学生')
    elif select == 6:
        sys.exit(0)
    else:
        print('输入的功能序号有误！')


# 1、添加学生信息的函数
def add_info():
    """添加学生函数"""
    # 将用户输入的数据追加到字典
    stu_info = intput_info()
    #  学生信息的字典
    stu = {'id': stu_info[0], 'name': stu_info[1], 'tel': stu_info[2]}
    # 2、判断是否添加这个学生，如果学生姓名已经存在报错提示，如果不存在则添加数据
    # 如果用户输入的姓名不存在，则添加该学生信息
    # 2.1 不允许姓名重复：判断用户输入的姓名如果和列表里面字典的name值是相等的，则提示姓名重复
    for i in info:
        if stu['id'] == i['id']:
            print("此用户已经存在，请勿重复添加")
            #  退出当前函数，后面添加信息的代码不执行
            return

    # 将这个学生的字典数据追加到列表
    info.append(stu)
    print(info)


# 2、删除学生的信息
def del_info(del_id):
    """删除学生"""
    # 2.3 判断学生是否存在，存在则执行删除信息，break：不允许重名，那么删除了一个，后面的不需要再遍历；不存在则提示
    stu = search_info(del_id)
    if stu != None:
        info.remove(stu)
    # for i in info:
    #     if del_id == i['id']:
    #         info.remove(i)
    #         break
    # else:
    #     print('该学生不存在！')


# 3、修改学生的信息
def modify_info(modify_id):
    """修改函数"""
    stu = search_info(modify_id)
    if stu != None:
        stu_info = intput_info()
        stu['id'] = stu_info[0]
        stu['name'] = stu_info[1]
        stu['tel'] = stu_info[2]


# 4、查询学生信息
def search_info(stu_id):
    """查询学生信息"""
    # 2、判断学生是否存在，如果输入的姓名存在则显示该学生的信息，否则则提示
    for i in info:
        if stu_id == i['id']:
            print(f"该学生的学号是{i['id']},姓名是{i['name']},手机号是{i['tel']}")
            return i

    print("该学生不存在！")
    return None


# 5、显示所有学生信息
def show_all():
    """显示所有学生信息"""
    print('学号\t姓名\t手机号')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")


def main():
    # 系统菜单功能需要循环使用，直到用户输入6，才退出系统
    while True:
        # 1、显示功能界面
        info_print()

        # 2、用户输入功能序号
        select_id = eval(input('请输入功能序号：'))

        # 3、根据输入选择对应的函数
        oper(select_id)


main()
