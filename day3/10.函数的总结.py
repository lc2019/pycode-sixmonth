# def 声明
# 函数格式 def 函数名(形参1,形参2...)
# 函数调用 函数名()
# 函数返回值 return
# 返回多个结果 使用列表和字典 元祖

def add(a, b):
    return a + b


x = add(1, 3)
print(x)


def calc(a, b):
    shang = a // b
    yusu = a % b
    return shang, yusu


m, n = calc(13, 5)
print(m, n)


# 参数传递
def say_hello(name, age, city='hb'):
    print("dajiahao ,wshi{},jinnin{},laizi{}".format(name, age, city))


# 参数传递 默认参数
say_hello('lc', 18, 'tianmen')
say_hello('ll', 18)

print('hello', 'nihao', sep=" hehe")
print('lc')


# 可变位置参数*args **kwargs关键字参数 字典的形式保存
def show(a, b, *args, m=1, **kwargs):  # 缺省参数需要放最后
    print(a, b, args)  # 数组保存在元祖中
    print(kwargs)
    c = a + b + m
    # 使用循环遍历
    for arg in args:
        c += arg
    return c


print(show(1, 2, 3, 4, m=5, x=1, y=2))
