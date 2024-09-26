# 遍历循环的扩展模式
# -语法结构

# for 循环变量 in 遍历对象：
#   语句块1
# else:
#   语句块2

# -else语句只在循环正常结束后才执行
# -通常与break和continue语句一起使用
s=0  # 定义一个变量s，用来存储数据
for i in range(1,11):
    s+=i   # s=s+i  把s+i的值，再重新赋于s
else:
    print('1-10之间的累加和为：',s)


