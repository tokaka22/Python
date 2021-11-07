"""
非线性方程多个解 root的情况
"""

import numpy as np
from scipy.optimize import fsolve
import math

'''
lambda t: (-0.0066197 + (1/4)*math.exp(-17/4/t)/(math.pi*t*((1/4)/(math.pi*t) + math.exp(-1/t)/(math.pi*t) + math.exp(-2/t)/(math.pi*t) + math.exp(-4/t)/(math.pi*t) + 2*math.exp(-5/t)/(math.pi*t) + math.exp(-8/t)/(math.pi*t) + math.exp(-9/t)/(math.pi*t) + 2*math.exp(-10/t)/(math.pi*t) + 2*math.exp(-13/t)/(math.pi*t) + math.exp(-18/t)/(math.pi*t) + math.exp(-1/2/t)/(math.pi*t) + 2*math.exp(-5/2/t)/(math.pi*t) + math.exp(-9/2/t)/(math.pi*t) + 2*math.exp(-13/2/t)/(math.pi*t) + 2*math.exp(-17/2/t)/(math.pi*t) + 3*math.exp(-25/2/t)/(math.pi*t) + 2*math.exp(-29/2/t)/(math.pi*t) + 2*math.exp(-37/2/t)/(math.pi*t) + math.exp(-49/2/t)/(math.pi*t) + math.exp(-1/4/t)/(math.pi*t) + 2*math.exp(-5/4/t)/(math.pi*t) + math.exp(-9/4/t)/(math.pi*t) + 2*math.exp(-13/4/t)/(math.pi*t) + 2*math.exp(-17/4/t)/(math.pi*t) + 3*math.exp(-25/4/t)/(math.pi*t) + 2*math.exp(-29/4/t)/(math.pi*t) + 2*math.exp(-37/4/t)/(math.pi*t) + 2*math.exp(-41/4/t)/(math.pi*t) + 2*math.exp(-45/4/t)/(math.pi*t) + math.exp(-49/4/t)/(math.pi*t) + 2*math.exp(-53/4/t)/(math.pi*t) + 2*math.exp(-61/4/t)/(math.pi*t) + 2*math.exp(-65/4/t)/(math.pi*t) + 2*math.exp(-85/4/t)/(math.pi*t))))

i 289, j 755, res [3.19015299]
'''
# f = lambda x : x * np.cos(x-4) 解多解
f = lambda t: (-0.0066197 + (1/4)*math.exp(-17/4/t)/(math.pi*t*((1/4)/(math.pi*t) + math.exp(-1/t)/(math.pi*t) + math.exp(-2/t)/(math.pi*t) + math.exp(-4/t)/(math.pi*t) + 2*math.exp(-5/t)/(math.pi*t) + math.exp(-8/t)/(math.pi*t) + math.exp(-9/t)/(math.pi*t) + 2*math.exp(-10/t)/(math.pi*t) + 2*math.exp(-13/t)/(math.pi*t) + math.exp(-18/t)/(math.pi*t) + math.exp(-1/2/t)/(math.pi*t) + 2*math.exp(-5/2/t)/(math.pi*t) + math.exp(-9/2/t)/(math.pi*t) + 2*math.exp(-13/2/t)/(math.pi*t) + 2*math.exp(-17/2/t)/(math.pi*t) + 3*math.exp(-25/2/t)/(math.pi*t) + 2*math.exp(-29/2/t)/(math.pi*t) + 2*math.exp(-37/2/t)/(math.pi*t) + math.exp(-49/2/t)/(math.pi*t) + math.exp(-1/4/t)/(math.pi*t) + 2*math.exp(-5/4/t)/(math.pi*t) + math.exp(-9/4/t)/(math.pi*t) + 2*math.exp(-13/4/t)/(math.pi*t) + 2*math.exp(-17/4/t)/(math.pi*t) + 3*math.exp(-25/4/t)/(math.pi*t) + 2*math.exp(-29/4/t)/(math.pi*t) + 2*math.exp(-37/4/t)/(math.pi*t) + 2*math.exp(-41/4/t)/(math.pi*t) + 2*math.exp(-45/4/t)/(math.pi*t) + math.exp(-49/4/t)/(math.pi*t) + 2*math.exp(-53/4/t)/(math.pi*t) + 2*math.exp(-61/4/t)/(math.pi*t) + 2*math.exp(-65/4/t)/(math.pi*t) + 2*math.exp(-85/4/t)/(math.pi*t))))
f = lambda t: (0.25*math.exp(-61/4/t)/(math.pi*t*((1/4)/(math.pi*t) + math.exp(-1/t)/(math.pi*t) + math.exp(-2/t)/(math.pi*t) + math.exp(-4/t)/(math.pi*t) + 2*math.exp(-5/t)/(math.pi*t) + math.exp(-8/t)/(math.pi*t) + math.exp(-9/t)/(math.pi*t) + 2*math.exp(-10/t)/(math.pi*t) + 2*math.exp(-13/t)/(math.pi*t) + math.exp(-18/t)/(math.pi*t) + math.exp(-1/2/t)/(math.pi*t) + 2*math.exp(-5/2/t)/(math.pi*t) + math.exp(-9/2/t)/(math.pi*t) + 2*math.exp(-13/2/t)/(math.pi*t) + 2*math.exp(-17/2/t)/(math.pi*t) + 3*math.exp(-25/2/t)/(math.pi*t) + 2*math.exp(-29/2/t)/(math.pi*t) + 2*math.exp(-37/2/t)/(math.pi*t) + math.exp(-49/2/t)/(math.pi*t) + math.exp(-1/4/t)/(math.pi*t) + 2*math.exp(-5/4/t)/(math.pi*t) + math.exp(-9/4/t)/(math.pi*t) + 2*math.exp(-13/4/t)/(math.pi*t) + 2*math.exp(-17/4/t)/(math.pi*t) + 3*math.exp(-25/4/t)/(math.pi*t) + 2*math.exp(-29/4/t)/(math.pi*t) + 2*math.exp(-37/4/t)/(math.pi*t) + 2*math.exp(-41/4/t)/(math.pi*t) + 2*math.exp(-45/4/t)/(math.pi*t) + math.exp(-49/4/t)/(math.pi*t) + 2*math.exp(-53/4/t)/(math.pi*t) + 2*math.exp(-61/4/t)/(math.pi*t) + 2*math.exp(-65/4/t)/(math.pi*t) + 2*math.exp(-85/4/t)/(math.pi*t))))
x = np.array([1,10])
vector = np.vectorize(fsolve)
print(vector(f,x))


'''
write by self: it is slow
by Jaan Kiusalaas:
'''
# import math

# def rootsearch(f,a,b,dx):
#     x1 = a; f1 = f(a)
#     x2 = a + dx; f2 = f(x2)
#     while f1*f2 > 0.0:
#         if x1 >= b:
#             return None,None
#         x1 = x2; f1 = f2
#         x2 = x1 + dx; f2 = f(x2)
#     return x1,x2

# def bisect(f,x1,x2,switch=0,epsilon=1.0e-9):
#     f1 = f(x1)
#     if f1 == 0.0:
#         return x1
#     f2 = f(x2)
#     if f2 == 0.0:
#         return x2
#     if f1*f2 > 0.0:
#         print('Root is not bracketed')
#         return None
#     n = int(math.ceil(math.log(abs(x2 - x1)/epsilon)/math.log(2.0)))
#     for i in range(n):
#         x3 = 0.5*(x1 + x2); f3 = f(x3)
#         if (switch == 1) and (abs(f3) >abs(f1)) and (abs(f3) > abs(f2)):
#             return None
#         if f3 == 0.0:
#             return x3
#         if f2*f3 < 0.0:
#             x1 = x3
#             f1 = f3
#         else:
#             x2 =x3
#             f2 = f3
#     return (x1 + x2)/2.0

# def roots(f, a, b, eps=1e-6):
#     print ('The roots on the interval [%f, %f] are:' % (a,b))
#     while 1:
#         x1,x2 = rootsearch(f,a,b,eps)
#         if x1 != None:
#             a = x2
#             root = bisect(f,x1,x2,1)
#             if root != None:
#                 pass
#                 print (round(root,-int(math.log(eps, 10))))
#         else:
#             print ('\nDone')
#             break

# f=lambda t: (-0.0066197 + (1/4)*math.exp(-17/4/t)/(math.pi*t*((1/4)/(math.pi*t) + math.exp(-1/t)/(math.pi*t) + math.exp(-2/t)/(math.pi*t) + math.exp(-4/t)/(math.pi*t) + 2*math.exp(-5/t)/(math.pi*t) + math.exp(-8/t)/(math.pi*t) + math.exp(-9/t)/(math.pi*t) + 2*math.exp(-10/t)/(math.pi*t) + 2*math.exp(-13/t)/(math.pi*t) + math.exp(-18/t)/(math.pi*t) + math.exp(-1/2/t)/(math.pi*t) + 2*math.exp(-5/2/t)/(math.pi*t) + math.exp(-9/2/t)/(math.pi*t) + 2*math.exp(-13/2/t)/(math.pi*t) + 2*math.exp(-17/2/t)/(math.pi*t) + 3*math.exp(-25/2/t)/(math.pi*t) + 2*math.exp(-29/2/t)/(math.pi*t) + 2*math.exp(-37/2/t)/(math.pi*t) + math.exp(-49/2/t)/(math.pi*t) + math.exp(-1/4/t)/(math.pi*t) + 2*math.exp(-5/4/t)/(math.pi*t) + math.exp(-9/4/t)/(math.pi*t) + 2*math.exp(-13/4/t)/(math.pi*t) + 2*math.exp(-17/4/t)/(math.pi*t) + 3*math.exp(-25/4/t)/(math.pi*t) + 2*math.exp(-29/4/t)/(math.pi*t) + 2*math.exp(-37/4/t)/(math.pi*t) + 2*math.exp(-41/4/t)/(math.pi*t) + 2*math.exp(-45/4/t)/(math.pi*t) + math.exp(-49/4/t)/(math.pi*t) + 2*math.exp(-53/4/t)/(math.pi*t) + 2*math.exp(-61/4/t)/(math.pi*t) + 2*math.exp(-65/4/t)/(math.pi*t) + 2*math.exp(-85/4/t)/(math.pi*t))))
# roots(f, 7, 9)