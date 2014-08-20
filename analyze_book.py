#!/usr/bin/env python
# encoding: utf-8

import string

def process_file(filename):
    hist = {}
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

hist = process_file('emma.txt')
print 'Total words', total_words(hist)
print 'Different words', different_words(hist)
