#语法格式
#变量=eval（字符串）

#eval变量=去掉''

s='3.14+3'
print(s,type(s))  # 3.14+3 <class 'str'>

x=eval(s)
print(x,type(x)) # 6.140000000000001 <class 'float'>


#eval()函数经常和input()函数一起使用，用来获取用户输入的数据型
age=eval(input(('请输入您的年龄：'))) #将字符串类型转成了int类型，相当于int(age)
print(age,type(age))

height=eval(input(('请输入您的身高：'))) #将字符串类型转成了float类型，相当于float(height)
print(height,type(height))

hello='北京欢迎你'
print(hello)
#使用eval报错的情况
print(eval('hello'))



