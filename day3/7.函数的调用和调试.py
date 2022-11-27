def test1():
    print('test1 begin')


def test2():
    test1()
    print('test2 begin')


test2()


# test1 begin
# test2 begin

# 求 n m之间的和
def add(n, m):
    x = 0
    for i in range(n, m):
        x += i
    return x


res = add(0, 101)
print(res)


# 计算阶乘
def fc(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


y = fc(5)
print(y)


def fac_sum(n):
    x = 0
    for i in range(1, n + 1):
        x += fc(i)  # 调用fc函数
    return x


y = fac_sum(5)
print(y)

a = 100
word = 'nihao'


def test():
    x = 'hello'
    print(x)
    a = 10
    print('neibua = {}'.format(a))
    global word  # 修改全局变量
    word = '2020'
    print(globals(), locals())


test()
print('waibu = {}'.format(a))
print('waibu = {}'.format(word))
