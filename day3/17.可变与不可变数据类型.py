# 不可变 float int string tuple bool
# 可变  列表 字典 集合 / list dict set

# python参数传递都是内存地址的传递

a = 100  # 不可变数据类型


def test(a):
    a = 1


test(a)
print(a)  # 100

heros = ['lc', 'll', '2017']


def ch(x):
    x[2] = '2022'


ch(heros)
print(heros)  # ['lc', 'll', '2022']
