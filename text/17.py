# 定义函数findall,要求返回符合要求的所有位置的起始下标，如字符串"helloworldhellopythonhelloc++hellojava"
#需要找出里面所有'hello'的位置，返回的格式是一个元组，即:（0，10，21，29）

# src：原始字符串   dst:要查找的字符串
def findall(src,dst):
    # 获取字符长度，用去截取字符
    lg=len(dst)
    # 保存查找的下标
    res=[]
    # 遍历字符通过下标
    for index in range(len(src)):
        # 截取与dst相同的字符，如果相等说明，位置ok
        if src[index:index+lg]==dst:
            # 把当前位置添加到结果集中
            res.append(index)
    
    # 把结果转化成元组返回
    return tuple(res)

s='helloworldhellopythonhelloc++hellojava'
i='hello'
print(findall(s,i))


