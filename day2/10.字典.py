# 字典{} 键值对出现  k-->v
per = {'leichao': 18, 'lulu': 18, '2020': 'kaishi'}
# 如果key有重复的 后面的key会覆盖前面的key
print(per)
# key只能是不可变的数据类型 字符串 数字 元组

# 字典的操作
print(per.get('leichao'))  # 如果没有返回None
print(per.get('leichao1'))  # 如果没有返回None

# 添加,不存在直接添加
per['goon'] = 2020
print(per)
# 更新字典
hope={'2022':'goon'}
per.update(hope)

# 删除 随机
print(per.pop('2020'))
del per['lulu']

# 遍历 ,获取所有的键值对
for k, v in per.items():
    print(k, v)

# 获取所有的key
for k in per.keys():
    print(k)

# 获取所有的值
for v in per.values():
    print(v)

# 字典的合并
addr = {'hubei': 'tianmen'}
per.update(addr)
print(per)
