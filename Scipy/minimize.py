import scipy
import math
from scipy.optimize import minimize,fsolve
import torch

f = 'lambda t: (1e+15)*((-0.0018382 + (1/4)*math.exp(-29/2/t)/(math.pi*t*((1/4)/(math.pi*t) + math.exp(-1/t)/(math.pi*t) + math.exp(-2/t)/(math.pi*t) + math.exp(-4/t)/(math.pi*t) + 2*math.exp(-5/t)/(math.pi*t) + math.exp(-8/t)/(math.pi*t) + math.exp(-9/t)/(math.pi*t) + 2*math.exp(-10/t)/(math.pi*t) + 2*math.exp(-13/t)/(math.pi*t) + math.exp(-18/t)/(math.pi*t) + math.exp(-1/2/t)/(math.pi*t) + 2*math.exp(-5/2/t)/(math.pi*t) + math.exp(-9/2/t)/(math.pi*t) + 2*math.exp(-13/2/t)/(math.pi*t) + 2*math.exp(-17/2/t)/(math.pi*t) + 3*math.exp(-25/2/t)/(math.pi*t) + 2*math.exp(-29/2/t)/(math.pi*t) + 2*math.exp(-37/2/t)/(math.pi*t) + math.exp(-49/2/t)/(math.pi*t) + math.exp(-1/4/t)/(math.pi*t) + 2*math.exp(-5/4/t)/(math.pi*t) + math.exp(-9/4/t)/(math.pi*t) + 2*math.exp(-13/4/t)/(math.pi*t) + 2*math.exp(-17/4/t)/(math.pi*t) + 3*math.exp(-25/4/t)/(math.pi*t) + 2*math.exp(-29/4/t)/(math.pi*t) + 2*math.exp(-37/4/t)/(math.pi*t) + 2*math.exp(-41/4/t)/(math.pi*t) + 2*math.exp(-45/4/t)/(math.pi*t) + math.exp(-49/4/t)/(math.pi*t) + 2*math.exp(-53/4/t)/(math.pi*t) + 2*math.exp(-61/4/t)/(math.pi*t) + 2*math.exp(-65/4/t)/(math.pi*t) + 2*math.exp(-85/4/t)/(math.pi*t)))))'
# f = 'lambda x:(x-2)**2'
# f2 = 'lambda x:((x-2)**2)**2'

F = eval(f)
F2 = eval('lambda t: (1e+15)*((-0.0018382 + (1/4)*math.exp(-29/2/t)/(math.pi*t*((1/4)/(math.pi*t) + math.exp(-1/t)/(math.pi*t) + math.exp(-2/t)/(math.pi*t) + math.exp(-4/t)/(math.pi*t) + 2*math.exp(-5/t)/(math.pi*t) + math.exp(-8/t)/(math.pi*t) + math.exp(-9/t)/(math.pi*t) + 2*math.exp(-10/t)/(math.pi*t) + 2*math.exp(-13/t)/(math.pi*t) + math.exp(-18/t)/(math.pi*t) + math.exp(-1/2/t)/(math.pi*t) + 2*math.exp(-5/2/t)/(math.pi*t) + math.exp(-9/2/t)/(math.pi*t) + 2*math.exp(-13/2/t)/(math.pi*t) + 2*math.exp(-17/2/t)/(math.pi*t) + 3*math.exp(-25/2/t)/(math.pi*t) + 2*math.exp(-29/2/t)/(math.pi*t) + 2*math.exp(-37/2/t)/(math.pi*t) + math.exp(-49/2/t)/(math.pi*t) + math.exp(-1/4/t)/(math.pi*t) + 2*math.exp(-5/4/t)/(math.pi*t) + math.exp(-9/4/t)/(math.pi*t) + 2*math.exp(-13/4/t)/(math.pi*t) + 2*math.exp(-17/4/t)/(math.pi*t) + 3*math.exp(-25/4/t)/(math.pi*t) + 2*math.exp(-29/4/t)/(math.pi*t) + 2*math.exp(-37/4/t)/(math.pi*t) + 2*math.exp(-41/4/t)/(math.pi*t) + 2*math.exp(-45/4/t)/(math.pi*t) + math.exp(-49/4/t)/(math.pi*t) + 2*math.exp(-53/4/t)/(math.pi*t) + 2*math.exp(-61/4/t)/(math.pi*t) + 2*math.exp(-65/4/t)/(math.pi*t) + 2*math.exp(-85/4/t)/(math.pi*t)))))**2')
# F2 = eval(f2)
x0 = 12
res = minimize(F2, x0, method='L-BFGS-B')
print(res)
res2 = fsolve(F, 4.0)
print(f"res2:{res2}")
print(F(res2))

t0 = torch.tensor([11], dtype=torch.double)
with torch.enable_grad():
    tv = t0.clone().detach().requires_grad_() # 既不数据共享，也不对梯度共享，从此两个张量无关联
    # xv = x.detach() # 不需要追踪导数

    opt = torch.optim.LBFGS([tv], tolerance_grad=1e-6, max_iter=100) # 前者代表对谁求梯度（需要更新的参数）
    def reevaluate(): # 这部分LBFGS不懂
        opt.zero_grad()
        z = (F(tv))**2
        z.backward()
        return z
    opt.step(reevaluate)
print(f'tv: {tv}')
print(F(tv))
print(F(t0))
print(F(tv)>F(t0))