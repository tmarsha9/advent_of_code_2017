#!/usr/bin/env python

import sys

def usage_and_exit():
  print 'usage: {} input_file'.format(sys.argv[0])
  sys.exit(1)

if len(sys.argv) != 2:
  usage_and_exit()

f = open(sys.argv[1], "r")
sum = 0
for row in f:
  print row
  items = [int(num) for num in row.split()]
  min = items[0]
  max = items[0]
  for i in range(1,len(items)):
    if items[i] > max:
      max = items[i]
    elif items[i] < min:
      min = items[i]
  sum = sum + max-min
print 'sum: {}'.format(sum)
