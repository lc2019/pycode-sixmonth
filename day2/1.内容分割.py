# split splitlines parttion rparttion
s = 'zhangsan,lisi,wangwu,zhaoliu'
s1 = s.split(',')  # 切割以后的结果就是列表
print(s1)
s2 = s.split(',', 2)  # 分割次数
print(s2)

print('asdcasd'.partition('c'))  # ('asd', 'c', 'asd')
print('asdcasd'.rpartition('d'))  # ('asdcas', 'd', '')

# 获取文件名和后缀名 x.mp3
filename = 'x.mp4'
t = filename.partition('.')
print(t)

filename = '2020.03.28-x.mp4'
print(filename.rpartition('.'))

#join
print('-'.join(s1))
print(('*'.join('hello')))
print('+'.join(('yes','ok')))
