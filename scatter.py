import random as np
import matplotlib.pyplot as plt

x_ax = []
y_ax = []
for i in range(5):

	x = np.randint(1, 10)
	y = np.randint(1, 10)

	x_ax.append(x)
	y_ax.append(y)

	i += 1

fig, ax = plt.subplots()

ax.scatter(x_ax, y_ax, c="red")

fig.savefig("scatter.png")
