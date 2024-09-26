number=eval(input('请输入您的6位中奖号码:'))
#使用if语句
if number==987654:
    print('恭喜您，中奖了')

if number!=987654:
    print('您未中本期大奖')
print('-------以上if判断的表达式，使用比较运算符，比较表达式--------')

n=98 #赋值
if n%2:  # 98%2 的余数为0, 0的布尔值为False, 非0的布尔值为 True
    print(n,'为奇数')
if not n%2:  # 98%2 的余数为0, 0 的布尔值为False,not False 结果为True
    print(n,'为偶数')

