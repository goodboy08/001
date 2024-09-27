# ·实战二
# -题目：模拟京东购物流程
# -需求：从键盘录入5个商品信息(1001手机)添加到商品列表中
    # ,展示商品信息，提示用户选择商品，用户选中的商品添加到购
    # 物车中（购物车中的商品要逆序），用户选中的商品不存在需要
    # 有相应提示

# 创建一个列表，用于存储入库的商品信息
lst=[]
for i in range(5):
    goods=input('请输入商品和编号和商品的名称进行商品入库，每次只能输入一件商品:')
    lst.append(goods)
# 输出所有的商品信息
for item in lst:
    print(item)

# 创建一个空列表，用于存储购物车中的商品
cart=[]
while True:
    flag=False  # 代表没有商品的情况
    num=input('请输入要购买的商品编号:')
    # 遍历商品列表，查询一下要购买的商品是否存在
    for item in lst:
        if num==item[0:4]:
            flag=True   # 代表商品已找到
            cart.append(item)   # 添加到购物车列表
            print('商品已成功添加到购物车')
            break  # 退出的是for循环
    if not flag and num!='q':  # flag==False
        print('该商品不存在!')
    if num=='q':
        break  # 退出的是while循环

print('----------------------------------')
print('您购物车里已选择的商品为:')
# 反向
cart.reverse()
for j in cart:
    print(j)
