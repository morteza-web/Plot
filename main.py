#this is test message.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, color='green')

fig.savefig("first.png")
plt.show()
