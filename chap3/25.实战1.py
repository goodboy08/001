# 实战一
# -题目：输入一个年份，判断是否是闰年
# -需求：从键盘获取一个四位的整数年份，判断其是否是闰年。闰
# 年的判断条件为：能被4整除但不能被100整除，或者能被400整除
# -运行效果图

year=eval(input('请输入一个四位的年份：'))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,'年是闰年')
# elif year%400==0:
#     print(year,'是闰年')
else:
    print(year,'年是平年')

