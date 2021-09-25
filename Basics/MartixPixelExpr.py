import torch
import numpy as np

y1=['yes','n1','n2','n3','yes1']
y1 = np.array(y1)
print(type(y1[2]))

a = np.empty([2,2], dtype=object)
a[1,1] = "abc"
print(type(a[1,1]))

b = torch.ones(2,3, dtype=int)
print(b[1,1])

# list
