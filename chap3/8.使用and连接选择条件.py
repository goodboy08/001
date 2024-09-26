# 使用and连接多个选择条件
# -只有同时满足多个条件，才能执行if后面的语句块
user_name=input('请输入您的姓名：')
pwd=input('请输入您的密码：')
if user_name=='lyt' and pwd=='123456':
    print('登录成功')
else:
    print('您的账号或密码不正确')



