from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, another_point):
        x_diff = self.x - another_point.x
        y_diff = self.y - another_point.y
        return sqrt((x_diff ** 2) + (y_diff ** 2))
