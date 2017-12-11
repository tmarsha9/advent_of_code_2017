#!/usr/bin/env python

import sys

def usage_and_exit():
  print 'usage: {} data_location'.format(sys.argv[0])
  sys.exit(1)

#input for my test = 312051

if len(sys.argv) != 2:
  usage_and_exit()

input = int(sys.argv[1])

if input <= 0:
  usage_and_exit()
elif input == 1:
  #rest of formula only works if input > 1
  print 'distance: {}'.format(0)
  sys.exit(0)

input = input-1
#compute biggest square before location
count = 1
while (count+2)**2 <= input:
  count = count + 2

#subtract biggeset square from index to only consider indexes of outside layer
input = input - (count**2)

#find distance to middle of outside row
input = abs((count+2)/2-(input+1)%(count+1))

#add distance from center to this layer
print 'distance: {}'.format(input+count/2+1)
