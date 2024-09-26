answer=input('请问，您喝酒了吗？y/n')    # 嵌套由外至内编写
if answer=='y':  # 代表喝酒了
    proof=eval(input('请输入酒精含量：'))   # 嵌套一个，多选一
    if proof<20:
        print('构不成酒驾，你可以走了')
    elif proof<80:
        print('已构成酒驾标准，请不要开车')
    else:
        print('已达到醉驾标准，请千万不要开车')
else:  # 代表没有喝酒
    print('你走吧，没你啥事儿')
