dict = {}
for i in range(2):
    stu = input('请输入学生姓名：')
    socre_1 = int(input('请输入语文成绩：'))
    socre_2 = int(input('请输入数学成绩：'))
    socre_3 = int(input('请输入英语成绩：'))
    print('-------------')
    list_i = [socre_1, socre_2, socre_3]
    dict[stu] = list_i
for i in dict:
    print('%s 的语文成绩为： %d ；数学成绩为 %d ；英语成绩为： %d' % (i, dict[i][0], dict[i][1], dict[i][2]))
print(list_i)