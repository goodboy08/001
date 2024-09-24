# 已知字符串 test = "aAsmr3idd4bgs7Dlsf9eAF",
# 将字符串中的数字取出，生成一个新的字符串

# 要想提取数字字符，我们就需要遍历字符串
test = 'aAsmr3idd4bgs7Dlsf9eAF'

#定义一个变量用于接收数字字符
result=''
for i in test:
    # 如果s在后面的字符串中说明这个字符是数字字符
    if i in '0123456789':
        # 把数字字符拼接到结果中
        result+=i
# 打印结果 
print(result)