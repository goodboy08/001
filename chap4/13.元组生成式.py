t=(i for i in range(4))
print(t)  # <generator object <genexpr> at 0x00000224D88BA0B0>  生成器对象
# t=tuple(t)
# print(t)  # (0, 1, 2, 3, )

# for item in t:
    # print(item,end='\t') # 0       1       2       3   

# __next__()方法
print(t.__next__())  # 0
print(t.__next__())  # 1
print(t.__next__())  # 2

t=tuple(t)
print(t)   # (3,)
