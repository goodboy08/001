
# ·集合
    # -Python中的集合与数学中集合的概念一致
    # -集合可分为可变集合set与不可变集合frozenset
    # -集合与字典中的key一致都是无序的
    # -集合中的元素要求唯一
    # -集合中只能存储不可变数据类型（字符串、整数、浮点数、元组）
    # -集合使用{}定义，元素之间使用逗号进行分隔

# ·集合的创建
    # -使用{}直接创建集合
       # s={元素1，元素2，...，元素N}  
    # -使用内置函数set()创建集合
        # s=set(可迭代对象)
# ·集合的删除
    # del集合名

# 使用{}直接创建集合
s={10,20,30,40}
print(s)  #{40, 10, 20, 30}   无序的

# s={[10,20],[20,30]}   # TypeError: unhashable type: 'list'
# s={([10,20]),([20,30])}  # TypeError: unhashable type: 'list'
# print(s)

s={}   # 创建的是字典还是集合呢？
print(type(s))  # <class 'dict'> 字典

# 如何创建空集合
s=set()
print(type(s),bool(s))  # <class 'set'> False

# 第二种创建集合的方式set()
s=set('helloworld')
s2=set([10,20,30])
s3=set(range(10))
print(s)    # {'w', 'r', 'e', 'l', 'o', 'd', 'h'}   去重'l'
print(s2)   # {10, 20, 30}
print(s3)   # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# 集合属于序列中的一种
print('max:',max(s3))  # max: 9
print('min:',min(s3))  # min: 0
print('len:',len(s3))  # len: 10

print('9在集合中是否存在?',(9 in s3))    # 9在集合中是否存在? True
print('9在集合中不存在?',(9 not in s3))  # 9在集合中不存在? False

# 集合的删除
del s3
print(s3)   # NameError: name 's3' is not defined