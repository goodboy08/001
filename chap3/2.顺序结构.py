# 赋值运算符的执行顺序, 从右到左
name='zhangsan'  # 将zhangsan赋值给就是name
age=20   # 将20赋值给变量age

a=b=c=d=10086   # 链式赋值
# 系列解包赋值
name1,age1='lisi',54  # 元组分解赋值
[name2,age2]='wangwu',68  # 列表分解赋值
print(name,age)
print(name1,age1)
print(name2,age2)

a,b,c,d='room'
print(a,b,c,d)

#扩展的字符串解包赋值
a,*b='room'
print(a,b)

print('--------输入输出语句，也是典型的顺序结构-------')
name=input('请输入您的姓名:')
age=eval(input('请输入您的年龄:'))
lucky_number=eval(input('请输入您的幸运数字:'))
print('您的姓名:',name)
print('您的年龄:',age)
print('您的幸运数字:',lucky_number)


