# ·集合的相关操作方法
    # s.add(x)
        # 如果x不在集合s中，则将x添加到集合s
    # s.remove(x)
       # 如果x在集合中，将其删除，如果不在集合中，程序报错
    # s.clear()
       # 清除集合中所有元素
# ·集合的遍历
    # -使用遍历循环for
    # -使用for循环和enumerate()函数
# ·集合生成式

s={10,20,30}

# 向集合中添加元素
s.add(100)
print(s)   # {100, 10, 20, 30}

# 删除元素
s.remove(20)
print(s)   # {100, 10, 30}

# 清除集合中所有元素
s.clear()
print(s,'空集合的布尔值:',bool(s))   # set() 空集合的布尔值: False


s={101,202,303}

# 遍历集合
for item in s:
    print(item)
# 202
# 101
# 303

for index,item in enumerate(s,100000):    # 100000表示的是元素的序号
    print(index,'-->',item)
# 100000 --> 202
# 100001 --> 101
# 100002 --> 303


# 集合的生成式
s={i for i in range(10)}
print(s)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

s={i for i in range(10) if i%2!=0}
print(s)  # {1, 3, 5, 7, 9}