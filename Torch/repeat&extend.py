'''
https://blog.csdn.net/guofei_fly/article/details/104467138
'''

import torch
a = torch.tensor([[1, 0, 2]])
b = a.expand(2, -1)   # 第一个维度为升维，第二个维度保持原阳
# b为   tensor([[1, 0, 2],  [1, 0, 2]])
print(a.shape)
print(b.shape)
print(a)
print(b)

a = torch.tensor([[1], [0], [2]])
b = a.expand(-1, 2)   # 保持第一个维度，第二个维度只有一个元素，可扩展
# b为  tensor([[1, 1],
#              [0, 0],
#              [2, 2]])


import torch
a = torch.tensor([1, 0, 2])
b = a.repeat(3,2)  # 在轴0上复制3份，在轴1上复制2份
# b为 tensor([[1, 0, 2, 1, 0, 2],
#        [1, 0, 2, 1, 0, 2],
#        [1, 0, 2, 1, 0, 2]])
