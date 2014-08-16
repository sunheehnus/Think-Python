#!/usr/bin/env python
# encoding: utf-8

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print is_palindrome("")
print is_palindrome("a")
print is_palindrome("ab")
print is_palindrome("aba")
