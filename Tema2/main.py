import numpy as np

x = np.array([2, 1, 2])
y = np.array([1, -1, 4])
x = x.T
y = y.T
print(x, y)
print(np.dot(x, y))
print(f'Len x: {np.linalg.norm(x)}; Len y: {np.linalg.norm(y)}')
print(f'Arccos of the vectors {np.arccos(np.clip(np.dot(x / np.linalg.norm(x), y / np.linalg.norm(y)), -1.0, 1.0))}')
