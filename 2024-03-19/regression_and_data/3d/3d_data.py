import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = plt.axes(projection="3d")

x_data, y_data, z_data = [], [], []

with open("3D_data.txt") as f:
    lines = f.readlines()

for line in lines:
    x, y, z = line.split(",")
    x_data.append(float(x))
    y_data.append(float(y))
    z_data.append(float(z))

_1s = np.ones(len(x_data))
M = np.array([x_data, y_data, _1s]).T
n = np.linalg.inv(M.T @ M) @ M.T @ z_data

xx, yy = np.meshgrid(range(-50, 50), range(-50, 50))
zz = (-n[0] * xx - n[1] * yy) / n[2]

ax.scatter3D(x_data, y_data, z_data, c=z_data, cmap="Greens")
ax.plot_surface(xx, yy, zz, alpha=0.5)

print(f"{n[0]}x + {n[1]}y + {n[2]}z = 0")

plt.show()
plt.savefig("3d_data.png")
