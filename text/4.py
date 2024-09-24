# int=100  # 错误，对内置方法进行了赋值，导致后面int方法不可用
a='200'
b=int(a)
print(b)