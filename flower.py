#!/usr/bin/env python
# encoding: utf-8

from turtle_api import *

def flower(t, R, n):
    angle = 360.0 / n
    for i in range(n):
        arc(t, R, angle)
        lt(t, 180 - angle)
        arc(t, R, angle)
        lt(t, 180)

def dul_flower(t, R, n):
    for i in range(2):
        flower(t, R, n)
        lt(t, 180.0/n)

if __name__ == '__main__':
    world = TurtleWorld()

    bob = Turtle()
    bob.delay = 0.001

    #flower(bob, 300, 20)
    dul_flower(bob, 400, 10)
    wait_for_user()
