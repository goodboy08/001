x=20  #直接赋值, 直接将20赋值给变量x
y=10
x=x+y  #将x+y的和赋值给x, x的值为30
print(x)
x+=y
print(x)
x-=y
print(x)
x*=y
print(x)
x/=y
print(x)
x%=9
print(x)

z=3
y//=z
print(y)

y**=3
print(y)

a=b=c=100
print(a,b,c)

a,b=10,20  #python支持系列解包赋值
print(a,b)

print('-------如何交换两个变量的值-------')
# temp=0
# temp=a  #将a的值赋给temp, temp的值为10
# a=b    #将b的值赋给a, a的值为20
# b=temp  #将temp的值赋给b, b的值为10
# print(a,b)
a,b=b,a
print(a,b)





