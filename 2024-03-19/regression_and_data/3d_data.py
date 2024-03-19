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

ax.scatter3D(x_data, y_data, z_data, c=z_data, cmap="Greens")

# its regression time!

M = np.matrix([[1, 1], [2, 2]])
print(M)


# plt.show()
