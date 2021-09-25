
from itertools import repeat

def square(x, y):
    x = x**2 - y
    print(x)
    return x

print(list(zip([1,2,3,4,6], repeat(3))))
print(list(map(square, zip([1,2,3,4,6], repeat(3))))) # 传不进去，和multiprocessing中strmap不一样
# print(list(map(square, [(1, 3), (2, 3), (3, 3), (4, 3), (6, 3)])))
[square()]