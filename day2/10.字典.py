# 有序字典
d = {'a':1,'d':2,'c':3}
print(d)

# 字典{} 键值对出现  k-->v
per = {'leichao': 18, 'lulu': 18, '2020': 'kaishi'}
hope = {'2022': 19}
# 如果key有重复的 后面的key会覆盖前面的key
print(per)
# key只能是不可变的数据类型 字符串 数字 元组

# 字典的操作 增删改查
print(per.get('leichao'))  # 如果没有返回None
print(per.get('leichao1'))  # 如果没有返回None
# 如果key不存在回报错
lulu = per['lulu']
print(lulu)
# 添加,不存在直接添加
per['goon'] = 2020
print(per)
per.update(hope)
print(per)

# 删除 随机 popiterm
print(per.pop('2020'))
del per['lulu']
per.popitem()  # 删除最后一个键值对

# 遍历 ,获取所有的键值对
for k, v in per.items():
    print(k, v)
print('--------------')
# 获取所有的key
for k in per:
    print(per[k])

for k in per.keys():
    print(k)
print('--------------')
# 获取所有的值
for v in per.values():
    print(v)
print('--------------')
# 字典的合并
addr = {'hubei': 'tianmen'}
per.update(addr)
print(per)
