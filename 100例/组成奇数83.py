#不太懂这个结论是哪里来的

count = 0
for i in range(1, 9):
    if i == 1:
        # 当为一位数时，奇数个数为4个
        count += 4
    elif i == 2:
        # 当为两位数时，奇数个数为7*4个
        count += 7 * 4
    else:
        # 当为三位数时，奇数有7*8*4个，
        # 当为四位数时，奇数有7*8*8*4个，
        # 得出结论，当为三位数以上时奇数个数为7*(8**(i-2))*4个
        count += 7 * (8 ** (i - 2)) * 4
print(count)
