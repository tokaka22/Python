import numpy as np
from numpy.random import default_rng

rng = default_rng()

list = np.random.random_integers(20,size=(10))
print(list)

print(rng.choice(range(225), 50, replace=False)) # replace表明不能重复选

print(range(225))