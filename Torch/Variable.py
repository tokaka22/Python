'''
https://blog.csdn.net/Hungryof/article/details/71024114
em.......Variable已经和Tensor合并
    新版本中，torch.autograd.Variable 和 torch.Tensor 将同属一类。更确切地说，
    torch.Tensor 能够追踪日志并像旧版本的 Variable 那样运行; Variable 封装仍旧可以像以前一样工作，
    但返回的对象类型是 torch.Tensor。这意味着你的代码不再需要变量封装器。
'''


import torch
from torch.autograd import Variable
x = Variable(torch.ones(2, 2), requires_grad=True)
print(type(x))
print(x)  # notice the "Variable containing" line
'''
Variable containing:
 1  1
 1  1
[torch.FloatTensor of size 2x2]
'''
print(x.grad_fn)


y = x + 2
print(y)
'''
Variable containing:
 3  3
 3  3
[torch.FloatTensor of size 2x2]
'''
print(y.grad_fn)
'''
<torch.autograd._functions.basic_ops.AddConstant object at 0x7fe6000cb4a8>
'''
z = y * y * 3
out = z.mean()

out.backward()
print(x.grad)
'''
Variable containing:
 4.5000  4.5000
 4.5000  4.5000
[torch.FloatTensor of size 2x2]
'''


