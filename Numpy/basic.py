import numpy as np

### save array
# np.save(path, array)

# ### array[0,:]
# a = np.random.rand(22,2)
# print(a)
# b = a[:, 0]
# print(b)

# ### array+标量
# a[:,0] = a[:,0]+10
# print(a)

### a[bool 矩阵]
a = np.random.rand(22,2)
a_bool = np.ones((22,), dtype=bool)
a_bool[2:12] = False 
print(a)
print(a[a>0.2])
print(a[a_bool])