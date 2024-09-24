# 考试成绩的问题：提示用户输入成绩，判断是属于哪个水平，
# 将结果打印到控制台。60以下不及格，60分以上为及格，
# 70分至80分为合格，80分至90分为良好，
# 90分以上为优秀。

perf=eval(input('请输入您的成绩:'))

if perf<60:
    print('不及格')
elif 0<=perf<70:
    print('及格')
elif 70<=perf<80:
    print('合格')
elif 80<=perf<90:
    print('良好')
else:
    print('优秀')
