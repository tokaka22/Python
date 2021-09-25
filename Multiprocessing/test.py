from multiprocessing import RawArray
import numpy as np

X_shape = (6, 10)
# Randomly generate some data
data = np.random.randn(*X_shape)
X = RawArray('d', X_shape[0] * X_shape[1])
# Wrap X as an numpy array so we can easily manipulates its data.
X_np = np.frombuffer(X, dtype=np.float64).reshape(X_shape)
# Copy data to our shared array.
res = np.copyto(X_np, data)
print(res)