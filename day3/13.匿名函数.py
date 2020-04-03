def add(a, b):
    return a + b


x = add(1, 3)
print(x)
fn = add  # 类似别名的作用
print(id(fn), fn)  # <function>

# 除了使用def还可以使用lambda
lambda a, b: a + b  # 匿名函数,一次使用


# lambda当做参数传给另一个参数使用

def calc(a, b, fn):
    c = fn(a, b)  # fn类似别名
    return c


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# 回调函数
x1 = calc(10, 20, add)
x2 = calc(10, 20, sub)
print(x1, x2)

# lambda作为参数传递
x3 = calc(1, 2, lambda x, y: x + y)
print(x3)
