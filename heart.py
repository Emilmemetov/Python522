import math
from turtle import *


def heart1(m):
    return 15 * math.sin(m) ** 3


def heart2(m):
    return 12 * math.cos(m) - 5 * \
        math.cos(2 * m) - 2 * \
        math.cos(3 * m) - \
        math.cos(4 * m)


speed(0)
bgcolor("black")

for i in range(300):
    goto(heart1(i) * 18, heart2(i) * 18)
    for j in range(1):
        color("red")
    goto(0, 0)

done()


