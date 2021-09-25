

import torch
import numpy as np
a = torch.tensor([[1., 2], [3, 4]])
print(torch.var(a, unbiased=False)) # unbiased似乎是某种样本上的方差计算纠正，没必要用
print(torch.var(a, unbiased=True))

a_np = np.array([[1, 2], [3, 4]])
print(np.var(a_np))
# unbiased=False和np.var都是1.25，故应该都用False

b = torch.randn((4,5))
print(torch.var(b, unbiased=False))
print(torch.var(b, unbiased=True))