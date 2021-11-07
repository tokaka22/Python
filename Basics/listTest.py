'''
np的函数可以用在list上
'''

# import numpy as np

# list = [1,2,3,4]
# print(np.mean(list)) 

'''
delete
'''
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
delIndex = [1, 2, 7, 9] # 删除1，2，7，9
# # 依次删除 报错
# del a[1]
# del a[2]
# del a[7]
# del a[8]
# print(a)

# # 正序删除
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for _,item in enumerate(delIndex):
#     del a[item]
# print(a)

# 逆序删除
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for _,item in enumerate(reversed(delIndex)):
    del a[item]
print(a)