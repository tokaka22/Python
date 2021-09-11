'''
https://www.youtube.com/watch?v=IEEhzQoKtQU&list=RDCMUCCezIgC97PvUuR4_gbFUs5g&index=2
print(f'') f是指format形式，与.format()类似，用其他类型替换string
time.pref_counter()比较精确，time.time()受系统影响，适合大程序计时
thread传统操作是thread.start()，thread.join()，后者用于 截断 多线程并发的运行
'''
import concurrent.futures
import time

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs) # map自带join()

        for res in results:
            print(res)

    final = time.perf_counter()
    # print('Finished time is {}'.format(final - strat))
    print(f'Finished time is {round(final - start, 2)}')


'''---Source Code---

import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
'''