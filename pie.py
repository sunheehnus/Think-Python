#!/usr/bin/env python
# encoding: utf-8

from turtle_api import *

def pie(t, n, length):
    import math
    angle = 90 + 180.0 / n
    isosceles_len = (length / 2.0) / math.cos((180-angle) / 360.0 * 2 * math.pi)
    for i in range(n):
        fd(t, length)
        lt(t, angle)
        fd(t, isosceles_len)
        lt(t, 180)
        fd(t, isosceles_len)
        lt(t, angle)

if __name__ == '__main__':
    world = TurtleWorld()

    bob = Turtle()
    bob.delay = 0.001

    pie(bob, 17, 40)

    wait_for_user()
