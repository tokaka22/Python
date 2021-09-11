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

2.https://blog.csdn.net/m0_37693335/article/details/81474995
    在同一目录下第一层即为同级目录，./即可
    ../父级目录
'''

###
os.path.splitext