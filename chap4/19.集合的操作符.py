a={10,20,30,40,50}
b={30,50,88,76,20}

# 交集操作
print(a&b)  # {50, 20, 30}

# 并集
print(a|b)  # {40, 10, 76, 50, 20, 88, 30}

# 差集
print(a-b)  # {40, 10}

# 补集
print(a^b)  # {10, 88, 40, 76}
