i=1  # 1.初始化变量
j=0  # 变量用于存储累加和
while i<=100:  #2.条件判断
    j+=i   #3.语句块    相当于j=j+i，即累加和
    i+=1   #4.改变变量
else:
    print('1-100之间的累加和为：', j)
