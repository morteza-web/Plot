import random as rn
import matplotlib.pyplot as plt

data = []

def datagen():

	round = int(input("enter number"))
	for i in range(round):

		data.append(rn.randint(1, 10))
		i += 1

	return

datagen()

fig, ax = plt.subplots()
ax.pie(data, labels=data)

name = input("enter the name of your plot ")

fig.savefig(name)
plt.show()
