
x=True
print(x)     #   True
print(type(x))  # 对像类型为布尔  <class 'bool'>

print(x+10)  # 1+10  True为1
print(False+10)  # 0+10   False为0

print('--------------------')
# 测试对象的bool值
print(bool(18))   # True
print(bool(0),bool(0.0))   # False
# 总结，非0的数值型布尔值都为True
print(bool('北京欢迎你'))   # True
print(bool(''))   # False
print(bool(False))   # False
print(bool(None))   # False
