# i = 0
j = 0
# while i < 5:
#     while j < 5:
#         print('*'*5)
#         j+=1
#     i+=1
while j < 5:
    j +=1
    # 打印5行*
    i = 0
    while i < 5:
        i+=1
        print('*',end=" ") # 打印1个*
    # 换行
    print()

j = 0
while j<9:
    j+=1
    i = 0
    while i < j:
        i += 1
        print(i,'*',j,'=',(j*i),sep='',end="\t")
    print()

