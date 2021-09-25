import torch

t = torch.ones(2,3)
print(t.shape)

print(t.unsqueeze(dim=0).unsqueeze(dim=0).shape)