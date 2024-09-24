# 现有字符串 msg = "hel@#$lo pyt \nhon ni\t hao%$" ，
# 去掉所有不是英文字母的字符，
# 打印结果："请理以后的结果为：hellopythonnihao"


# 1.因为要处理每个字符，所以需要遍历字符
# 2.如果判断每一个字符是不是英文字母，字符串本身就有方法可以判断 isalpha 方法
# 3.把英文单词拼接到一起就是我们要的

msg = "hel@#$lo pyt \nhon ni\t hao%$" 
# 定义一个空字符。用于保存结果
result=''
# 循环遍历字符
for i in msg:
    # 判断当前字符是否是字母
    if i.isalpha():
        # 把字母添加到结果中
        result+=i
# 打印结果
print(result)
