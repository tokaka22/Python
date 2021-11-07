# import torch

# a = torch.tensor(1.0, requires_grad=True)
# y = a ** 2 
# a_ = a.detach()
# print(a_.grad)    # None，requires_grad=False
# a_.requires_grad_()  # 强制其requires_grad=True，从而支持求导

# z = a_ * 3
# y.backward()
# z.backward()

# print(a.grad)    #　2，与a_无关系
# print(a_.grad)   #  3

'''
clone()后对a梯度叠加，叠加即2+3，是加！！！
'''
import torch

a = torch.tensor(1.0, requires_grad=True)
y = a ** 2 
a_ = a.clone()
z = a_ * 3
y.backward()
print(a.grad)   # 2
z.backward()
print(a_.grad)  # None. 中间variable，无grad
print(a.grad)    #　5. a_的梯度会传递回给a，因此2+3=5
