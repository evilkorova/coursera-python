#!/bin/python
# Exercise 5.1
# kindle location 1323

numTotal = 0
numCount = 0

while True:
    input = raw_input("Enter a number: ")
    if input == "done":
        break
    try:
        input = float(input)
    except:
        print "Invalid input"
        continue
    numTotal = numTotal + input
    numCount = numCount + 1

print numTotal, numCount, numTotal/numCount
