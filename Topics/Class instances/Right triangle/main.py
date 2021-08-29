class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.s = (self.a * self.b) / 2


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here


def is_right_triangle(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


if is_right_triangle(input_a, input_b, input_c):
    triangle = RightTriangle(input_c, input_a, input_b)
    print("%.1f" % triangle.s)
else:
    print("Not right")
