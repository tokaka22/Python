
import torch
### is_nonzero 是不是非零,只能检测单个向量
torch.is_nonzero(torch.tensor([0.]))
torch.is_nonzero(torch.tensor([1.5]))
# torch.is_nonzero(torch.tensor([1, 3, 5])) # wrong


### count_nonzero 计数非零项
x = torch.zeros(3,3)
x[torch.randn(3,3) > 0.5] = 1
print(x)
print(torch.count_nonzero(x))

### 切换类型
'''
1.CPU tensor转GPU tensor：
cpu_imgs.cuda()

2. GPU tensor 转CPU tensor：
gpu_imgs.cpu()

3. numpy转为CPU tensor：
torch.from_numpy(imgs)

4.CPU tensor转为numpy数据：
cpu_imgs.numpy()
'''