'''
argsparse是python的命令行解析的标准模块，内置于python，不需要安装。这个库可以让我们直接在命令行中就可以向程序中传入参数并让程序运行。
https://zhuanlan.zhihu.com/p/56922793
'''

import argparse

'''
1
'''
# ### basic
# parser = argparse.ArgumentParser(description='命令行中传入一个数字')
# #type是要传入的参数的数据类型  help是该参数的提示信息
# parser.add_argument('integers', type=str, help='传入的数字')

# args = parser.parse_args()

# #获得传入的参数
# print(args)

# '''
# 其实得到的这个结果Namespace(integers='5')是一种类似于python字典的数据类型。
# 我们可以使用 arg.参数名来提取这个参数
# '''
# print(args.integers)

'''
2
'''
# ### 传入多个参数
# nargs='+'表示将多个参数合成List

# parser = argparse.ArgumentParser(description='命令行中传入一个数字')
# #type是要传入的参数的数据类型  help是该参数的提示信息
# parser.add_argument('integers', type=str, nargs = '+', help='传入的数字')

# args = parser.parse_args()

# #获得传入的参数
# print(args)
# print(args.integers)

'''
3
'''
# ### 改变数据类型：add_argument中有type参数可以设置传入参数的数据类型。我们看到代码中有type这个关键词，该关键词可以传入list, str, tuple, set, dict等。例如我们把上面的type=str，改成type=int,这时候我们就可以进行四则运算。
# parser = argparse.ArgumentParser(description='命令行中传入一个数字')
# parser.add_argument('integers', type=int, nargs='+',help='传入的数字')
# args = parser.parse_args()

# print(args.integers)

'''
4
'''
### 位置参数，默认是按序传参
parser = argparse.ArgumentParser(description="姓名")
parser.add_argument('param1', type=str, help='姓')
parser.add_argument('param2', type=str, help='名')
args = parser.parse_args()

print(args.param1 + args.param2)

'''
5
'''
### 按序不方便，可选参数
parser = argparse.ArgumentParser(description='姓名')
parser.add_argument('--family', type=str,help='姓')
parser.add_argument('--name', type=str,help='名')
args = parser.parse_args()

#打印姓名
print(args.family+args.name)

#需要输入 python demo.py --family=张 --name=三

'''
6
'''
### 默认值 关键词default
parser = argparse.ArgumentParser(description='姓名')
parser.add_argument('--family', type=str, default='张',help='姓')
parser.add_argument('--name', type=str, default='三', help='名')
args = parser.parse_args()

#打印姓名
print(args.family+args.name)

'''
7
'''
### 必需参数 required
parser = argparse.ArgumentParser(description='姓名')
parser.add_argument('--family', type=str, help='姓')
parser.add_argument('--name', type=str, required=True, default='', help='名')
args = parser.parse_args()

#打印姓名
print(args.family+args.name)