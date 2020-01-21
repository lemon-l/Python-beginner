# 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），
# 凡报到3的人退出圈子，问最后留下的是原来第几号的那位。



n = int(input('请输入人数：'))
list = []
count = 0
for i in range(1, n + 1):
    list.append(i)
while True:
    if len(list) == 1:
        print(list)
        break
    else:
        count += 1
        pop = list[0]
        list.pop(0)
        if count == 3:
            count = 0
            continue
        else:
            list.append(pop)
    print(list)
