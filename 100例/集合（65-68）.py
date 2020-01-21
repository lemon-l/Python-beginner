# 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面
# 的m个数

'''
思路：就是把后面的数先去掉，然后再在原本的list里面插入去掉的数
'''

n = [0,10,20,30,40,50,60,70]
m = int(input('输入你要倒的顺序: '))
for i in range(m):
    n.insert(0,n.pop(-1))
print(n)


# 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组
'''
难点：找到最大值和最小值对应的索引，并赋值
注意：排序sorted默认是升序，担当设置reverse = True的时候会降序排列 
'''
list = [333,65,98,69,52,45,78, 55555,42,2748]
print(sorted(list,reverse=True))
Max = max(list)
Min = min(list)
list[list.index(Max)],list[0] = list[0],Max
list[list.index(Min)],list[-1] = list[-1],Min
print(list)
