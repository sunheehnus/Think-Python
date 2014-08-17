#!/usr/bin/env python
# encoding: utf-8

def rotate_word(word, step):
    result = ''
    for i in word:
        flag = ord(i) & 0x20
        cur = chr(ord(i) & ~0x20)
        if ord(cur) >= ord('A') and ord(cur) <= ord('Z'):
            result += chr((ord('A') + (ord(cur)-ord('A')+step)%26) | flag)
        else:
            result += i
    return result

print rotate_word('cheer', 7)
print rotate_word('cHE-er', 7)
print rotate_word('melon', -10)
