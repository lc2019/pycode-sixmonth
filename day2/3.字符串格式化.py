name = '2020'
age = 18
# 格式化
print('my name is %s age is %d' % (name, age))

# 在字符串中使用%占位符
# %s 表示字符串
# %d 整数的占位符
# %nd 打印时n表示占位 如果不够使用空格补齐
# %f表示浮点数的占位符
# 2 format函数
x = '大家好，我是{},年龄{}'.format('zhangsan', 18)
print(f' name is {name} age is {age} ')
print(x)

# 3 列表 *
y = ['zhangsan', 18]
b = '大家好，我是{},年龄{}'.format(*y)
print(b)

# 4 字典 **
z = {'name': 'zhangsan', 'age': 18}
c = '大家好，我是{name},年龄{age}'.format(**z)
print(c)
