#!/usr/bin/env python
# encoding: utf-8

def sqrt(x , epsilon = 0.00000000001):
    guess = 1.0
    while abs(guess**2 - x) >= epsilon:
        guess = (guess + x/guess) / 2
    return guess

def pi():

    sqrt_2 = sqrt(2, 1e-15)
    res_tmp = 0
    cur = 1103 * 2 * sqrt_2 / 9801
    k = 0
    while cur > 1e-15 :
        res_tmp += cur
        cur /= 1103 + 26390 * k
        k += 1
        cur *= 1103 + 26390 * k
        cur *= 4*k * (4*k - 1) * (4*k - 2) * (4*k - 3)
        cur /= k**4 * 396**4
    return 1/res_tmp

print sqrt(2)
print pi()
