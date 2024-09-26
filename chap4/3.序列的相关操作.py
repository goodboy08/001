'''
序列
-序列是一个用于存储多个值的连续空间，每个值都对应一个整数
的编号，称为索引
-序列结构主要有列表、元组、集合、字典和字符串

索引
-正向递增索引，取值范围[0,N-1]
-反向递减索引，取值范围[-1,-N]

x:为元素   s:为序列

x in s        如果x是s的元素,结果为True,否则结果为False
x not in s    
len(s)        序列s中元素的个数(即序列的长度)
max(s)        序列s元素的最大值
min(s)
s.index(x)    序列s中第一次出现元素x的位置
s.count(x)    序列s中出现x的总次数
'''

# 序列的相加
s='Hello'
s2='World'
print(s+s2)   # 产生一个新的字符串序列

# 注意事项，+左右的数据类型相同，序列中元素的数据类型可以不同

lst=[10,20,30,'PHP']  # 列表属于序列

#print(s+lst)  # TypeError: can only concatenate str (not "list") to str

# 序列的相乘
print('-----序列的相乘-----')
print(s*5)
print('----------------')
print('-'*40)

