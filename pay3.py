#!/bin/python
# 3.11 Excercise 2
# Kindle Location 910

hours = raw_input('Enter Hours: ')
rate = raw_input('Enter Rate: ')

try:
  hours = float(hours)
  rate = float(rate)
except:
  print "Error, please enter numeric input"
  quit()

if hours > 40:
  ot = hours - 40
  otrate = rate * 1.5
  extra = ot * otrate
  pay = (40 * rate) + extra
else:
  pay = hours * rate
pay = str(pay)
print "Pay: " + pay
