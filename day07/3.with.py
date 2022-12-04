# 使用with不用在手动关闭文件 自动调用enter 和exit方法
# 也不能处理异常 但是会自动关闭
try:
    with open('../data/test.txt','r') as f:
        while True:
            f_read = f.read(1024 * 1024)
            print(f_read)
            if not  f_read:
                break
except Exception as e:
    print('file not found')