# input接收用户输入  （输入提示信息）
# 默认回车结束
# res = input("请输入信息：")
# print(res)

# 数据类型转换，input接收的是str类型
# num1 = eval(input("enter a num:"))
# num2 = eval(input("enter a num:"))
# print(num1+num2)

# 内置类转换
a = '31'
b = int(a)  # 将字符转为数字 '31'
print(a, b, type(a), type(b))

# x = 'hello'
# y = int(x)
# print(y)

c = '3.14'
d = '3.145'
print(float(c))
print(float(c) + float(d))

# 运算符 + - *  / % //
*x, y, z = 1, 2, 3, 4, 5
print(x, y, z, sep='-----')

# 值交换
e = 4
f = 5
e, f = f, e
print(e, f)

# 逻辑运算符 and or not


