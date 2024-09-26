# 输出倒直角三角形，5行5列
for i in range(1,6):  # 5行
    for j in range(1,7-i):  # 列数与行数相同
        print('*',end='')
    print()

print('---------------------------')
'''
----*
---***
--*****
-*******
*********
'''
# 输出一个等腰三角形 5行9列
for i in range(1,6):
    # 倒三角形
    for j in range(1,6-i):  # 列数与行数相同
        print(' ',end='')
    # 1，3，5，7，9的三角形，range(1,2),range(1,4),range(1,6),range(1,8),range(1,10)
    for k in range(1,i*2):   # (1,1) (2,3) (3,5) (4,7) (5,9)
        print('*',end='')
    print()





