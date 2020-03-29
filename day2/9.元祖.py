# 元祖 不可变数据类型
num = (1, 2, 3, 4, 5, 1, 2)
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
