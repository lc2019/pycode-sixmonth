# []列表，元素直接使用，分割
names = ['zhangsan', 'lisi', 'lisi', 18, 29]

# list 可迭代对象转化成列表，列表是有序的
name = list(names)
print(name, names[0])
names[0] = 'wangwu'
# ['wangwu', 'lisi', 18, 29]
print(names)

# 列表表常用的方法
#   增加
x = ['zhangsan']
names.extend(x)
print(names)

# 追加到末尾
names.append('123')
print(names)

# pop弹出最后1个数据
print(names.pop())  # 返回最后1个数据
print(names.pop(3))  # 删除指定下标的数据
print(names.remove(29))  # None 删除成功返回
print(names)

# 查询
print(names.index('lisi'))  # 下标
print(names.count('lisi'))  # 下标
print('wangwu' in names)  # bool

# 列表的遍历 while/ for  in
i = 0
while i < len(names):
    print(names[i])
    i += 1

# for
for i in names:
    print(i)
