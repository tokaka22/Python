import numpy as np

### save array
# np.save(path, array)

### array[0,:]
a = np.random.rand(22,2)
print(a)
b = a[:, 0]
print(b)

### array+标量
a[:,0] = a[:,0]+10
print(a)