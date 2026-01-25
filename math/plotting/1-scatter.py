#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

#data
mean = [69, 0]
cov = [[15, 8], [8, 15  ]]  # diagonal covariance
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y +=180

#plot scatter
plt.figure(figsize=(10, 6))
plt.scatter(x, y, c='magenta')
plt.xlabel('Height (in)')
plt.ylabel('Weight (lbs)')
plt.title('Men\'s Height vs Weight')
plt.show()