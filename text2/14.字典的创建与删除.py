# ·键值对  key  value
    #  -根据一个信息查找另一个信息的方式构成了“键值对”，它表示
    #   索引用的键和对应的值构成的成对关系

# ·字典的特征
    # -通过键从字典中获取指定的项，但不能通过索引来获取
    # -字典是无序的，也被称为hash表（散列表）
    # -是Python中的可变序列
    # -字典中的键必须唯一，如果出现两次，后出现的将覆盖先出现的
    # -字典中的键要求是不可变序列

# ·字典的创建
    # -使用{}直接创建字典
        # d=(key1: value1, key2: value2......}
    # -使用内置函数dict()创建字典
        # ·通过映射函数创建字典
            # zip(lst1,Ist2)
        # ·通过给定关键字创建字典
            # dict(key1=value1,key2=value2..)

# 1.直接使用{}创建
d={10:'cat',20:'pig',30:'pet',20:'zoo'}   # key相同，值进行覆盖
print(d)   # {10: 'cat', 20: 'zoo', 30: 'pet'}

# zip()函数的使用
lst1=[10,20,30,40]
lst2=['cat','dog','car','zoo']
zipobj=zip(lst1,lst2)  # 映射函数的结果是一个zip对象
print(zipobj)   # <zip object at 0x00000242A303B180>
#print(list(zipobj))  # [(10, 'cat'), (20, 'dog'), (30, 'car'), (40, 'zoo')]
d=dict(zipobj)
print(d)  # {10: 'cat', 20: 'dog', 30: 'car', 40: 'zoo'}

# 使用参数创建字典
d=dict(cat=10,dog=20)  # 注意事项：参数相当于变量，变量的名字不加引号
print(d)   # {'cat': 10, 'dog': 20}

t=(10,20,30)   # 创建一个元组
print({t:10})   # {(10, 20, 30): 10}

# lst=[10,20,30]  # TypeError: unhashable type: 'list'
# print({lst:10})  因为列表是可变数据类型，不能做键

# 字典属于序列类型
print('max:',max(d))   # dog
print('min:',min(d))   # cat 
print('len:',len(d))   # 2

# 字典的删除
del d
print(d)   # NameError: name 'd' is not defined
