# ·字典元素的访问
    # d[key]或d.get(key)
# ·字典元素的遍历
    # for element in d.items(): 
      # pass

    # for key, value in d.items():
      # pass

d={'hello':10,'world':20,'python':30}
# 访问字典中的元素
# 1.使用d[key]
print(d['hello'])   # 10
# 2.使用d.get(key)
print(d.get('hello'))   # 10

# 二者之间是有区别的，如果key不存在时d[key]报错，而使用get(key)可以指定默认值 
# print(d['jave'])   # KeyError: 'jave'
print(d.get('jave'))   # None
print(d.get('java','不存在'))   # 不存在

# 字典的遍历
for item in d.items():
    print(item)  
# key-value组成的一个元组
# ('hello', 10)
# ('world', 20)
# ('python', 30)

for key,value in d.items():
    print(key,value)
# 在使用for循环遍历时，分别获取key和value
# hello 10
# world 20
# python 30