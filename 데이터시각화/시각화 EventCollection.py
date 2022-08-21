import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# create random data
xdata = np.random.random([2, 10])
print(xdata)
print(xdata.shape)
print('************')
# split the data into two parts
xdata1 = xdata[0, :]
xdata2 = xdata[1, :]

print(xdata1)
print(xdata2)

# sort the data so it makes clean curves
xdata1.sort()
xdata2.sort()

# create some y data points
ydata1 = xdata1 ** 2
ydata2 = 1 - xdata2 ** 3
# plot the data
fig = plt.figure()

# display the plot
plt.show()