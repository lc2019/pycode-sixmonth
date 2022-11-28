# split splitlines partition repartition
s = 'zhangsan,lisi,wangwu,zhaoliu'
s1 = s.split(',')  # 切割以后的结果就是列表
print(s1)
s2 = s.split(',', 2)  # 分割次数
print(s2)

# 分割成3部分 前面 分隔符 后面
print('asdcasd'.partition('c'))  # ('asd', 'c', 'asd')
print('asdcasd'.rpartition('d'))  # ('asdcas', 'd', '')

# 获取文件名和后缀名 x.mp3
filename = 'x.mp4'
t = filename.partition('.')
print(t)

filename = '2020.03.28-x.mp4'
print(filename.rpartition('.'))

# join
print('-'.join(s1)) # zhangsan-lisi-wangwu-zhaoliu
print(('*'.join('hello'))) # h*e*l*l*o
print('+'.join(('yes', 'ok')))

"""
判断字符串
 startswith
 endswith
 isupper
 islower
 isdigit
 isalpha
 isalnum
 issapce
"""

print('abs123'.isalnum()) # True 字母和数字
print('abs123'.isdigit()) # 纯数字
print('abs123'.isalpha()) # 纯字母


# 转换字符串
print('abs123'.upper())
print('Abs123'.lower())