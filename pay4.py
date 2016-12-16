#!/bin/python
# 4.14 Excercise 6 
# Kindle Location 910

def computepay(h,r):
  if h >= 40:
    ot = h - 40
    otr = r * 1.5
    p = (40 * r) + (ot * otr)
  else:
    p = h * r
  return p

hours = raw_input('Enter Hours: ')
rate = raw_input('Enter Rate: ')

try:
  hours = float(hours)
  rate = float(rate)
except:
  print "Error, please enter numeric input"
  quit()

pay = computepay(hours,rate)
pay = str(pay)
print "Pay: " + pay
