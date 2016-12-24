#!/usr/bin/python2
# Exercise 9.3
# Parses mailbox file and builds a histogram of how many
# emails came from each address

finput = raw_input('Enter a file name: ')
if finput is '':
    finput = 'mbox-short.txt'

try:
    fname = open(finput)
except:
    print 'File cannot be opened: ' + filename
    exit()

print ''

emails = dict()

for line in fname:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    emails[words[1]] = emails.get(words[1],0) + 1

print emails
