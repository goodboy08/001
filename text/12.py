# 编程实现 把一个元素全为数字的列表中的所有偶数加1
lst=[2,5,10,9,6,80,51,11,26]
for i in lst:
    if i%2==0:
        lst[lst.index(i)]=(i+1)
print(lst)