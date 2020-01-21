L = []
for i in range(1, 11):
    list = []
    for j in range(1, i + 1):
        list.append(0)
    list[0] = 1
    list[-1] = 1
    L.append(list)
    if len(list) > 2:
        for k in range(len(list)):
            if 0 < k < len(list) - 1:
                list[k] = L[-2][k - 1] + L[-2][k]
for a in L:
    for b in a:
        print(b, end=' ')
    print()
