# ·元组
    # -由一系列按特定顺序排列的元素组成
    # -Python中的不可变序列
    # -使用()定义，元素之间使用逗号分隔
    # -元组中的元素可以是任意数据类型
# ·元组的创建
    # -使用()直接创建元组
    # -使用内置函数tuple()创建元组
# ·元组的删除
    # del元组名

# 直接使用()创建元组
t=('hello',[10,20,30],'python','world')
print(t)   # ('hello', [10, 20, 30], 'python', 'world')

# 使用内置tuple()创建元组
t=tuple('hellopython')
print(t)   # ('h', 'e', 'l', 'l', 'o', 'p', 'y', 't', 'h', 'o', 'n')

t=tuple([10,20,30])
print(t)  # (10, 20, 30)

t=tuple(range(1,11))
print(t)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 元组的相关操作：元组也是序列，操作也可以用
print('10在元组中是否存在:',(10 in t))
print('10在元组中不存在:',(10 not in t))
print('max:',max(t))
print('min:',min(t))
print('len:',len(t))
print('t.index:',t.index(3))
print('t.count:',t.count(3))

x=(10)
print(x,type(x))  # 10 <class 'int'>

x=(10,)  # 元组中只有一个元素，逗号不能省
print(x,type(x))  # (10,) <class 'tuple'>

# 元组的删除
del t
print(t)   # NameError: name 't' is not defined