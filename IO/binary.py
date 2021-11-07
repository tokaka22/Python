import numpy as np

filename = open("chart_target\AdcData-11-6-2-39-38_minus_338.chart", "r") # 'wr'报错
oriData = np.fromfile(filename, dtype=np.int16) # np.fromfile可以转换二进制文件