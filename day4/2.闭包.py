# 闭包 外部变量+函数
def outer(n):
    x = n

    def inner():
        # 内部函数操作局部变量
        return x + 1

    return inner


print(outer(3)())  # 4 将x +1 返回
