for i in 'hello world':
    if i =='r':
        break
    print(i)

print('-------------------------------------------')

for i in range(0,3):  # 遍历循环次数
    user_name=input('请输入您的姓名：')
    pwd=input('请输入您的密码：')
    if user_name=='lyt' and pwd=='123456':
        print('正在登录中.....')
        break
    else:
        if i<2:
            print('账号或密码错误，您还有',2-i,'次机会')
else:
    print('登录错误次数超过3次，请明天再试')