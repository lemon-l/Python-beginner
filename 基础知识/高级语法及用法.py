#枚举(意义重在标签)
#不支持大小的比较，但支持等值的比较
#枚举类型、枚举的名字、枚举的值
from enum import Enum

class VIP(Enum):
    yellow = 1       #前面的标签务必不能重复，但后面对应的值可以，
    green = 2        #当后面对应的值相同时，用for循环遍历只会出现一种标签，重复的另为一个会被忽略
    black = 3
    red = 4

print(VIP.black.value)     #对应的数值
print(VIP.black.name)      #对应的标签
print(VIP.black)           #输出原来的
print(VIP['black'])        #同上

'''
for i in VIP:
    print(i)
'''

for v in VIP.__members__:
    print(v)                 #打印出重复的标签

result = VIP.green == VIP.black
print(result)

'''
class common():
    yellow = 1
a = 1                       #相当于类型转换
print(VIP(a))
'''
