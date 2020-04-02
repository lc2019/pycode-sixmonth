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
    #函数的文档
    '''
    函数-将2个数字相加得到结果返回
    :param a:第一个数
    :param b:第二个数
    :return:返回的数
    '''
    c = a + b  # c只在函数内部可见
    return c  # 如果一个函数没有返回值就是None


res = add(1, 2)
print(res)

#查看函数的帮助
help(add)
