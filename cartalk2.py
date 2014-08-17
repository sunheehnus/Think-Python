#!/usr/bin/env python
# encoding: utf-8

def is_palindrome(num, length):
    num1 = num
    num2 = 0
    while num != 0:
        num2 = num2*10 + num%10
        num /= 10
        length -= 1
    return num1 == num2 and length == 0

def find_special_palindrome():
    i = 100000
    while i < 999997:
        if is_palindrome(i%10000, 4) and is_palindrome((i+1)%100000, 5) and is_palindrome((i+2)%100000/10, 4) and is_palindrome((i+3), 6):
            print i
        i += 1

find_special_palindrome()
