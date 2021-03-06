#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-180, 180, 3000)

plt.subplot(1, 2, 1)

y1 = np.sin(x)
y2 = (np.sin(x)) ** 2
y3 = np.cos(x)

plt.plot(x, y1, "r", label = "sine")
plt.plot(x, y2, "g", label = "sine squared")
plt.plot(x, y3, "b", label = "cosine")
plt.legend(loc = "lower left")

plt.xlim(-4, 4)
plt.ylim(-1, 1)

plt.subplot(1, 2, 2, polar = True)

r1 = (np.sin(x)) ** 2
r2 = np.sin(x)
r3 = np.cos(x)

plt.plot(x, y1, "g", label = "sin squared")
plt.plot(x, y2, "r", label = "sin")
plt.plot(x, y3, "b", label = "cos")
plt.legend(loc = "lower left")

plt.suptitle("Trignometric Functions", fontsize = 31)

plt.show()
