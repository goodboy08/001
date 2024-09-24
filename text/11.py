# 考察列表遍历，考察整数转字符串，考虑字符串的拼接
lst=[1,2,3,4]
# 定义空字符串用于拼接字符串
result=''
# 遍历列表元素
for num in lst:
    # 把整数转成字符串，然后拼接到result
    result+=str(num)
# 打印结果
print(result)