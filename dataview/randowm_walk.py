# coding=utf-8
from random import choice


class Randomwalk ():
    """ creat a random data class """

    def __init__(self, num_points=5000):
        """ init random attributes """
        self.num_points = num_points
        # all random set init num is zero
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ calculation"""
        while len (self.y_values) < self.num_points:
            # 决定前进的方向以及沿着这个方向前进的就前进的就
            x_direction = choice ([1, -1])
            x_distance = choice ([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_directoion = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_setp = y_directoion * y_distance

            if x_step == 0 and y_setp == 0:
                continue
            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_setp

            self.x_values.append (next_x)
            self.y_values.append (next_y)
