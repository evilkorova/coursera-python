#!/usr/bin/python2
# Exercise 9.2
# Parses mailbox file and keeps track of which day of the week
# each mail message was sent on.

finput = raw_input('Enter a file name: ')
if finput is '':
    finput = 'mbox-short.txt'

try:
    fname = open(finput)
except:
    print 'File cannot be opened: ' + filename
    exit()

print ''

dow = dict()

for line in fname:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    dow[words[2]] = dow.get(words[2],0) + 1

print dow
