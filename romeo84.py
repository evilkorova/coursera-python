#!/usr/bin/python2
# Exercise 8.4

fname = open('romeo.txt')

unique = []

for line in fname:
    words = line.split()
    for word in words:
        if word in unique: continue
        unique.append(word)

unique.sort()
print unique
