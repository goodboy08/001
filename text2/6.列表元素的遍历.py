'''
列表元素的遍历
    -使用遍历循环for
    -遍历循环for与range()函数和len()函数组合遍历
    -遍历循环for与enumerate()函数组合遍历元素和索引
        for index item in enumerate(lst):
输出index和item
    ·index ：用于保存元素的索引 (序号)
    ·item:用于保存获取到的元素值
'''

lst=['hello','world','python','php']

# 使用遍历循环for遍历列表元素
for item in lst:
    print(item)
# hello
# world
# python
# php

# 使用for循环，rang()函数，len()函数，根据索引进行遍历
for i in range(0,len(lst)):
    print(i,'-->',lst[i])
# 0 --> hello
# 1 --> world
# 2 --> python
# 3 --> php
    
# 使用for循环和enumerate()函数，进行遍历
for index,item in enumerate(lst):
    print(index,item)
# 0 hello
# 1 world
# 2 python
# 3 php

for index,item in enumerate(lst,10):
    print(index,item)