a = input('请输入一个八进制数:')
b = int(a, 8)
print('%d 的十进制为：%d' % (int(a), b))


a = input('请输入一个八进制数:')         #这里面的a是一个字符串，必须在后面转化为整形
sum = 0
for i in range(len(a)-1,-1,-1):
	sum += int(a[0])*(8**i)
print('%d 的十进制为：%d' % (int(a), sum))