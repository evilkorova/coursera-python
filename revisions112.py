# Exercise 11.2

import re

finput = input('Enter a file name: ')
if finput is '':
    finput = 'mbox-short.txt'

fname = ''
try:
    fname = open(finput)
except:
    print('File cannot be opened: ' + filename)
    exit()

revisions = []
for line in fname:
    n = re.findall('New Rev.+: ([0-9]+)', line)
    try:
        i = float(n[0])
        revisions.append(i)
    except:
        continue

avg = sum(revisions) / len(revisions)
print(avg)
