from scipy.io import loadmat
import numpy as np

points = loadmat(r'E:\tokaka\recent_learn\crowd_counting\code\C-3\C-3-Framework\datasets\UCF-qnrf-processed\train\point\1.mat')['annPoints'].astype(np.float32)
print('ok')