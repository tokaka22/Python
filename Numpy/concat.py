'''
https://blog.csdn.net/qq_39516859/article/details/80666070
'''

import numpy as np

a = np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])

print(a.shape)

a = np.array([1,2,3])
print(a.shape)

b = np.array([4,5,6])
ab = np.concatenate((a,b),axis=-1) # 好像不能像vstack纵向，axis=1就越界
ab = np.vstack((a,b))
print(ab)