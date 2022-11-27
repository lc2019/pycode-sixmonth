# 变量直接声明
hello = "你好，世界"
print(hello)

# bool
b = 34
c = True
d = ['leichao']
money = 100.1
print(b, c, d, money)
# 在python中变量没有数据类型 变量的数据类型就是值的数据类型
# <class 'str'> <class 'int'> <class 'bool'> <class 'list'>
print(type(hello), type(b), type(c), type(d), type(money))

# 类型转换
f = '100'
# eval 转数字
print(eval(f), type(eval(f)))
g = -100
print(abs(g))

print(int(f))
