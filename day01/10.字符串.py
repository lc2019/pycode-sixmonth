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

#字符串的查找

