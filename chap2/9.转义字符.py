# \n 换行符
# \t 水平制表位，用于横向跳到下一行
# \" 一个双引号
# \' 一个单引号
# \\ 一个反斜杠
print('北京')
print('欢迎你')

print('-------------')
print('北京\n欢迎你')  # 遇到\n即换行，可连续换行
print('北\n京\n欢\n迎\n你')
print('-------------')
print('北京\t欢迎你')
print('hellooooooo')
print('-------------')
print('老师说:\'好好学习，天天向上\'')
print('老师说:\"好好学习，天天向上\"')

# 在字符串界定符前加上r或R，转义字符失效，将原样输出
print(r'北\n京\n欢\n迎\n你') # 北\n京\n欢\n迎\n你
print(R'北\n京\n欢\n迎\n你')



# 北京
# 欢迎你       
# -------------
# 北京
# 欢迎你       
# 北
# 京
# 欢
# 迎
# 你
# -------------
# 北京    欢迎你
# hellooooooo
# -------------
# 老师说:'好好学习，天天向上'
# 老师说:"好好学习，天天向上"
# 北\n京\n欢\n迎\n你
# 北\n京\n欢\n迎\n你