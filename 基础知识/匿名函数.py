'''
filter（function，list） 过滤
（函数式编程），我们熟悉的都是命令式编程
lambda 算子

装饰器

*对修改是封闭的，对扩展是开放的
Unix 时间戳
*args  -------------  可变参数
**kw(key word) -------------  关键字参数
'''
from functools import reduce 
import time 

#匿名函数：
def add(x,y):
    return x+y

print(add(1,2))

f= lambda x,y: x+y
print(f(1,2))

#python 中的三木表达式
x = 1   
y = 3
r = x if x > y else y
print(r)

#map(function，list)函数
list_x = [1,2,3,4,5,6,7,8,9]
list_y = [1,2,3,4,5,6,7]

'''
第一种表达方式： 
def square(x):
return x*x
r = map(square, list_x)
'''

'''
第二种表达方式：
r = map(lambda x: x*x, list_x)
'''
r = map(lambda x,y: x*x + y, list_x, list_y)    #的道德的结果数量取决于较少的一个参数

print(list(r))

#reduce()
r = reduce(lambda x, y: x+y, list_x)      #高度抽象
print(r)


#filter()函数
list_x = [1,0,1,0,0,0,1,0,1]

r = filter(lambda x: True if x else False, list_x)
print(list(r))

#装饰器(不改变函数的具体内容)
def decorator(func):
    def wrapper(*args, **kw):    #（*args)在这里表示可变的参数；
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorator
def f1(func_name1,func_name2,func_name3):
    print('今天是个好日子' + func_name1 + func_name2 + func_name3)

f1(', 李蒙', ', 你真棒',' , 高数你一定不会挂科')


