'''·
列表的创建
-使用[]直接创建列表
列表名=[element1,element2,...elementN]

-使用内置方法list()创建列表
列表名=list(序列)

·列表的删除
del 列表名
'''

# 直接使用[]创建
lst=['hello','world',99.8,100]
print(lst)   # ['hello', 'world', 99.8, 100]

# 可以使用内置的list()函数创建列表
lst2=list('helloworld')
lst3=list(range(1,10,2))
print(lst2)  # ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
print(lst3)  # [1, 3, 5, 7, 9]


# 列表是序列的一种，对序列操作的运算符(+,*)，操作符(.index,.count)，函数均可以使用(max(),min(),len())
print(lst+lst2+lst3)    # 相加运算
print(lst*5)            # 相乘运算

print(lst.index(99.8))
print(lst.index('hello'))   # 列表中第一个hello的索引
print(lst.count('hello'))   # 列表中出现hello的次数

print(len(lst3))   # lst3 = [1, 3, 5, 7, 9]
print(max(lst3))
print(min(lst3))

# 列表的删除
lst4=[10,20,30]
print(lst4)
del lst4
print(lst4)
