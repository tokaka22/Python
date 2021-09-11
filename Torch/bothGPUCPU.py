'''
model可以在cpu，gpu上同时运行，不影响autograd
'''

import torch
import torch.nn as nn

# setup
x_cuda = torch.randn(1, 1).to('cuda')
lin_cuda = nn.Linear(1, 1).to('cuda')
lin_cpu = nn.Linear(1, 1)

# workload on the GPU
out = lin_cuda(x_cuda)
# transfer to CPU
out_cpu = out.to('cpu')
# workload on CPU
out_cpu = lin_cpu(out_cpu)

# loss calculation on the CPU
loss = (out_cpu ** 2).mean()

# backward
loss.backward()

# check grads
for name, param in lin_cuda.named_parameters():
    print(name, param.grad)

for name, param in lin_cpu.named_parameters():
    print(name, param.grad)

