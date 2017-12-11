#!/usr/bin/env python

import sys

def usage_and_exit():
  print 'usage: {} input'.format(sys.argv[0])
  sys.exit(1)

#input for my example =  ??? lost it :(

if len(sys.argv) != 2:
  usage_and_exit()

input = sys.argv[1]

sum = 0
for index,num in enumerate(input):
  if input[index-1] == num:
    sum = sum + int(num)

print 'sum: {}'.format(sum)
