#!/usr/bin/env python
# encoding: utf-8

is_reducible = {"":True}

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

def remove_pos(word, pos):
    lst = list(word)
    del lst[pos]
    return ''.join(lst)

def check_reducible(word, wordlist):
    if len(word) == 0:
        return True
    if bi_search(word, wordlist) < 0:
        return False
    for pos in range(len(word)):
        tar_word = remove_pos(word, pos)
        if is_reducible.get(tar_word, False) or check_reducible(tar_word, wordlist):
            is_reducible[remove_pos(word, pos)] = True
            return True
    return False


if __name__ == '__main__':
    wordlist = ["sprite", 'spite', 'spit', 'pit', 'it', 'i', 'hello']
    wordlist.sort()
    print check_reducible("sprite", wordlist)
    print check_reducible("hello", wordlist)
