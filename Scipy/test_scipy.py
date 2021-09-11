import scipy.optimize as opt
from numpy import exp
import time
start_time = time.time()

def f(variables) :
    (x,y) = variables
    first_eq = x + y**2 - 4
    second_eq = exp(x) + x*y - 3
    return [first_eq, second_eq]
for i in range(100000):
    solution = opt.fsolve(f, (0.1, 1)) # fsolve(equations, X_0)
    print(i)
print(solution)

print("--- %s seconds ---" % (time.time() - start_time))