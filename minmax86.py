#!/usr/bin/python2
# Exercise 8.6
# Rewrite minmax.py using lists and the min() and max() functions

numbers = []

while True:
    input = raw_input("Enter a number: ")
    if input == "done":
        break
    try:
        input = int(input)
    except:
        print "Invalid input"
        continue
    numbers.append(input)

numMax = max(numbers)
numMin = min(numbers)

print "Maximum is ", numMax
print "Mininum is ", numMin
