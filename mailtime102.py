#!/usr/bin/python3
# Exercise 10.2
# Parses mailbox file and builds a histogram of how many
# emails came from each hour of the day.

finput = input('Enter a file name: ')
if finput is '':
    finput = 'mbox-short.txt'

fname = ''
try:
    fname = open(finput)
except:
    print('File cannot be opened: ' + filename)
    exit()

print()

hours = dict()

for line in fname:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    t = words[5].split(':')
    hours[t[0]] = hours.get(t[0], 0) + 1

lst = []
for k, v in hours.items():
    lst.append((k, v))

lst.sort()
for x, y in lst:
    print(x, y)
