
import numpy as np
a = np.array([[1,2],
                 [3,4]])
b = np.array([[5,6],
                 [7,8]])

print(a*b) # 对应元素相乘
print(a.dot(b)) # 内积

print(np.sum(a*b))