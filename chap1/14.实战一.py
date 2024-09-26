fb=open('text.txt','w')     #打开文件
print('人生苦短,我用Python', file=fb)     #向文件写入（输出）内容
fb.close()  #关闭文件