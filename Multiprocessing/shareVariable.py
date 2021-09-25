"""
https://stackoverflow.com/questions/17377426/shared-variable-in-pythons-multiprocessing
1.
    The Manager can be shared across computers, while Value is limited to one computer. 
    Value will be faster (run the below code to see), so I think you should use 
    that unless you need to support arbitrary objects or access them over a network.

2.To summarize:
    a.
    Use Manager to create multiple shared objects, including dicts and lists. 
    Use Manager to share data across computers on a network.
    b.
    Use Value or Array when it is not necessary to share information across a network 
    and the types in ctypes are sufficient for your needs.
    c.
    Value is faster than Manager.

3.foo函数即多进程运行的函数对值更改过多需要用到Lock，否则会出错
"""
from itertools import repeat
import multiprocessing
import numpy as np
import time
from multiprocessing import Lock, Process, Manager, Value, Pool, Array
import multiprocessing as mp
'''
测试manager.Value与Value
同时对值更改过多时会出错
'''
# # def foo(data, name=''):
# #     print(type(data), data.value, name)
# #     data.value += 1

# ### 对值更改过多出错
# def foo(data, name=''): # foo函数即多进程运行的函数对值更改过多需要用到Lock，否则会出错
#     print(type(data), data.value, name)
#     for j in range(1000): # 1000体现对值更改过多
#         data.value += 1
#         # 这样才用上lock，前提是有lock
#         # with data.get_lock():
#         #     data.value += 1

# if __name__ == "__main__":
#     manager = Manager()
#     x = manager.Value('i', 0,)
#     y = Value('i', 0) # Value更快
#     # y = Value('i', 0, lock=False) # 改成False也对

#     for i in range(5):
#         Process(target=foo, args=(x, 'x')).start()
#         Process(target=foo, args=(y, 'y')).start()

#     print('Before waiting: ')
#     print('x = {0}'.format(x.value)) 
#     print('y = {0}'.format(y.value)) 

#     time.sleep(5.0)
#     print('After waiting: ')
#     print('x = {0}'.format(x.value))
#     print('y = {0}'.format(y.value))

'''
测试multiprocess对普通变量多次修改是否会有效
结果：无法改变x，y值
'''
# ### 普通变量
# def foo(data, name=''): # foo函数即多进程运行的函数对值更改过多需要用到Lock，否则会出错
#     print(type(data), data, name)
#     for j in range(10):
#         data += 1

# if __name__ == "__main__":
#     ### 测试普通变量————无法改变x，y值
#     x = 0
#     y = 0

#     for i in range(5):
#         Process(target=foo, args=(x, 'x')).start()
#         Process(target=foo, args=(y, 'y')).start()

#     print('Before waiting: ')
#     print('x = {0}'.format(x)) 
#     print('y = {0}'.format(y)) 

#     time.sleep(5.0)
#     print('After waiting: ')
#     print('x = {0}'.format(x))
#     print('y = {0}'.format(y))

'''
测试给矩阵不同位置赋值行不行
结果：不行，且array好像错乱了(array的memory会瞎变)
'''
# def foo(tuple, array):
#     array[tuple[0], tuple[1]] = 1 # array的memory会瞎变
#     print(array)
#     return

# if __name__ == '__main__':
#     h = 2
#     w = 3
#     falltenList = []
#     for i in range(h):
#         for j in range(w):
#             tuple = (i, j)
#             falltenList.append(tuple)
#     print(falltenList)

#     array = np.zeros((h, w), dtype=float)
#     # print(array)
#     multiPool = Pool(1)
#     multiPool.starmap(foo, zip(falltenList, repeat(array)))
#     print(f'final:{array}')


'''
测试给 数组list 不同位置赋值行不行——使用共享变量
'''
# import ctypes as c

# def foo(tuple, list):
#     list.append(tuple)
#     return

# if __name__ == '__main__':
#     h = 2
#     w = 3
#     falltenList = []
#     for i in range(h):
#         for j in range(w):
#             tuple = (i, j)
#             falltenList.append(tuple)
#     print(falltenList)

#     manager = multiprocessing.Manager()
#     # list = manager.list() # 可以
#     list = [] # 普通list就是不行
    
#     multiPool = Pool(1)
#     multiPool.starmap(foo, zip(falltenList, repeat(list)))
#     print(f'final:{list}')

'''
测试给矩阵不同位置赋值行不行——list保存(x, y, value)

'''
def foo(tuple, array):
    array[tuple[0], tuple[1]] = 1 # array的memory会瞎变
    print(array)
    return

if __name__ == '__main__':
    h = 2
    w = 3
    falltenList = []
    for i in range(h):
        for j in range(w):
            tuple = (i, j)
            falltenList.append(tuple)
    print(falltenList)

    array = np.zeros((h, w), dtype=float)
    # print(array)
    multiPool = Pool(1)
    multiPool.starmap(foo, zip(falltenList, repeat(array)))
    print(f'final:{array}')

'''stackoverflow原问题
def f(n):
    n.value += 1

if __name__ == '__main__':
    d = {}
    p = []

    for i in range(5):
        d[i] = Manager().Value('i',0)
        p.append(Process(target=f, args=(d[i],)))
        p[i].start()

    for q in p:
        q.join()

    for i in d:
        d[i] = d[i].value

    print(d)
'''