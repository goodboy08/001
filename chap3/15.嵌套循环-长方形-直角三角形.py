#输出一个三行四列的长方形
for i in range(1,4):   # 一共3行
    for j in range(1,5):  # 一共4列
        print('*',end='')  # 输出每行为4列*号
    print()  # 转行操作

#输出一个直角三角形，共5行5列
for i in range(1,6):   # 一共5行
    for j in range(1,i+1):  # 列数与行数相同
        print('*',end='')
    print()  # 换行操作
