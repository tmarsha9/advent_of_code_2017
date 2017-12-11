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

grid = {} #key is (x,y) coordinate

grid[(0,0)] = 1

print grid
