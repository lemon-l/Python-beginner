import numpy as np
from math import *

#十六进制文本输入
bf1=open("test.txt","rb")
c=bf1.read()

bf1.close()
c_bin=bin(int(c,16)).lstrip('0b')

# 序列长度
length=len(c_bin)

#子矩阵个数j_num
num=length/(32*32)
N=int(num)

if(N > 0):
    # 构造矩阵
    def build_matrix(n):
        a = np.ones((32,32))
        for i in range(32):
            for j in range(32):
                a[i][j] = int(c_bin[n])
                n += 1 
        return a

    #求矩阵的秩
    def Get_rank(ls):
        A=np.array(ls)
        return (np.linalg.matrix_rank(A))

    # 上不完全伽马函数
    def upper_incomplete_gamma(a,x,d=0,iterations=100):
        if d == iterations:
            if ((d % 2) == 1):
                return 1.0 
            else:
                m = d/2
                return x + (m-a)
        if d == 0:
            result = ((x**a) * (e**(-x)))/upper_incomplete_gamma(a,x,d=d+1)
            return result
        elif ((d % 2) == 1):
            m = 1.0+((d-1.0)/2.0)
            return x+ ((m-a)/(upper_incomplete_gamma(a,x,d=d+1)))
        else:
            m = d/2
            return 1+(m/(upper_incomplete_gamma(a,x,d=d+1)))

    # 不完全伽玛函数
    def igamc(a,x):
        return upper_incomplete_gamma(a,x)/gamma(a)

    n = 0
    FM, FM_1 = 0, 0
    for i in range(N):
        a = Get_rank(build_matrix(n))
        n += 1025
        if(a == 32):
            FM += 1
        elif(a == 31):
            FM_1 += 1
    v = (FM-0.2888*N)*(FM-0.2888*N)/(0.2888*N)+(FM_1-0.5776*N)*(FM_1-0.5776*N)/(0.5776*N)+(N-FM-FM_1-0.1336*N)*(N-FM-FM_1-0.1336*N)/(0.1336*N)
    result = igamc(1,v/2)

    a = 0.01
    if(result <= 0.01):
        print("This is a random sequence")
    else:
        print("This is not a random sequence")
else:
    print("This sequence can't build one Matrix,please give more!")
    







