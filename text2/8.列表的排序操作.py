lst=[4,55,12,65,35,4545,21,565,84,256]
print('原列表:',lst)

# 排序，默认是升序
lst.sort()
print('列表升序:',lst)

# 降序
lst.sort(reverse=True)
print('列表降序:',lst)

print('------------------------------------------')
lst2=['banana','apple','Cat','Orange']
# 升序，先排大写，再排小写
lst2.sort()
print(lst2)
# 降序，先排小写，再排大写
lst2.sort(reverse=True)
print(lst2)
# 忽略大小写进行比较
lst2.sort(key=str.lower)
print(lst2)
# 忽略大小写，降序
lst2.sort(key=str.lower,reverse=True)
print(lst2)