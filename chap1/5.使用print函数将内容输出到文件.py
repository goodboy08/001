fp=open("note.txt", "w") # 打开文件 w-->write
print("Hello Python!!!",file=fp)  # 输出到文件中
fp.close()  # 关闭文件