import os

### 显示当前路径下文件
# Get the list of all files and directories
# in the root directory
path = "/"
dir_list = os.listdir(path)
  
print("Files and directories in '", path, "' :") 
  
# print the list
print(dir_list)

### 显示当前路径
pwd = os.getcwd()
print(f"current path: {pwd}")

### 路径符号问题
'''
1.
    在python中,路径可以接受“/”“\”，这里形象的比喻成撇和捺。但是由于“\”在python中是作为转义符使用，所以在路径中使用“\”时，要写成“\\”
    r'E:\tokaka\recent_learn\crowd_counting\code\C-3\C-3-Framework\datasets\UCF-qnrf-processed\train\point\1.mat'
    加r就可以用“\”

2.https://blog.csdn.net/m0_37693335/article/details/81474995
    在同一目录下第一层即为同级目录，./即可
    ../父级目录
'''

### os.path.splitext 得到扩展名

# importing os module 
import os
  
# path
path = '/home/User/Desktop/file.txt'
  
# Split the path in 
# root and ext pair
root_ext = os.path.splitext(path)
  
# print root and ext
# of the specified path
print("root part of '% s':" % path, root_ext[0])
print("ext part of '% s':" % path, root_ext[1], "\n")
  
  
# path
path = '/home/User/Desktop/'
  
# Split the path in 
# root and ext pair
root_ext = os.path.splitext(path)
  
# print root and ext
# of the specified path
print("root part of '% s':" % path, root_ext[0])
print("ext part of '% s':" % path, root_ext[1])

### basename 得到文件名
import glob
import os

for f in sorted(glob.glob('E:\\tokaka\\recent_learn\\crowd_counting\\dataset\\UCF-QNRF_ECCV18\\Train\\*.jpg')
):
    temp = f.split('\\')[-1]
    temp1 = os.path.basename(f)
    print(temp)
    print(temp1)
    print(f)