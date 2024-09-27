import matplotlib.pyplot as plt
import numpy as np
import random

floors = []
ratings = []

for i in range (1, 28):
    floor = "floor\n" + str(i)
    floors.append(floor)

floors.insert(0, "basement")

x = np.array(floors)

for i in range (27):
    r1 = random.randint(1, 10)
    ratings.append(r1)
ratings.insert(0, 10)

y = np.array(ratings)

plt.bar(x,y, color = "green")
plt.ylabel("Rating")
plt.show()