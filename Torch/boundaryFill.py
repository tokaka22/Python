import torch
import torch.nn as nn


# ================== 镜像填充 ==================
def conv_ReflectionPad2d():
    # 定义一个四维数据：(batchSize, channel, height, width)
    data = torch.tensor([[[[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]]]]).float()
    print("data_shape: ", data.shape)
    print("data: ", data)
    # 复制边界n次，分别为：左、右、上、下
    ReflectionPad = nn.ReflectionPad2d(padding=(2, 1, 1, 2))
    data1 = ReflectionPad(data)
    print("data1_shape: ", data1.shape)
    print("data1: ", data1)


if __name__ == '__main__':
    conv_ReflectionPad2d()