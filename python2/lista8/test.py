import numpy as np

grad = np.array([[i] for i in range(10)])
print(grad)

Theta = np.array([-1, 1])
print(Theta)

print()
print()
print()

print(sum(grad * Theta))