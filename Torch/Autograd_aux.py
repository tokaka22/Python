# x=0.5
# y=1.5

# def circle(x,y):
#     return x**2+y**2-1

# print(circle(x,y)**2)

# def f1(x, y):
#     return -x/y

# print(f1(x,y))

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

relu = 0.5
w2 = 0.3
def f2(relu, w2):
    return 2*(relu*w2-2)*w2

print(f2(relu,w2))

def f3(relu, w2):
    return 2*(relu*w2-2)*relu

print(f3(relu,w2))