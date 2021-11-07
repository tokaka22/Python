import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

X_train = np.array([[ 1., -1.,  2.]])
X_train = X_train.reshape(-1,1)
print(X_train)
X_scale = preprocessing.MaxAbsScaler().fit_transform(X_train)
print(X_scale)