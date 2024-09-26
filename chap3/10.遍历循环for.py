# 遍历循环for
    # -语法结构
    # for 循环变量 in 遍历对象：
    # 语句块

# -遍历对象
# ·字符串
for i in 'hello':
    print(i)
# ·文件
# ·组合数据类型
# ·range()函数等
print('----------------')
for i in range(1,11):
    if i%2==0:
        print(i,'是偶数')

#计算1-10之间的累加和
s=0  #用于存储累加和
for i in range(1,11):
    s+=i  # s=s+i
print('1-10之间的累加和为：',s)



