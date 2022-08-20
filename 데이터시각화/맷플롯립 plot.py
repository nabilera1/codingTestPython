import matplotlib.pyplot as plt
import numpy as np

x = np.arange(50)
y = np.arange(50) * 2

plt.figure(figsize=(3, 6))
plt.plot(x, y)
plt.plot(x, y, linestyle=':', color='red', label='Temperature')
# plt.plot(x, y, linestyle=':', marker='*', color='red', label='Temperature')
# plt.plot(x,y, linestyle=':', marker='o', color='red', label='Temperature')
# plt.plot(x,y, color='red', label='Temperature')
plt.title("My Data")
plt.xlabel("X")
plt.ylabel("X*2")
plt.xlim(0, 50)
plt.ylim(0, 100)
plt.legend(shadow=True, borderpad=1)
plt.show()
