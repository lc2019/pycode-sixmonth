stus = [
    {'name': 'zhangsan', 'age': 18, 'score': 50, 'tel': '13655558888', 'gender': 'female'},
    {'name': 'lisi', 'age': 15, 'score': 80, 'tel': '13655512354', 'gender': 'male'},
    {'name': 'wangwu', 'age': 27, 'score': 90, 'tel': '13655558789', 'gender': 'female'},
    {'name': 'zhaoliu', 'age': 17, 'score': 70, 'tel': '13655558456', 'gender': 'female'},
    {'name': 'leichao', 'age': 18, 'score': 96, 'tel': '13655558123', 'gender': 'female'},
    {'name': 'lulu', 'age': 19, 'score': 96, 'tel': '13655551238', 'gender': 'male'},
]
count = 0
max_score = stus[0]['score']
max_index = 0
for i, stu in enumerate(stus):
    if stu['score'] < 60:
        count += 1
        print('不及格的学生%s，分数%d' % (stu['name'], stu['score']))
    if stu['tel'].endswith('8'):
        print('tel以8结尾:', stu['name'])
    if stu['score'] > max_score:
        max_score = stu['score']

        # max_index = i #有并列的情况出现

print('不及格的学生有%d个' % count)
print('最高分数%d' % max_score)
for stu in stus:
    if stu['score'] == max_score:
        print(stu['name'])
i - 0
j = 0
# 字典排序
for i in range(0, len(stus) - 1):
    for j in range(0, len(stus[i]) - j):
        if stus[i]['score'] > stus[i]['score']:
            stus[i]['score'], stus[i + 1]['score'] = stus[i + 1]['score'], stus[i]['score']
print(stus)

# 三个元组三门学科
sing = ('zhangsan', 'wangwu', 'zhaoliu', 'leichao')
dance = ('zhangsan', 'lisi')
rap = ('zhangsan', 'lisi')
total = set(sing + dance + rap)
print(total)  # 人数
di = {}
alls = sing + dance + rap
for p in alls:
    if p not in di:
        # 直接使用count来统计
        di[p] = alls.count(p)
print(di)

for k, v in di.items():
    if v == 1:
        print('one', k)
    elif v == 2:
        print('two', k)
    elif v == 3:
        print('three', k)
