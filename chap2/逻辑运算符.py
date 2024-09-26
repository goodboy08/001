print(True and True,True and False,
      False and False,False and True)
print(8>7 and 6>5)  # True and True
print(8>7 and 6<5)  # True and False
print(8<7 and 10/0)  # 当第一个表达式为False时，不计算第二个表达式
#print(10/0 and 8<7)  # ZeroDivisionError: division by zero

print('-------------------------')
print(True or True,True or False,
      False or False,False or True)
print(8>7 or 10/0)  # 当第一个表达式为True时，不计算第二个表达式

print('-------------------------')
print(not True)
print(not False)
print(not 8>7)

