# 元祖 不可变数据类型
num = (1, 2, 3, 4, 5, 1, 2)
num3 = (6, 7)
num2 = [1, 2, 3, 4]
num2[0] = 5
print(num2)
print(num.count(1))

# 元祖1个元素表示
age = (18,)
print(age)

# join
print(tuple('hello'))
print('*'.join('hello'))
li = ['h', 'i']
print(''.join(li))  # hi

# 查找
print(num.index(1))

# 相加
num = num + num3
print(num)
