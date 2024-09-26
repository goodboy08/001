x=10
y=3
z=x/y   # 在执行除法运算，将运算的结果赋值给z
print(z,type(z))  # 隐式转换，通过运算隐式地转换了运算结果
                  # 3.3333333333333335 <class 'float'>

# float类型转换成int类型，只保留整数部分
print('float类型转换成int类型',int(3.14))
print('float类型转换成int类型',int(3.9))
print('float类型转换成int类型',int(-3.14))
print('float类型转换成int类型',int(-3.9))

# 将int类型转换成float类型
print('将int类型转换成float类型',float(18))

# 将str类型转换成int类型
print(int('200')+int('100'))

# 将str类型转换成float类型
print('将str类型转换成float类型',float('3.14'))

# 将str转换成int类型报错的情况
#print(int('18a')) # ValueError: invalid literal for int() with base 10: '18a'
#print(int('3.14'))

# 将str转换成float类型报错的情况
#print(int('3b.14'))

