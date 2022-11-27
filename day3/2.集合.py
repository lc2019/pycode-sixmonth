# 无序 不重复的 {} set
per = {'name': 'lc'}  # 字典
x = {10, 2, 3, 4, 'lc', 4}  # 集合
print(x)  # 集合去重

# set的操作 增加
x.add('2020')
print(x)

# pop
print(x.pop())

# 删除
print(x.remove('2020'))

# 联合,多个集合合并生成新的集合
print(x.union({'liuneng', 'zhaosi'}))

# update 讲b拼接进a
x.update(['liuneng', 'hehe'])
print(x)
#
# 空集合 set()
