import numpy as np
import matplotlib.pyplot as plt
import random

x_coords = []
y_coords = []
colors = []

starting_point = np.array([[0], [1]])
matrix = np.array([[1.02, 0.095], [-0.095, 1.02]])

for _ in range(250):
    x_coords.append(starting_point[0, 0])
    y_coords.append(starting_point[1, 0])
    colors.append((random.random(), random.random(), random.random()))
    starting_point = np.dot(matrix, starting_point)

plt.scatter(x_coords, y_coords, color=colors, marker='o', s=10)
plt.title("Rainbow spiral")
plt.xlabel("x")
plt.ylabel("y")
plt.show()