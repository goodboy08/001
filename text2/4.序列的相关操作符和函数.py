s='helloworld'
print('e' in s)
print('e' not in s)

print('e在helloworld中存在吗?',('e'in s))
print('v在helloworld中存在吗?',('v'in s))

print('e在helloworld中不存在吗?',('e' not in s))
print('v在helloworld中不存在吗?',('v' not in s))

# 内置的函数
print('序列s的长度len():',len(s))
print('序列s的最大值max():',max(s))
print('序列s的最小值min():',min(s))

# 序列对象的方法，使用序列的名称，打点调用
print('s.index()',s.index('o')) # 在序列s中，o第一次出现的位置：索引值为4
print('s.count()',s.count('o')) # 在序列s中，o出现的总次数为：2

