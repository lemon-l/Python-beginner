#【Python 练习实例89】某个公司采用公用电话传递数据，数据是四位的整数，
# 在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10
# 的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换

# method 1: 将数据转换为字符串来计算
num = input('输入要加密的数： ')
str_num = ''
for i in range(4):
    str_num += str(int((int(num[i]) + 5) % 10))
i,j,k,l = str_num[3],str_num[2],str_num[1],str_num[0]
str_num = i+j+k+l
print('加密后的数据为：%s' % str_num)


# method 2: 将数据存储到列表，然后分别执行加密规则
num = int(input('请输入要加密的数据：'))
list_num = []
# 分别将数据的千位，百位，十位，个位数存入列表中
list_num.append(int(num / 1000))
list_num.append(int((num % 1000) / 100))
list_num.append(int((num % 100) /10))
list_num.append(int(num % 10))
# 对各个位数分别执行加密规则
for i in range(4):
	list_num[i] = (list_num[i] + 5) % 10
#将第一位和第四位交换，第二位和第三位交换，即[1,2,3,4] -> [4,3,2,1]，也就是倒序输出即可
print('加密后的数据为：', end='')
for i in range(-1,-5,-1):
	print(list_num[i], end='')