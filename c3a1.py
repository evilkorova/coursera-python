# Data Assignment 1

import re

finput = input('Enter a file name: ')
if finput is '':
    finput = 'regex_sum_306614.txt'

try:
    f = open(finput)
except:
    print('File cannot be opened: ' + filename)
    exit()

blob = f.read()
numlist = re.findall('[0-9]+', blob)

walk = 0
for i in numlist:
    numlist[walk] = int(i)
    walk = walk + 1

sumlist = sum(numlist)

# list compehensive makes the walk shorter:
# numlist = [int(i) for i in numlist]
