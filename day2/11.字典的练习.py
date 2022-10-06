# 1.统计字符出现的次数
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'c', 'a']
d1 = {}
for c in set(x):
    # if c in d1:
    #     d1[c] += 1
    # else:
    #     d1[c] = 1
    d1[c]=x.count(c)
print(d1)
# 取值
vs = d1.values()
# 获取最大数
max_count = max(vs)
print(max_count)
# 打印出现最多的次数
for k, v in d1.items():
    # 出现最大数则打印对应的k
    if v == max_count:
        print(k)

# 2.让用户输入姓名 如果存在提示，不存在添加 继续输入年龄
name = input('enter a name:')
# 列表嵌套字典
per = [{'name': 'leichao', 'age': 18}, {'name': 'lulu', 'age': 19}]
for p in per:
    print(p)
    print(p['name'])
    if p['name'] == name:
        print('exist')
        break
    else:
        age = int(input('enter age:'))
        # 创建新的列表 加入到原来的列表里面
        newp = {'name': name,'age': age}
        per.append(newp)
        break
print(per)


x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'c', 'a']
new_x=[]
for i in x:
    if i not in new_x:
        new_x.append(i)
print(new_x)