import cv2
import numpy as np
import pandas as pd

# 长宽不同
def gaussian_kernel_2d_opencv(row_size, col_size, sigma): # 和matlab略有小小误差
    kx = cv2.getGaussianKernel(row_size,sigma)
    ky = cv2.getGaussianKernel(col_size,sigma)
    return np.multiply(kx,np.transpose(ky)) 

H = gaussian_kernel_2d_opencv(15,8,4) # 
print(H)
print(H.shape)
print(np.sum(H))

H_df = pd.DataFrame(H)
H_df.to_csv("tep.csv", index=False, header=False)

# 长宽一致
def gaussian_kernel_2d_opencv_eq(kernel_size, sigma):
    kx = cv2.getGaussianKernel(kernel_size,sigma)
    ky = cv2.getGaussianKernel(kernel_size,sigma)
    return np.multiply(kx,np.transpose(ky))

H2 = gaussian_kernel_2d_opencv_eq(15,4)
print(H2)
# H_df = pd.DataFrame(H2)
# H_df.to_csv("tep.csv", index=False, header=False)
