#!/usr/bin/env python
# encoding: utf-8

def most_frequent(sentence):
    hist = {}
    for i in sentence:
        hist[i] = hist.get(i, 0) + 1
    t = [(freq, x) for (x, freq) in hist.items()]
    t.sort(reverse=True)
    print [x for (freq, x) in t]

if __name__ == '__main__':
    most_frequent("Hello World!\nGoodbye Cruel World!\n")
