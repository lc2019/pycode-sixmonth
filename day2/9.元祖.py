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

# 嵌套元组的遍历
t = (1, 2, 3, (4, 5, 6))
for v in t:
    # 判断参数1是否是参数2 的类型
    if isinstance(v, tuple):
        for v2 in v:
            print(v2)
    else:
        print(v)

# 元组的常用方法
t = (1,2,3,4,55,5,5,6,6,2,3,2)
print(t.count(2))
print(t.index(2)) # 首次出现的下标

# 查找
print(num.index(1))

# 相加
num = num + num3
print(num)
