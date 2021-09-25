"""
没有lock的话，共享内存（即共享变量Value）会抢来抢去
"""
import time
import multiprocessing as mp

def job(v, num, l):
    # l.acquire()
    for _ in range(10):
        time.sleep(1)
        v.value += num
        print(v.value)
    # l.release()

if __name__ == '__main__':
    l = mp.Lock()
    v = mp.Value('i', 0)

    p1 = mp.Process(target=job, args=(v,1,l))
    p2 = mp.Process(target=job, args=(v,3,l))

    p1.start()
    p2.start()

    p1.join()
    p2.join()