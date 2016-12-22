#!/usr/bin/python2
# Exercise 8.5
# Parses mailbox file and returns emails in from field

finput = raw_input('Enter a file name: ')

try:
    fname = open(finput)
except:
    print 'File cannot be opened: ' + filename
    exit()

fromCnt = 0

print ''

for line in fname:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    print words[1]
    fromCnt = fromCnt + 1

print ''
print 'There were %d lines in the file with From as the first word' % fromCnt
