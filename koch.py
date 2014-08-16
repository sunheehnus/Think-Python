#!/usr/bin/env python
# encoding: utf-8

from turtle_api import *

def koch_curve(t, x):
    if x < 3:
        fd(t, x)
        return
    koch_curve(t, x/3)
    lt(t, 60)
    koch_curve(t, x/3)
    rt(t, 120)
    koch_curve(t, x/3)
    lt(t, 60)
    koch_curve(t, x/3)

def snowflake(t, x):
    koch_curve(t, x)
    rt(t, 120)
    koch_curve(t, x)
    rt(t, 120)
    koch_curve(t, x)

if __name__ == '__main__':
    world = TurtleWorld()

    bob = Turtle()
    bob.delay = 0.001

    #koch_curve(bob, 1000)
    snowflake(bob, 100)
    wait_for_user()
