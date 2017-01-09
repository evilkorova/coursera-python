#!/usr/bin/python3
# Exercise 10.1
# Parses mailbox file and builds a histogram of how many
# emails came from each address and prints max but using
# tuples and sorting

finput = input('Enter a file name: ')
if finput is '':
    finput = 'mbox-short.txt'

try:
    fname = open(finput)
except:
    print('File cannot be opened: ' + filename)
    exit()

print()

emails = dict()

for line in fname:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    emails[words[1]] = emails.get(words[1],0) + 1

lst = []
for key, add in emails.items():
    lst.append((add, key))

lst.sort(reverse=True)
x,y = lst[0]
print(y, x)
