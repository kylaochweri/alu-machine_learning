#!/usr/bin/env python3

#import libs
import numpy as np
import matplotlib.pyplot as plt

#data
y = np.arange(0, 11) ** 3
x = np.arange(0, 11)

#plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='red', linewidth=2)
plt.title('Cubic line graph')
plt.show()