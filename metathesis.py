#!/usr/bin/env python
# encoding: utf-8

def bi_search(word, wordlist):
    floor = 0
    ceil = len(wordlist) - 1
    while floor <= ceil:
        mid = (floor + ceil) / 2
        if wordlist[mid] == word:
            return mid
        elif wordlist[mid] > word:
            ceil = mid - 1
        else:
            floor = mid + 1
    return -1

def swap(word, pos1, pos2):
    lst = list(word)
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return ''.join(lst)

def output_metathesis(wordlist):
    for pos in range(len(wordlist)):
        word = wordlist[pos]
        for i in range(0, len(word)):
            for j in range(i+1, len(word)):
                tar_word = swap(word, i, j)
                if bi_search(tar_word, wordlist) > pos:
                    print word, tar_word


if __name__ == '__main__':
    wordlist = ['converse', 'conserve', 'hello', 'world', 'pig', 'gip', 'git', 'tig', 'igt']
    wordlist.sort()
    output_metathesis(wordlist)
