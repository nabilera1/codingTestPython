import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d


np.random.seed(0)

# generate noisy data
raw = np.cumsum(np.random.normal(5, 100, 1000))
raw /= np.max(raw)
# print(raw)
# print(np.max(raw), np.min(raw)) #1.0 -0.723911150393409


# smooth
smooth = gaussian_filter1d(raw, 100)

# compute second derivative
smooth_d2 = np.gradient(np.gradient(smooth))

# find switching points
infls = np.where(np.diff(np.sign(smooth_d2)))[0]

# plot results
plt.figure(figsize=(12, 6))
plt.plot(raw, label='Noisy Data')
plt.plot(smooth, label='Smoothed Data')
plt.plot(smooth_d2 / np.max(smooth_d2), label='Second Derivative (scaled)')
for i, infl in enumerate(infls, 1):
    plt.axvline(x=infl, color='k', label=f'Inflection Point {i}')
# plt.legend(bbox_to_anchor=(1.55, 1.0))
plt.legend()
plt.show()