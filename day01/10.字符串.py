word = 'zhangsan'
#左闭右开
print(word[:5]) #zhang 从头开始到end
print(word[:]) #zhangsan 取所有
print(word[2:]) #angsan #从2开始到end
print(word[1:4]) #han #从start开始，不包含end

#设置步长
print(word[1:6:2])
print(word[6:1:-1]) #asgna 倒叙
print(word[::]) #zhangsan
print(word[::-1]) #nasgnahz

#字符串的操作
x = 'adsdfhoihoasaid'
print(len(x))

#查找相关
print(x.find('a'))
print(x.index('a'))

#查找不到元素
# print(x.index('x'))
print(x.find('x')) #-1
print(x.rfind('a')) #最后一次出现的下标

#判断 is 返回bool类型
print('hello'.startswith('he')) #True
print('hello'.endswith('he'))
print('hello111'.isalpha()) #数字
print('hello111'.isalnum()) #数字 +字符

#count
print('hello'.count('l')) #2

#替换
res = 'hello'
print(res.replace('l','a')) #heaao
print(res)





