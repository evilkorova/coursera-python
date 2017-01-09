# Exercise 11.1
# Write a program to simulate the operation of the _grep_ command
# Ask the user the to enter a regular expression and count
# the number of lines that matched the regular expression

# import regex library
import re

regex = input('Enter a regular expression: ')
filename = open('mbox.txt')

count = 0

for line in filename:
    if re.search(regex, line) == None:
        continue
    count = count + 1

print('mbox.txt had %d lines that matched %s' % (count, regex))
