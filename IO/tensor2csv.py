import torch
import pandas as pd
import numpy as np

x = torch.randn((8,5))
print(x)
x_np = x.numpy()
print(x_np)
x_df = pd.DataFrame(x_np)
print(x_df)
# index无行名，header无列名
x_df.to_csv('tmp.csv',index = False, header=False)