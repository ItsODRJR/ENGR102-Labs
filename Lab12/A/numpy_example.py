import numpy as np

# A (3x4)
A = np.arange(0, 12).reshape(3, 4)

# B (4x2)
B = np.arange(0, 8).reshape(4, 2)

# C (2x3)
C = np.arange(0, 6).reshape(2, 3)

# D (ABC)
D = A @ B @ C

# D^T (D Transposed)
D_T = D.T

# E (sqrt of D divided by 2)
E = np.sqrt(D) / 2

print("A = ", A,  "\n")
print("B = ", B,  "\n")
print("C = ", C,  "\n")
print("D = ", D,  "\n")
print("D^T = ", D_T,  "\n")
print("E = ", E,  "\n")