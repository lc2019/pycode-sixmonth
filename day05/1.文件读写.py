import os,time


file = input('输入你备份的文件：')

if os.path.exists(file):
    # 二进制方式读取
    f = open(file,mode='rb')
    names = os.path.splitext(file)
    new_path=names[0]+'.bak.'+names[1]
    new_file= open(new_path,mode='wb')

    while True:
        content = f.read(1024 * 1024 * 1024)
        new_file.write(content)

        if not content:
            break

    f.close()
    new_file.close()
else:
    print('输入的文件不存在')