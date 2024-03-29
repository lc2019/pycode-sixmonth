def test1():
    print("test begin")


def test2():
    print("test2 begin")
    test1()
    print("test2 over")


test2()  # 函数调用


def add(n, m):
    x = 0
    for i in range(n, m):
        x += i

    return x


rest = add(0, 101)
print(rest)


# 阶乘
def fac(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


# 阶乘和
def fcm(m):
    x = 1
    for i in range(1, m + 1):
        x += fac(m)
    return x


r1 = fcm(5)
print(r1)

# 变量的作用域
a = 100


def test3():
    x = 'hello'
    print('x = {}'.format(x))
    # a = 10  # 局部变量优先
    # print('函数内部a = {}'.format(a))

    # 修改全局变量
    global a
    a = 20
    print("修改全局变量 a = {}".format(a))

    # print(locals(), globals())


test3()


# 位置参数 默认参数在args后 可变关键字参数**kwargs
def foo(a, b, *args, start=5, **kwargs):
    sum = a + b + start
    # 直接遍历的是key  kwargs以字典的形式保存
    # for k in kwargs:
    #     sum+=kwargs[k]

    for arg in args + tuple(kwargs.values()):
        sum += arg
    print(sum)


foo(4, 5, start=5, c=10, d=20)
