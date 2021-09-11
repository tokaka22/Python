'''
将输入input张量每个元素的夹紧到区间 [min,max]，并返回结果到一个新张量。
'''
import torch

a = torch.randn(4)
print(a)

b = torch.clamp(a, min=-0.5, max=0.5)
print(b)