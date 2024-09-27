# ·实战四
# -题目：模拟手机通迅录
# -需求：从键盘录入5位好友的姓名和电话，由于通讯录是无序的
# 所以可以使用集合来实现

# 创建一个空集合
phones=set()
# 录入5位好友的姓名和手机号
for i in range(5):
    info=input('请输入第'+str(i)+'位好友的姓名与手机号码:')
    # 添加到集合中
    phones.add(info)

# 遍历集合
for item in phones:
    print(item)