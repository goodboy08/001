num1=eval(input('请输入第一个数:'))
operator=input('输入想要的运算(+-*/):')
num2=eval(input('请输入第二个数:'))

if operator=='+' :
    print(f'{num1}{operator}{num2}={num1+num2}')
elif operator=='-':
    print(f'{num1}{operator}{num2}={num1-num2}')
elif operator=='*':
    print(f'{num1}{operator}{num2}={num1*num2}')
elif operator=='/':
    print(f'{num1}{operator}{num2}={num1/num2}')
else:
    print('你的输入有误，无法运算！')