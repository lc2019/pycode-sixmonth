file = None
try:
    file = open('a.txt', 'r')
except Exception as e:
    print('file not found')
else:
    while True:
        content = file.read(1024 * 1024 * 1024)
        print(content)
        if not content:
            break
# 都会执行 与try一起出现
finally:
    print('file close')
    if file is not None:
            file.close()
