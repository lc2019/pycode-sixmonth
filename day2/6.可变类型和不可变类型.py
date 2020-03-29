num = [100,200,300]
num2 = num
num[0] =10
print(num2) #10
print(id(num),id(num2)) # 56238440 56238440

#可变数据类型 列表 字典 集合 -如果修改值 内层地址不会变化
#不可变数据类型 字符串 数字 元组--如果修改值 内层地址回发生变化

#列表的复制
num3 = []
for x in num:
    num3.append(x)
print(num3,id(num3),id(num))

#copy函数来解决
num4 = num.copy()
print(id(num4),num4)

# 切片实际是一个浅拷贝
num5 = num[::]
num5[0] = 400
print(num5,num)