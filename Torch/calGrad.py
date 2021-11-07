import torch
import math


# f = 'lambda t: (-0.615724265575409 + 24873.0487102721*math.exp(-248.730487102721/t)/(math.pi*t*(248.730487102721/(math.pi*t) + 994.921948410882*math.exp(-1989.84389682176/t)/(math.pi*t) + 1989.84389682176*math.exp(-1243.6524355136/t)/(math.pi*t) + 994.921948410882*math.exp(-994.921948410882/t)/(math.pi*t) + 994.921948410882*math.exp(-497.460974205441/t)/(math.pi*t) + 994.921948410882*math.exp(-248.730487102721/t)/(math.pi*t))))'
# with torch.enable_grad():
#     t = torch.tensor(49.1074).detach().requires_grad_()
#     F = eval(f)
#     z = F(t)
#     z.backward()
#     print(t.grad)

# f = 'lambda gtv,t: (-gtv + 24873.049744046*math.exp(-248.73049744046/t)/(math.pi*t*(248.73049744046/(math.pi*t) + 994.921989761839*math.exp(-1989.84397952368/t)/(math.pi*t) + 1989.84397952368*math.exp(-1243.6524872023/t)/(math.pi*t) + 994.921989761839*math.exp(-994.921989761839/t)/(math.pi*t) + 994.921989761839*math.exp(-497.460994880919/t)/(math.pi*t) + 994.921989761839*math.exp(-248.73049744046/t)/(math.pi*t))))'
# with torch.enable_grad():
#     gtv = torch.tensor(0.6157).detach().requires_grad_()
#     t = torch.tensor(49.1074).detach().requires_grad_()
#     F = eval(f)
#     z = F(gtv,t)
#     z.backward()
#     print(t.grad)

'''
加上dtype=torch.float64后与默认的float32的结果不一致，说明位数太少了，浮点数精确位的不同体现出来了
'''
f2 = 'lambda t: (-0.615724265575409 + 24873.0487102721*math.exp(-248.730487102721/t)/(math.pi*t*(248.730487102721/(math.pi*t) + 994.921948410882*math.exp(-1989.84389682176/t)/(math.pi*t) + 1989.84389682176*math.exp(-1243.6524355136/t)/(math.pi*t) + 994.921948410882*math.exp(-994.921948410882/t)/(math.pi*t) + 994.921948410882*math.exp(-497.460974205441/t)/(math.pi*t) + 994.921948410882*math.exp(-248.730487102721/t)/(math.pi*t))))'
f = 'lambda gtv,t: (-gtv + 24873.049744046*math.exp(-248.73049744046/t)/(math.pi*t*(248.73049744046/(math.pi*t) + 994.921989761839*math.exp(-1989.84397952368/t)/(math.pi*t) + 1989.84397952368*math.exp(-1243.6524872023/t)/(math.pi*t) + 994.921989761839*math.exp(-994.921989761839/t)/(math.pi*t) + 994.921989761839*math.exp(-497.460994880919/t)/(math.pi*t) + 994.921989761839*math.exp(-248.73049744046/t)/(math.pi*t))))'
F2 = eval(f2)
with torch.enable_grad():
    gtv = torch.tensor(0.6157, dtype=torch.float32).detach().requires_grad_()
    t1 = torch.tensor(49.1074, dtype=torch.float64).detach().requires_grad_()
    F = eval(f)
    z = F(gtv,t1)
    z.backward()
    print(t1.grad)

    # T_grad[j,i] = -gtv.grad/t.grad*grad_output[j,i]

with torch.enable_grad():
    t2 = torch.tensor(49.1074, dtype=torch.float64).detach().requires_grad_()
    z2 = F2(t2)
    z2.backward()
    print(t2.grad)

    # T_grad[j,i] = -gtv.grad/t.grad*grad_output[j,i]