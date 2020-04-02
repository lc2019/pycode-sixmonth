# 函数定义
# def 函数名（）:
def prt():
    print('这是1个函数')


prt()  # 函数的调用()


# 函数的参数
def sum(a, b):  # 占位
    sum = a + b
    print(sum)


sum(1, 2)  # 按照顺序赋值
sum(b=10, a=20)  # 变量名来赋值


# 函数的返回值-函数执行的结果
def add(a, b):
    c = a + b  # c只在函数内部可见
    return c  # 如果一个函数没有返回值就是None


res = add(1, 2)
print(res)


# 对函数进行说明
def test(a, b):
    """
    这是1个相加的函数
    :param a:  第一个数
    :param b:  第2个数
    :return: 返回值
    """
    return a + b


help(test)


def test2(a, b):
    x = a // b
    y = a % b
    return x, y


# res,re2 = test2(13, 5)
res = test2(13, 5)
print(res[0], res[1])
