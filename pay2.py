#!/bin/python
# 3.11 Excersise 1
# Kindle Location 910

hours = raw_input('Enter Hours: ')
hours = float(hours)
rate = raw_input('Enter Rate: ')
rate = float(rate)
if hours > 40:
  ot = hours - 40
  otrate = rate * 1.5
  extra = ot * otrate
  pay = (40 * rate) + extra
else:
  pay = hours * rate
pay = str(pay)
print "Pay: " + pay
