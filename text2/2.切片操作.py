s='HelloWorld'
s1=s[0:5:1]  # 索引从0开始，到5结束，步长为1
print(s1)

# 省略开始位置start,默认从0开始
print(s[:5:1])

# 省略开始位置start,省略步长step
print(s[:5])

# 省略结束位置
print(s[0::1])

# 省略结束位置和步长
print(s[5:])

# 更换一下步长
print(s[0:5:2])

# 省略开始位置和结束位置，只写步长
print(s[::2])

# 步长可以为负数
print(s[::-1])

