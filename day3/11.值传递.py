# 变量的作用域
# global 所有的全局变量
# locals 当前作用域的所有变量
# vars
a = 100  # 全局变量
x = 'hi'


def test(a):
    a = 1  # 局部变量
    print(f'函数内部的x的值是', a)
    global x  # global 修改全局变量
    x = 'hello'
    print(f'函数内部的x的值是', x)


def demo(num):  # 地址传递 可变数据类型
    num[0] = 10


test(a)  # 1
num = [1, 2, 5]
demo(num)  # 10
print(num)
print(f'函数外部部的x的值是', x)
