# ·列表生成式
#    -生成指定范围的数值列表
#        Ist=[expression for item in range]
#    -从列表中选择符合条件的元素组成新的列表
#           Ist=[expression for item in 列表 if condition]

import random

lst=[item for item in range(1,11)]
print(lst)

lst=[item*item for item in range(1,11)]
print(lst)


lst=[random.randint(1,100) for _ in range(10)]
print(lst)
lst2=sorted(lst)
print(lst2)

# 从列表中选择符合条件的元素组成新的列表
lst=[item for item in range(10) if item%2==0]
print(lst)
