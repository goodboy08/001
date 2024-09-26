# 语法结构
# if 表达式:
#   语句块
# else:
#   语句块


number=eval(input('请输入您的六位中奖号码:'))

# if number==987654:
#     print('恭喜您中奖了')
# else:
#     print('您未中本期大奖')

# 还可以使用条件表达式简化
result='恭喜您中大奖了' if number==987654 else '您未中本期大奖'
print(result)


