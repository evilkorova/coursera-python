#!/usr/bin/python2
# Exercise 7.1

filename = raw_input('Enter a file name: ')
try:
 fin = open(filename)
except:
 print 'File cannot be opened: ' + filename
 exit()

for line in fin:
 upLine = line.upper()
 upLine = upLine.rstrip()
 print upLine


 # upLine = line.upper().rstrip() works too!
