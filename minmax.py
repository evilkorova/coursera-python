#!/bin/python
# Exercise 5.2
# kindle location 1337

numMin = None
numMax = 0

while True:
    input = raw_input("Enter a number: ")
    if input == "done":
        break
    try:
        input = int(input)
    except:
        print "Invalid input"
        continue
    if numMin is None or input < numMin:
        numMin = input
    if input > numMax:
        numMax = input

print "Maximum is ", numMax
print "Mininum is ", numMin
