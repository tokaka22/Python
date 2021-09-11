'''
代码版本差得多没整出来

属性（成员变量）
saved_tensors: 传给forward()的参数，在backward()中会用到。
needs_input_grad:长度为 :attr:num_inputs的bool元组，表示输出是否需要梯度。可以用于优化反向过程的缓存。
num_inputs: 传给函数 :func:forward的参数的数量。
num_outputs: 函数 :func:forward返回的值的数目。
requires_grad: 布尔值，表示函数 :func:backward 是否永远不会被调用。

成员函数
forward()
forward()可以有任意多个输入、任意多个输出，但是输入和输出必须是Variable。(官方给的例子中有只传入tensor作为参数的例子)
backward()
backward()的输入和输出的个数就是forward()函数的输出和输入的个数。其中，backward()输入表示关于forward()输出的梯度(计算图中上一节点的梯度)，backward()的输出表示关于forward()的输入的梯度。在输入不需要梯度时（通过查看needs_input_grad参数）或者不可导时，可以返回None。
'''

'''
关于ctx :
ctx is a context object that can be used to stash information for backward computation
'''

'''
y = x*w +b # 自己定义的LinearFunction
z = f(y)
下面的grad_output = dz/dy
根据复合函数求导法则:
1. dz/dx =  dz/dy * dy/dx = grad_output*dy/dx = grad_output*w
2. dz/dw =  dz/dy * dy/dw = grad_output*dy/dw = grad_output*x
3. dz/db = dz/dy * dy/db = grad_output*1
'''

import torch.autograd.Function as Function

class LinearFunction(Function):
    # 创建torch.autograd.Function类的一个子类
    # 必须是staticmethod
    @staticmethod
    # 第一个是ctx，第二个是input，其他是可选参数。
    # ctx在这里类似self，ctx的属性可以在backward中调用。
    # 自己定义的Function中的forward()方法，所有的Variable参数将会转成tensor！因此这里的input也是tensor．在传入forward前，autograd engine会自动将Variable unpack成Tensor。
    def forward(ctx, input, weight, bias=None):
        print(type(input))
        ctx.save_for_backward(input, weight, bias) # 将Tensor转变为Variable保存到ctx中
        output = input.mm(weight.t())  # torch.t()方法，对2D tensor进行转置
        if bias is not None:
            output += bias.unsqueeze(0).expand_as(output)　＃unsqueeze(0) 扩展处第0维
            # expand_as(tensor)等价于expand(tensor.size()), 将原tensor按照新的size进行扩展
        return output

    @staticmethod
    def backward(ctx, grad_output): 
        # grad_output为反向传播上一级计算得到的梯度值
        input, weight, bias = ctx.saved_variables
        grad_input = grad_weight = grad_bias = None
        # 分别代表输入,权值,偏置三者的梯度
        # 判断三者对应的Variable是否需要进行反向求导计算梯度
        if ctx.needs_input_grad[0]:
            grad_input = grad_output.mm(weight) # 复合函数求导，链式法则
        if ctx.needs_input_grad[1]:
            grad_weight = grad_output.t().mm(input)　# 复合函数求导，链式法则
        if bias is not None and ctx.needs_input_grad[2]:
            grad_bias = grad_output.sum(0).squeeze(0)

        return grad_input, grad_weight, grad_bias

#建议把新操作封装在一个函数中
def linear(input, weight, bias=None):
    # First braces create a Function object. Any arguments given here
    # will be passed to __init__. Second braces will invoke the __call__
    # operator, that will then use forward() to compute the result and
    # return it.
    return LinearFunction()(input, weight, bias)#调用forward()

# 或者使用apply方法对自己定义的方法取个别名
linear = LinearFunction.apply

#检查实现的backward()是否正确
from torch.autograd import gradcheck
# gradchek takes a tuple of tensor as input, check if your gradient
# evaluated with these tensors are close enough to numerical
# approximations and returns True if they all verify this condition.
input = torch.randn(20,20).double(), requires_grad=True)
test = gradcheck(LinearFunction(), input, eps=1e-6, atol=1e-4)
print(test)  #　没问题的话输出True