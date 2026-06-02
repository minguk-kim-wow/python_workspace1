import matplotlib.pyplot as plt
import numpy as np


t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', 
                xy=(4, 1), 
                xytext=(3, 1.5),
                arrowprops=dict(facecolor='red', shrink=0.05),
             )

plt.annotate('local min', 
                xy=(3.5, -1), 
                xytext=(3, -1.5),
                arrowprops=dict(facecolor='blue', arrowstyle='<->'),
             )

plt.ylim(-2, 2)
plt.show()