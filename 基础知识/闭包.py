#python 中一切皆对象
#闭包 = 函数 + 环境变量

'''
def curve_pre():
    a=20              #环境变量
    def curve(x):
       return a**x
    return curve

a = 10         #不起作用
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))
'''

'''
def f1():
    a = 20
    def f2():
        a = 10      #局部变量，不影响外面。由于此事并未饮用外面环境变量里面的a，故算不上是闭包
        print(a)
    print(a)
    f2()
    print(a)

f1()
'''
#方法一：
origin = 0
def go(step):
    global origin            #用global声明全局变量
    new_pos = origin + step
    origin = new_pos
    return new_pos

print(go(2))
print(go(3))
print(go(6))

#方法二：
def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go 

tourist = factory(origin)
print(tourist(2))
print(tourist(3))
print(tourist(6))