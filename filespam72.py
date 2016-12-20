#!/usr/bin/python2
# Exercise 7.2

filename = raw_input('Enter a file name: ')
try:
 fin = open(filename)
except:
 print 'File cannot be opened: ' + filename
 exit()

spamCount = 0
spamTotal = 0

for line in fin:
 if line.startswith('X-DSPAM-Confidence:'):
    spamCount = spamCount + 1
    loc = line.find(':')
    value = float(line[loc+1:])
    spamTotal = spamTotal + value

spamAvg = str(spamTotal / spamCount)
print 'Average spam confidence: ' + spamAvg
