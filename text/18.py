# 定义一个函数sum_text接收一个参数n，在函数中计算1+2+3+...+n的值，并打印结果

def sum_text(n):
    # 保存结果
    sum=0
    # 循环因子
    i=1
    # 循环累加
    while i<=n:
        # 累加结果
        sum+=i
        # 增加循环因子
        i+=1
    print(f'1到{n}的累加和为:{sum}')

num = int(input('请输入一个整数:'))
sum_text(num)

