n = 1
m = int(input('请输入一个奇数：'))
while True:
    i = int('9' * n)
    if i % m == 0:
        print('%d 可以被 %d 整除,里面含有 %d 个9' % (m, i, n))
        break
    n += 1
