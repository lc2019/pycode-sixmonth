# 1个函数作为另一个函数的返回值
# 1个函数作为另一个函数的参数
# 函数内部在定义一个函数

def foo():
    print("wo shi foo")
    return 'foo'


def bar():
    print("bar")
    return foo  # 别名


x = bar()
print(x)

x()
print('---------')
# 先去调用bar得到foo函数 在使用foo（）调用函数
y = bar()()  # foo()
print(y)


# 函数嵌套调用
def outer():
    m = 10

    def inner():
        n = 90
        print("woshi inner ")

    print("woshi outer")
    return inner  # 返回函数


outer()()


# 函数调用 函数作为返回值
def test():
    print("woshi test")
    return 'hello'


def demo():
    print("woshi demo")
    return test


def bar():
    print("woshi bar")
    return test()


x = test()
print(x)

y = demo()
print(y)  # y是test函数名称
y()  # woshi test test()函数调用
print("----")
a = bar()
print(a)
