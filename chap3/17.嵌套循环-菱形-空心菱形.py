# 思路：用空格占位  ----推断出行与列的关系

row=eval(input('请输入菱形的行数:'))   # 输入菱形的行数
# 判断输入行数是否正常
while row%2==0 or row==1 :
    print('您的输入有误,请输入一个大于1的奇数.')
    row = eval(input('请输入菱形的行数:'))  # 改变变量
# 菱形上半部分==等腰三角形
up_row=(row+1)//2  # 上部分行数
for i in range(1,up_row+1):
    # 倒三角形
    for j in range(1,up_row+1-i):  # 列数与行数相同
        print(' ',end='')
    # 1，3，5，7，9的三角形，range(1,2),range(1,4),range(1,6),range(1,8),range(1,10)
    for k in range(1,i*2):   # (1,1) (2,3) (3,5) (4,7) (5,9)
        if k==1 or k==i*2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
# 下半部分==倒等腰三角形
down_row=row//2  # 下半部分的行数
for i in range(1,down_row+1):
    # 直角三角形
        for j in range(1, i+1):  # 列数与行数相同
            print(' ', end='')
        for j in range(1, 2*down_row - 2*i+2):  # 列数与行数相同
            if j==1 or j==2*down_row - 2*i+1:
                print('*', end='')
            else:
                print(' ',end='')
        print()



