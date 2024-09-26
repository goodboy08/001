
for i in range(1,10):   # i为1到9中的每个数字
    for j in range(1,i+1):  # j为1到9中的每个数字：--range(1,2),不包含2  --range(1,10),不包含10
        print('%d*%d=%d' % (j,i,j*i),end='\t')
    print('')


