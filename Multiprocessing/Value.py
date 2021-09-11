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

import time
from multiprocessing import Process, Manager, Value

# def foo(data, name=''):
#     print(type(data), data.value, name)
#     data.value += 1

def foo(data, name=''): # foo函数即多进程运行的函数对值更改过多需要用到Lock，否则会出错
    print(type(data), data.value, name)
    for j in range(1000):
        data.value += 1

if __name__ == "__main__":
    manager = Manager()
    x = manager.Value('i', 0)
    y = Value('i', 0) # Value更快

    for i in range(5):
        Process(target=foo, args=(x, 'x')).start()
        Process(target=foo, args=(y, 'y')).start()

    print('Before waiting: ')
    print('x = {0}'.format(x.value)) 
    print('y = {0}'.format(y.value)) 

    time.sleep(5.0)
    print('After waiting: ')
    print('x = {0}'.format(x.value))
    print('y = {0}'.format(y.value))

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