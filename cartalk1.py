#!/usr/bin/env python
# encoding: utf-8

def is_triple_double(word):
    def state1(word, pre):
        if len(word) == 0:
            return False
        if word[0] == pre:
            return state2(word[1:], word[0])
        else:
            pre = word[0]
            return state1(word[1:], word[0])
    def state2(word, pre):
        if len(word) == 0:
            return False
        if word[0] == pre:
            return state2(word[1:], word[0])
        else:
            pre = word[0]
            return state3(word[1:], word[0])
    def state3(word, pre):
        if len(word) == 0:
            return False
        if word[0] == pre:
            return state4(word[1:], word[0])
        else:
            pre = word[0]
            return state1(word[1:], word[0])
    def state4(word, pre):
        if len(word) == 0:
            return False
        if word[0] == pre:
            return state2(word[1:], word[0])
        else:
            pre = word[0]
            return state5(word[1:], word[0])
    def state5(word, pre):
        if len(word) == 0:
            return False
        if word[0] == pre:
            return True
        else:
            pre = word[0]
            return state1(word[1:], word[0])
    return state1(word[1:], word[0])
print is_triple_double("mississippi")
print is_triple_double("MMMMMSSYYY")
