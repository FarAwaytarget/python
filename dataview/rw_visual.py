# coding=utf-8
import matplotlib.pyplot as plt

from randowm_walk import Randomwalk

while True:

    rw = Randomwalk(5000)
    rw.fill_walk()
    # 设置绘图窗口的尺寸
    # plt.figure(dpi=128, edgecolor='none')

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=15)
    print(rw.y_values)
    # plt.plot(rw.x_values, rw.y_values, linewidth=1)  #绘制线条
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("make another walk y/n? \n")
    if keep_running == 1:
        break
