#!/usr/bin/python2
# Exercise 9.5
# Parses mailbox file and builds a histogram of how many
# emails came from each domain

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
    loc = words[1].find('@')
    domain = words[1][loc+1:]
    emails[domain] = emails.get(domain,0) + 1

for k, v in emails.items():
    print k, v
