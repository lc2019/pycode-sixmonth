def test(a):  # 值传递 不可变数据类型
    a = 100


def demo(num):  # 地址传递 可变数据类型
    num[0] = 10


x = 1
print(x)  # 1
num = [1, 2, 5]
demo(num)  # 10
print(num)

