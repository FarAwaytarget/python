# coding=utf-8
import matplotlib.pyplot as plt

from randowm_walk import Randomwalk

while True:

    rw = Randomwalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=15)
    plt.show()

    keep_running = input("make another walk y/n? \n")
    if keep_running == 1:
        break
    else:
        pass
