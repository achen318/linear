# Plotting 2D Data and Regression Lines
# Patrick Honner, 3/19/23

# Import the matplotlib package and alias the pyplot module
import matplotlib.pyplot as plt
import numpy as np

# Create the plot object
fig, ax = plt.subplots()

# Set the viewing window in the plot from -50 to 50  in both directions
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)

# Read in the data
# Data format: x,y

xdata = []
ydata = []

f = open("2D_data.txt")
data = f.readlines()
f.close()

# Parse the data into lists of x's and y's

for i in range(len(data)):
    datapoint = data[i].split(",")
    xdata.append(float(datapoint[0]))
    ydata.append(float(datapoint[1]))

# This plots the points (xdata[i], ydata[i])
# The 'ro' option yields red unconnected dots

plt.plot(xdata, ydata, "r*")

# The following code plots a line
# The way plot work is that given [x_1,x_2,...] and [y_1,y_2,...] it connects (x_1,y_1) to (x_2,y_2), then (x_2,y_2) to (x_3,y_3), and so on
# Thus, the following plots the segment with endpoints (-25,-25) and (30,30)

plt.plot([-25, 30], [-25, 30], "b")

# This shows the object (Must ctrl-c out of this in the console)
plt.show()
