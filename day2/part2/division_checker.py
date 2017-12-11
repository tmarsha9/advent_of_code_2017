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

  for i in range(len(items)):
    for j in range(i+1,len(items)):
      if items[j] % items[i] == 0:
        sum = sum + items[j]/items[i]
      elif items[i] % items[j] == 0:
        sum = sum + items[i]/items[j]
print 'sum: {}'.format(sum)
