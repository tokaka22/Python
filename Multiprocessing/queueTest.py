'''
https://stackoverflow.com/questions/11515944/how-to-use-multiprocessing-queue-in-python
'''

# from multiprocessing import Process, Queue
# import time
# import sys

# def reader_proc(queue):
#     ## Read from the queue; this will be spawned as a separate Process
#     while True:
#         msg = queue.get()         # Read from the queue and do nothing
#         if (msg == 'DONE'):
#             break

# def writer(count, queue):
#     ## Write to the queue
#     for ii in range(0, count):
#         queue.put(ii)             # Write 'count' numbers into the queue
#     queue.put('DONE')

# if __name__=='__main__':
#     pqueue = Queue() # writer() writes to pqueue from _this_ process
#     for count in [10**4, 10**5, 10**6]:             
#         ### reader_proc() reads from pqueue as a separate process
#         reader_p = Process(target=reader_proc, args=((pqueue),))
#         reader_p.daemon = True # p.daemon：默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置
#         reader_p.start()        # Launch reader_proc() as a separate python process

#         _start = time.time()
#         writer(count, pqueue)    # Send a lot of stuff to reader()
#         reader_p.join()         # Wait for the reader to finish
#         print("Sending {0} numbers to Queue() took {1} seconds".format(count, 
#             (time.time() - _start)))

'''
https://www.bilibili.com/video/BV1jW411Y7pv?p=3
q可以存放数据
'''

import multiprocessing as mp

def job(q):
    res = 0
    for i in range(1000):
        res += i+i**2+i**3
    q.put(res) # queue

if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)