n = 1
while n <= 7:
	m = int(input('请输入一个1~50的整数：'))
	if 1 <= m <= 50:
		print('*' * m)    #表示有m个*被输出
		n += 1
	else:
		print('输入的数字有误，请重新输入！')