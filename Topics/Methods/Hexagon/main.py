import math


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    # create get_area here
    def get_area(self):
        sqrt_3 = math.sqrt(3)
        area = (3 * sqrt_3 * (self.side_length ** 2)) / 2
        return "{:.3f}".format(area)
