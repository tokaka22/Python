import torch
import numpy
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

class Implicit(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x, y0, F, max_iter=100):
        with torch.enable_grad():
            y = y0.clone().detach().requires_grad_() # 既不数据共享，也不对梯度共享，从此两个张量无关联
            xv = x.detach() # 不需要追踪导数
            opt = torch.optim.LBFGS([y], max_iter=max_iter) # 前者代表对谁求梯度（需要更新的参数）
            def reevaluate(): # 这部分LBFGS不懂
                opt.zero_grad()
                z = F(xv,y)**2
                z.backward()
                return z
            opt.step(reevaluate)
        ctx._the_function = F
        ctx.save_for_backward(x, y)
        return y

    @staticmethod
    def backward(ctx, output_grad):
        x, y = ctx.saved_tensors
        F = ctx._the_function
        with torch.enable_grad():
            xv = x.detach().requires_grad_()
            y = y.detach().requires_grad_()
            z = F(xv,y)
            z.backward()
        return -xv.grad/y.grad*output_grad, None, None, None

def circle(x,y):
    return x**2+y**2-1

# x = numpy.linspace(-1.2,1.2,30)
# y = numpy.linspace(-1.2,1.2,30)
# t = numpy.linspace(0, 2*numpy.pi)
# xx = numpy.repeat(x, len(y)).reshape(x.shape[0],y.shape[0])
# yy = numpy.tile(y, (len(x),)).reshape(x.shape[0],y.shape[0])


# fig = pyplot.figure()
# ax = fig.gca(projection='3d')
# ax.plot_wireframe(xx,yy,circle(xx,yy),cmap=pyplot.cm.coolwarm_r,
#                        linewidth=0.01, antialiased=False)
# ax.plot(numpy.cos(t),numpy.sin(t), 0, linewidth=3, c="black")
# ax.view_init(elev=40., azim=30)

x = torch.tensor([0.5], dtype=torch.double, requires_grad=True)
y0 = torch.tensor([0.5], dtype=torch.double)
y= Implicit.apply(x, y0, circle)
print (y.item(), (1-0.5**2)**0.5) # 解y
print(x)
y.backward()
print(x.grad.shape, y.shape)
print(x)
print(torch.autograd.gradcheck(lambda x: Implicit.apply(x.unsqueeze(0),y0,circle), x))