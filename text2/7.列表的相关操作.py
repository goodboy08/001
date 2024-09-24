'''
列表的相关操作方法
    Ist.append(x)
        在列表Ist最后增加一个元素
    Ist.insert(index,x)
        在列表中第index位置增加一个元素
    Ist.clear()
        清除列表lst中所有元素
    Ist.pop(index)
        将列表Ist中第index位置的元素取出,并从列表中将其删除
    Ist.remove(x)
        将列表Ist中出现的第一个元素x删除
    Ist.reverse(x)
        将列表lst中的元素反转
    Ist.copy()
        拷贝列表lst中的所有元素,生成一个新的列表
'''

lst=['hello','world','python']
print('原列表:',lst)
# 原列表: ['hello', 'world', 'python']

# 新增元素
lst.append('增加')
print('增加元素之后:',lst)
# 增加元素之后: ['hello', 'world', 'python', '增加']

# 使用insert(index,x)在指定的位置上插入元素
lst.insert(1,'插入')
print('在插入元素后:',lst)
# 在插入元素后: ['hello', '插入', 'world', 'python', '增加']

# 列表元素的删除操作
lst.remove('world')
print('删除元素之后的列表:',lst)
# 删除元素之后的列表: ['hello', '插入', 'python', '增加']

# 使用pop(index)根据索引移出元素，先净元素取出，再将元素删除
print(lst.pop(2))   # 列表中python的索引为：2
print(lst)   # ['hello', '插入', '增加']

# 清除列表中的所有元素clear()
lst.clear()
print(lst)   # []

# 列表反向
lst2=['hello','python']
lst2.reverse()
print(lst2)

# 列表的拷贝,将产生一个新的列表对象
new_lst=lst2.copy()
print(new_lst,id(new_lst))
print(lst2,id(lst2))

# 列表元素的修改
# 根据索引进行修改元素
lst2[0]='oh'
print(lst2)