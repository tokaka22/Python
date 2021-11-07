
import numpy as np
import torch

# torch.rand(2, 3) # (2,3)为size，rand随机初始为0-1的数

# torch.randn(2, 3) # 均值为0，方差1的正态分布

# torch.randint(3, 10, (2, 2)) # low high size

# ### 改变类型
# tensor.double()

### equal
a = torch.tensor([0.0])
print(a.shape)
print(a == 0)
print(torch.eq(a, 0))
if not(torch.eq(a, 0))&(a <= 10000):
    print('ok')
print('g')

b = torch.tensor(0.0)
print(b.shape)
print(b)
print(b == 0)
if b==0:
    print("b okoko")

# ### Returns the value of this tensor as a standard Python number.
# # 标量
# x = torch.tensor([1.0])
# print(x.item())

### sum

# ### 由range初始向量，而后reshape一个矩阵
# '''
# 1.
#     torch.range(start=1, end=6) 的结果是会包含end的，
#     而torch.arange(start=1, end=6)的结果并不包含end。
# 2.
#     两者创建的tensor的类型也不一样。
# '''
# y = torch.range(1,6)
# print(y)
# print(y.dtype)

# z = torch.arange(1,6)
# print(z)
# print(z.dtype)

# x = torch.reshape(y,(2,3))
# print(x)

# ### bool mask
# x = torch.reshape(torch.range(1,50),(5,10))
# print(x)
# mask = x>15
# print(mask)
# print(x[mask])

# ### 初始化1维零向量
# print(torch.zeros(22))