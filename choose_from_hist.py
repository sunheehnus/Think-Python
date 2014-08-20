#!/usr/bin/env python
# encoding: utf-8

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def choose_from_hist(d):
    res = []
    for key in d:
        for i in range(d[key]):
            res.append(key)
    import random
    return random.choice(res)



print choose_from_hist(histogram(['a','a','b']))
print choose_from_hist(histogram(['a','a','b']))
print choose_from_hist(histogram(['a','a','b']))
print choose_from_hist(histogram(['a','a','b']))
print choose_from_hist(histogram(['a','a','b']))
print choose_from_hist(histogram(['a','a','b']))
