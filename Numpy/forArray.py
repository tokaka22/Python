import numpy as np

a = np.zeros((2,3))
print(f"a before: {a}")

func = lambda x:x+1
res = np.array([func(xi) for xi in a])

print(f"a after: {res}")