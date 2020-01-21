'''
import random
print('生成一个随机数: %s' % random.uniform(0,100))
print('生成随机整数：%s' % random.randint(0,100))

# random.uniform() 生成一个随机数
# random.randint() 生成随机整数
'''

import numpy as np

list_1 = np.random.randint(0, 50, (3, 3))
list_2 = np.random.randint(0, 50, (3, 3))
new_list = [[], [], []]
print(list_1, list_2, sep='\n     +\n')
print('     =')
for i in range(len(list_1)):
    for j in range(len(list_1[i])):
        new_list[i].append(list_1[i][j] + list_2[i][j])
print(new_list)
