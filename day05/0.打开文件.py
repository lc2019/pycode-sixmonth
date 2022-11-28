# 文件操作

# 打开文件 以写的模式
# # --w没有会直接创建文件,有的话会直接进行覆盖
# r不会覆盖 不存在会打开失败
f = open('a.txt', 'r')

f.close()

# 文件读取

f1 = open('a.txt', 'rt')

# 读取一部分
content = f1.read(10)
print(content)

# 默认读取有的文件内容
print(f1.read())


# 循环读取
while True:
    content = f1.read(1)
    # 如果读取的结果为‘’ 表示文件读取结束
    if not content:
        break
    print(content,end='')


# readlines 一换行的方式读取整个文件
f3=open('a.txt','r')
# print(f3.readlines())

for line in f3.readlines():
    print(line)


# 循环读取
while True:
    # 每次读取一行
    content = f3.readline()
    # 如果读取的结果为‘’ 表示文件读取结束
    if not content:
        break
    print(content,end='')


# 关闭文件流
f1.close()
