from decimal import InvalidContext
import numpy as np
import pandas as pd
import os
import sympy as sy
import math
import scipy
from sympy.utilities.lambdify import lambdify, implemented_function
from sympy.utilities.lambdify import lambdastr
from scipy.optimize import fsolve
from scipy.optimize import minimize_scalar
import warnings
import time
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
import concurrent.futures
import multiprocessing
import torch
import matplotlib.pyplot as plt

class Symbol():
    def __init__(self):
        self.size = 15
        self.delta = (self.size-1)/2
        pass

    ### 卷积函数
    def conv2d(self, Img, G, gt_value):
        temp = 0
        for i in range(self.size):
            for j in range(self.size):
                i1 = self.size-i-1
                j1 = self.size-j-1
                # print(A1[i1, j1])
                temp = temp + Img[i,j]*G[i1, j1]
        res = temp - gt_value
        return res

    def conv2dMul(self, Img, GI, gt_value, M):
        M = Img.multiply_elementwise(GI)
        res = sy.ones(1,self.size)*M*sy.ones(self.size,1)
        ans = res[0,0] - gt_value
        return ans

    def symbolMatrix(self):
        ### 求得Gxy filter的符号表示
        XG = sy.MatrixSymbol("XG", self.size, self.size)
        G = sy.Matrix(XG)

        x, y = sy.symbols('x, y')
        t = sy.symbols('t') 
        a = sy.symbols('a')

        Gxy = (1/(4*sy.pi*t*a)) * sy.exp((-1)*(x**2 + y**2)/(4*t*a))

        iArray = np.arange(-self.delta,self.delta+1)
        jArray = np.arange(-self.delta,self.delta+1)

        '''
        Matrix的具体位置：
        Matrix([
        [X[0, 0], X[0, 1], X[0, 2]],
        [X[1, 0], X[1, 1], X[1, 2]],
        [X[2, 0], X[2, 1], X[2, 2]]])
        '''

        for i in range(self.size):
            for j in range(self.size):
                # print(G[i,j])
                # print('{} {}'.format(i, j))
                i1 = iArray[i]
                j1 = jArray[j]
                # print('{} {}'.format(i1, j1))
                temp = Gxy.subs([(x,i1), (y,j1)])
                G[i,j] = temp
                # print(G[i,j])

        # print(G)
        G = G/(sum(G))
        # print(G)

        ### G左右上下颠倒，用作conv2d
        XGI = sy.MatrixSymbol('XGI', self.size, self.size)
        GI = sy.Matrix(XGI)
        for i in range(self.size):
            for j in range(self.size):
                i1 = self.size-i-1
                j1 = self.size-j-1
                # print(A1[i1, j1])
                GI[self.size-i-1, self.size-j-1] = G[i, j]

        m = 1
        n = 2
        assert G[m, n] == GI[self.size-m-1, self.size-n-1]

        ### 局部slice与filter对应元素相乘存储矩阵
        XM = sy.MatrixSymbol('XM', self.size, self.size)
        M = sy.Matrix(XM)

        ### 图像局部15*15 symbol表示
        XP = sy.MatrixSymbol("XP", self.size, self.size)
        P = sy.Matrix(XP)
        gt_value = sy.symbols('gtv')

        ### 方程通项
        expr = self.conv2dMul(P, GI, gt_value, M)# 卷积后的所有项之和

        return expr

def cal_t(tuple, u0_map, gt_map, gtv, expr):
    i = tuple[0] + 7
    j = tuple[1] + 7
    u0_slice = u0_map[i-7:i+8, j-7:j+8]
    # u0_slice = u0_map[i-2:i+3, j-2:j+3]
    is_all_zero = np.all((u0_slice == 0))
    if is_all_zero:
        return 

    XP = sy.MatrixSymbol("XP", 15, 15)
    gt_value = sy.symbols('gtv')
    a = sy.symbols('a')
    t = sy.symbols('t')

    temp1 = expr.subs([(XP, sy.Matrix(u0_slice)),(gt_value, gtv), (a, 1)])            
    temp2 = expr.subs([(XP, sy.Matrix(u0_slice)),(gt_value, gtv)])
    temp3 = expr.subs([(XP, sy.Matrix(u0_slice)), (gt_value, gt_map[i,j]), (a, 1)])
    F1 = eval(lambdastr(t, temp1))
    F2 = eval(lambdastr([gt_value,t], temp2))
    F3 = eval(lambdastr(t, temp3))
    flag = True
    with warnings.catch_warnings(): # 把warning当error抓住，然后应该不会报runningtime的错了，实际跑程序还有估计是其他地方的runningtime/warning错误
        warnings.filterwarnings('error')
        try:
            res0 = fsolve(F3, 7.0)
            print(f"res0: {res0}")
            res = fsolve(F1, 2.0)
            # if (res < 0) | (res > 10000):
            #     flag = False
        except:
            print("-"*30)
            print("solve False")
            flag = False
    if flag == True:
        return res
    else:
        return -100

def conv2dMul(Img, GI, gt_value, M):
    M = Img.multiply_elementwise(GI)
    res = sy.ones(1,15)*M*sy.ones(15,1)
    # res = sum(M)
    ans = res[0,0] - gt_value
    return ans

if __name__ == '__main__':
    '''
    expr好像有问题
    '''
    # expr = Symbol().symbolMatrix()
    
    gt_map = (pd.read_csv(r'matplotlib\gt_1.csv', header=None)).values
    u0_map = (pd.read_csv(r'matplotlib\u0_1.csv', header=None)).values

    H = gt_map.shape[0]
    W = gt_map.shape[1]

    # 高斯随机覆盖的情况，sum一致
    # randomArray = gaussGen(gt_map, np.sum(u0_map))
    # gt_map = randomArray

    XG = sy.MatrixSymbol("XG", 15, 15)
    G = sy.Matrix(XG)
    x, y = sy.symbols('x, y')
    t = sy.symbols('t') 
    a = sy.symbols('a')
    # Gxy = sy.exp(-1*(x**2 + y**2))/(4*a*t))/(4*sy.pi*a*t)
    Gxy = (1/(4*sy.pi*t*a)) * sy.exp((-1)*(x**2 + y**2)/(4*t*a))
    
    # print(Gxy)

    iArray = np.arange(-7,8)
    jArray = np.arange(-7,8)

    for i in range(15):
        for j in range(15):
            i1 = iArray[i]
            j1 = jArray[j]
            temp = Gxy.subs([(x,i1), (y,j1)])
            G[i,j] = temp
    
    # print(G)
    G = G/(sum(G))

    # print(G)

    ### G左右上下颠倒，用作conv2d
    XGI = sy.MatrixSymbol('XGI', 15, 15)
    GI = sy.Matrix(XGI)
    for i in range(15):
        for j in range(15):
            i1 = 15-i-1
            j1 = 15-j-1
            # print(A1[i1, j1])
            GI[15-i-1, 15-j-1] = G[i, j]

    m = 3
    n = 8
    assert G[m, n] == GI[15-m-1, 15-n-1]

    ### 局部slice与filter对应元素相乘存储矩阵
    XM = sy.MatrixSymbol('XM', 15, 15)
    M = sy.Matrix(XM)

    ### 图像局部15*15 symbol表示
    XP = sy.MatrixSymbol("XP", 15, 15)
    P = sy.Matrix(XP)
    gt_value = sy.symbols('gtv')

    ### 得到方程通项
    expr = conv2dMul(P, G, gt_value, M) # 卷积后的所有项之和
    i = 330
    j = 34
    gtv = np.linspace(0,0.004,101)
    t = np.empty_like(gtv)
    t[:] = np.NaN
    for idx, item in enumerate(gtv):
        tval = cal_t((i,j), u0_map, gt_map, item ,expr)
        if tval != -100:
            t[idx] = tval
    print(t)
    plt.plot(gtv, t)
    y1 = 0*gtv
    plt.plot(gtv, y1, 'r')
    # plt.xticks(range(-5, 5))
    # plt.yticks(range(-5, 5))
    plt.legend(loc='upper left')
    plt.show()
    print("ok")