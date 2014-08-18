#!/usr/bin/env python
# encoding: utf-8

def build_key(word):
    tar = {}
    for i in word:
        tar[i] = tar.get(i, 0) + 1
    return tuple(tar.items())
def build_anagram_sets(wordlist):
    dict_anagram = {}
    for word in wordlist:
        key = build_key(word)
        dict_anagram[key] = (dict_anagram.get(key, []))
        dict_anagram[key].append(word)
    res = {}
    for key in dict_anagram:
        if len(dict_anagram[key]) > 1:
            res[key] = dict_anagram[key]
    return res
def print_anagram_sets(anagram_sets):
    for key in anagram_sets:
        print key, anagram_sets[key]

def print_sorted_anagram_sets(anagram_sets):
    lst = []
    for key in anagram_sets:
        lst.append((len(anagram_sets[key]), anagram_sets[key], key))
    lst.sort(reverse=True)
    for i, value, key in lst:
        print key, value


if __name__ == '__main__':
    wordlist = ['deltas', 'desalt', 'lasted', 'retainers', 'ternaries', 'resmelts', 'smelters', 'termless', 'hello', 'world']
    ana_sets = build_anagram_sets(wordlist)
    print_anagram_sets(ana_sets)
    print
    print_sorted_anagram_sets(ana_sets)
