d = 1,2,3
print(type(d))
#把一个元祖的值付给三个变量
a,b,c = d
print(a,b,c)



#函数：（注意里面全是字符串，不是也应该转换为str（），not int）
#     1.必须参数；
#     2.关键字参数；
#     3.默认参数
#      *（直接在函数def functionName(x,y = a,z = b),赋值的参数就是默认参数
#         调用时如果没有按照函数本身的参数顺序来会报错，此时可以利用关键字参数
#         来改正。）
def add(x,y):
    result = x + y
    return result
#关键字参数
c = add(y=3,x=2)
print(c)
#必须参数
d = add(2,3)
print(d)

