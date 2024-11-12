import numpy as np
import matplotlib.pyplot as plt

######################################
x = np.linspace(-10, 10, 100)
f1 = x**2 / (4 * 2)
f2 = x**2 / (4 * 5)

plt.figure(figsize=(10, 6))
plt.plot(x, f1, label='f=2', linewidth=2.0, color='red')
plt.plot(x, f2, label='f=6', linewidth=6.0, color='blue')
plt.title("Parabola plots with varying focal length")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-2.0, 2.0)
plt.ylim(0, 0.5)  
plt.legend()
plt.show()
######################################

######################################
x_cubic = np.linspace(-4, 4, 25)
y_cubic = 2 * x_cubic**3 + 3 * x_cubic**2 - 11 * x_cubic - 6

plt.figure(figsize=(10, 6))
plt.scatter(x_cubic, y_cubic, marker='*', color='yellow', edgecolors='black')
plt.title("Plot of cubic polynomial")
plt.xlabel("x values")
plt.ylabel("y values")
plt.xlim(-4, 4)
plt.ylim(-50, 125)
plt.show()
######################################

######################################
x_trig = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_sin = np.sin(x_trig)
y_cos = np.cos(x_trig)

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))
ax1.plot(x_trig, y_cos, color='brown', label='cos(x)')
ax1.set_title("Plot of cos(x) and sin(x)")
ax1.set_ylabel("y=cos(x)")
ax1.grid(True)
ax1.legend()

ax2.plot(x_trig, y_sin, color='gray', label='sin(x)')
ax2.set_xlabel("x")
ax2.set_ylabel("y=sin(x)")
ax2.grid(True)
ax2.legend()

plt.show()
######################################