#!/usr/bin/env python
# encoding: utf-8

from turtle_api import *

def spiral(t, time):
    for i in range(time):
        arc(t, 10+i*0.5, 10)

if __name__ == '__main__':
    world = TurtleWorld()

    bob = Turtle()
    bob.delay = 0.001

    spiral(bob, 1000)

    wait_for_user()
