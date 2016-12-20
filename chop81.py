#!/usr/bin/python2
# Exercise 8.1

def chop(t):
    del t[0]
    del t[-1]
    return t

numlist = [1,2,3,4]
print chop(numlist)
