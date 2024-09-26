# 累加和>20时，当前数
i=1  # 循环变量
s=0  # 储存累加和的变量
while i<=20:  # 循环判断
   s+=i   # 计算累加
   if s>20:  # 判断累加和，是否退出
       print('累加和>20时，当前数为:',i)
       break
   i+=1  # 改变变量

print('--------------------------')
i=0
while i<3:
    user_name=input('请输入您的姓名：')
    pwd=input('请输入您的密码：')
    if user_name=='lyt' and pwd=='123456':
        print('正在登录中.....')
        break
    else:
        if i<2:
            print('账号或密码错误，您还有',2-i,'次机会')
    i+=1
else:
    print('登录错误次数超过3次，请明天再试')




