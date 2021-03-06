'''
(loss.data) # 旧的Variable的用法，应该直接取item()就行
'''



# ### 手动求导
# import torch

# dtype = torch.FloatTensor
# # dtype = torch.cuda.FloatTensor # Uncomment this to run on GPU

# # N is batch size; D_in is input dimension;
# # H is hidden dimension; D_out is output dimension.
# N, D_in, H, D_out = 64, 1000, 100, 10

# # Create random input and output data
# x = torch.randn(N, D_in).type(dtype)
# y = torch.randn(N, D_out).type(dtype)

# # Randomly initialize weights
# w1 = torch.randn(D_in, H).type(dtype)
# w2 = torch.randn(H, D_out).type(dtype)

# learning_rate = 1e-6
# for t in range(500):
#     # Forward pass: compute predicted y
#     h = x.mm(w1)
#     h_relu = h.clamp(min=0)
#     y_pred = h_relu.mm(w2)

#     # Compute and print loss
#     loss = (y_pred - y).pow(2).sum()
#     print(t, loss)

#     #手动写求导
#     # Backprop to compute gradients of w1 and w2 with respect to loss
#     grad_y_pred = 2.0 * (y_pred - y)
#     grad_w2 = h_relu.t().mm(grad_y_pred)
#     grad_h_relu = grad_y_pred.mm(w2.t())
#     grad_h = grad_h_relu.clone()
#     grad_h[h < 0] = 0
#     grad_w1 = x.t().mm(grad_h)

#     # Update weights using gradient descent
#     w1 -= learning_rate * grad_w1
#     w2 -= learning_rate * grad_w2

### AutoGrad求导
'''
过去 Variable对象是代表计算图中的一个节点，这种节点有x.data代表Tensor，和x.grad代表其梯度
现在不需要Variable
'''
import torch
from torch.autograd import Variable

dtype = torch.FloatTensor
# dtype = torch.cuda.FloatTensor # Uncomment this to run on GPU

# N is batch size; D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
N, D_in, H, D_out = 64, 1000, 100, 10

# Create random Tensors to hold input and outputs, and wrap them in Variables.
# Setting requires_grad=False indicates that we do not need to compute gradients
# with respect to these Variables during the backward pass.
# 输入求导干嘛，一点用都没有，所以 requires_grad = False
x = Variable(torch.randn(N, D_in).type(dtype), requires_grad=False)
y = Variable(torch.randn(N, D_out).type(dtype), requires_grad=False)

# Create random Tensors for weights, and wrap them in Variables.
# Setting requires_grad=True indicates that we want to compute gradients with
# respect to these Variables during the backward pass.
w1 = Variable(torch.randn(D_in, H).type(dtype), requires_grad=True)
w2 = Variable(torch.randn(H, D_out).type(dtype), requires_grad=True)

learning_rate = 1e-6
for t in range(500):
    # Forward pass: compute predicted y using operations on Variables; these
    # are exactly the same operations we used to compute the forward pass using
    # Tensors, but we do not need to keep references to intermediate values since
    # we are not implementing the backward pass by hand.
    y_pred = x.mm(w1).clamp(min=0).mm(w2)

    # Compute and print loss using operations on Variables.
    loss = (y_pred - y).pow(2).sum()
    print(t, loss.item())
    print(loss.data) # 旧的Variable的用法，应该直接取item()就行

    # Use autograd to compute the backward pass. This call will compute the
    # gradient of loss with respect to all Variables with requires_grad=True.
    # After this call w1.grad and w2.grad will be Variables holding the gradient
    # of the loss with respect to w1 and w2 respectively.
    loss.backward()

    # Update weights using gradient descent; w1.data and w2.data are Tensors,
    # w1.grad and w2.grad are Variables and w1.grad.data and w2.grad.data are
    # Tensors.
    w1.data -= learning_rate * w1.grad.data
    w2.data -= learning_rate * w2.grad.data

    # Manually zero the gradients after updating weights
    w1.grad.data.zero_()
    w2.grad.data.zero_()
