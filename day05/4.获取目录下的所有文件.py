import os.path


# # 遍历所有的文件和文件夹 递归
# def get_files(src_path):
#     if not os.path.exists(src_path):
#         print('输入的路径不存在')
#         return
#
#     if os.path.isdir(src_path):
#         lds = os.listdir(src_path)
#         for name in lds:
#             # 需要绝对路径
#             path_name = src_path + '/' + name
#             if os.path.isfile(path_name):
#                 print(path_name)
#             elif os.path.isdir(path_name):
#                 get_files(path_name)
#

# 使用自带的方法解决
def get_files(src_path):
    res = os.walk(src_path)
    for path,files in res:
        for file in files:
            print(os.path.abspath(os.path.join(path,file)))

# ('../day07', [], ['1.魔法方法.py'])
get_files('../')
