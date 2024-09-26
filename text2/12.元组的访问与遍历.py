t=('python','hello','world')
print(t[0])  # python

t2=t[0:3:1]  # 元组支持切片操作
print(t2)  # ('python', 'hello', 'world')

# 元组的遍历
for item in t:
    print(item)
# python
# hello
# world

# for+range()+len()组合遍历 
for i in range(len(t)):
    print(i,'-->',t[i])
# 0 --> python
# 1 --> hello
# 2 --> world

# 使用enumerate()
for index,item in enumerate(t,1):
    print(index,item)
# 1 python
# 2 hello
# 3 world