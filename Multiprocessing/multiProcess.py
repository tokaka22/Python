'''
multiprocessing.Process()建立进程需要start()与join()
有这样调用函数的：eg multiprocessing.Process() target指定函数名，args再传入参数
concurrent.futures.ProcessPoolExecutor()上下文建立Pool池
context manger内自动有join()效果
p接住executor.submit()后，需要p.result()才能调出结果
接住list comprehension的是list
map要等 全部 运行完后生成一个新list存放结果，故也不需要as_completed()
as_completed()时刻检查list中完成的process
map中：exception会存在results中，需要在results中进行进一步处理
'''

"""
args[]？？？
"""
import concurrent.futures
import time
import multiprocessing

# ### 第一版 体验最老的操作
# start = time.perf_counter()

# def do_something():
#     print("Sleeping 1 Second")
#     time.sleep(1)
#     print("Done Sleeping...")

# p1 = multiprocessing.Process(target = do_something)
# p2 = multiprocessing.Process(target = do_something)

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# print(f"Finished Time is {round(time.perf_counter()-start,3)}")

# ### 第二版 用个for&指定时间
# start = time.perf_counter()

# def do_something(seconds):
#     print(f"Sleeping {seconds} second")
#     time.sleep(seconds)
#     print("Done Sleeping")

# list = []
# for _ in range(10):
#     p = multiprocessing.Process(target = do_something, args = [2]) # target指定函数名，args再传入参数
#     p.start()
#     list.append(p)

# for res in list:
#     res.join()

# print(f"Finished Time is {round(time.perf_counter()-start,3)}")

# ### 第三版 用concurrent.futures
# start = time.perf_counter()

# def do_something(seconds):
#     print(f"Sleeping {seconds} second")
#     time.sleep(seconds)
#     return "Done Sleeping"

# with concurrent.futures.ProcessPoolExecutor() as executor: # context manger内自动有join()效果
#     p1 = executor.submit(do_something, 1)
#     p2 = executor.submit(do_something, 1)
    
#     print(p1.result()) # result()才能调出结果
#     print(p2.result())

# print(f"Finished Time is {round(time.perf_counter()-start,3)}")

### 第四版 用list comprehension作loop
start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second")
    time.sleep(seconds)
    return "Done Sleeping"

with concurrent.futures.ProcessPoolExecutor() as executor: # context manger内自动有join()效果
    results = [executor.submit(do_something, 1) for _ in range(10)]
    print(type(results))

    for f in concurrent.futures.as_completed(results): # 参数results为list，检查list中process是否完成
        print(f.result())

print(f"Finished Time is {round(time.perf_counter()-start,3)}")

# ### 第五版 用map
# start = time.perf_counter()

# def do_something(seconds):
#     print(f"Sleeping {seconds} second")
#     time.sleep(seconds)
#     return "Done Sleeping"

# secs = [5,4,3,2,1]
# with concurrent.futures.ProcessPoolExecutor() as executor: # context manger内自动有join()效果
#     results = executor.map(do_something, secs)

#     for res in results: # map要等 全部 运行完后生成一个新list存放结果
#         print(res)

# print(f"Finished Time is {round(time.perf_counter()-start,3)}")


'''---Source Code---

import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

'''