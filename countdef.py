#!/bin/python
# Exercise 6.3
# kindle location 1413

def countstuff(s,l):
    count = 0
    for letter in s:
        if letter == l:
            count = count + 1
    return count

output = countstuff("banana","a")
print output
