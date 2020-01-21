# method 1        通过在列表的前方插入数据
list = []
n = input('请输入一个数字：')
while True:
    list.insert(0, int(n))
    n = input('数字已存储至链表，请再输入一个数字：')
    if n == '':
        break
print(list)



# method 2     通过list.reverse()来实现列表的逆序排列
list = []
n = input('请输入一个数字：')
while True:
    list.append(int(n))
    n = input('数字已存储至链表，请再输入一个数字：')
    if n == '':
        break
list.reverse()
print(list)
