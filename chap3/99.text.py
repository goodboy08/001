# 99乘法表，列=column, 行=row
# 1*1=1
# 1*2=2  2*2=4
# 1*3=3  2*3=6  3*3=9
# 当行>=列时，换下一行
row=1  # 定义行变量
while row<=9:
    col = 1  # 定义列变量
    while col<=row:
        print('%d*%d=%d' % (col,row,col*row),end='\t')
        col += 1
    print('')
    row+=1


