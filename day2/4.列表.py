# []列表，元素直接使用，分割 有序
names = ['zhangsan', 'lisi', 18, 29,18]

# list 可迭代对象转化成列表，列表是有序的
name = list(names)
print(name, names[0])
names[0] = 'wangwu'
# ['wangwu', 'lisi', 18, 29]
print(names)

# 增删改查
# 列表表常用的方法
#   增加
x = ['zhangsan']
names.extend(x)  # 列表的元素添加到列表
print(names)
names.append("2020")
print(names)
names.insert(0, '2021')
print(names)

names += ['2019']
print(names)

# 删除 pop remove clear
# pop弹出最后1个数据
print(names.pop())  # 返回最后1个数据
# print(names.pop(2))  # 删除指定下标的数据
print(names.remove(29))  # None 删除成功返回 如果不存在就报错
print(names)
print(names.count('lisi'))

del names[0]  # 删除指定下标的元素
print(names)

# 查询
print(names.index('lisi'))  # 下标
print('wangwu' in names)  # bool

# 修改
names[-1] = '2022'
print(names)

# 列表的遍历 while/ for  in
i = 0
while i < len(names):
    print(names[i])
    i += 1

# for
for i in names:
    print(i)

# 将一个可迭代对象添加序号
for i, j in enumerate(names):
    print(f'第{i}个元素是{j}')
