# ·字典生成式
    # -使用指定范围的数作key
       # d={key:value for item in range}
    # -使用映射函数生成字典
       # d={key:value for key,value in zip(Ist1,Ist2)}
import random
d={item : random.randint(1,100) for item in range(5)}
print(d)  # {0: 86, 1: 57, 2: 73, 3: 47, 4: 30}

# 创建两个列表
lst=[1001,1002,1003]
lst2=['陈梅梅','王一一','李丽丽']
d={key:value for key,value in zip(lst,lst2)}
print(d)  # {1001: '陈梅梅', 1002: '王一一', 1003: '李丽丽'}