#!/usr/bin/env python
# encoding: utf-8

import string
def parse(sentence):
    sentence = sentence.strip().lower()
    for i in string.punctuation + string.whitespace:
        sentence = sentence.replace(i, ' ')
    #for i in string.punctuation + string.whitespace:
        #if i == ' ':
            #continue
        #sentence = ' '.join(sentence.split(i))
    return [i for i in sentence.split(" ") if i != '']

def addup(file):
    dic = {}
    f = open(file)
    for i in f:
        lst = parse(i)
        if len(lst) != 0:
            for i in lst:
                dic[i] = dic.get(i, 0) + 1
    res = [(value,key) for key, value in dic.items()]
    res.sort(reverse=True)
    #print res
    return res

def top20(file):
    return addup(file)[:20]

if __name__ == '__main__':
    #print parse("Hello World!~Good-bye Cruel World!\n")
    print top20('in')
