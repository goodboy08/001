# 使用or连接多个选择条件
# -只要满足多个条件中的一个，就可以执行if后面的语句块
score=eval(input('请输入您的成绩：'))
if score<0 or score>100:
    print('您的成绩无效')
else:
    print('您的成绩为：',score,sep='')


