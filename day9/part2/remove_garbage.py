#!/usr/bin/env python

import sys

def count_garbage(stream,index):
  count = 0
  while index < len(stream):
    if stream[index] == '!':
      index+=1
    elif stream[index] == '<':
      skipped,index = garbage_helper(stream,index)
      count += skipped
    index+=1
  return count

def garbage_helper(stream,index):
  if stream[index] != '<':
    print 'garbage helper must be called on a "<" character!'
    sys.exit(1)

  index+=1
  garbage_begin = index
  skipped=0
  while index < len(stream):
    if stream[index] == '!':
      index+=1
      skipped+=2
    elif stream[index] == '>':
      return index-garbage_begin-skipped,index
    index+=1
  return None

#for i in range(8):
#  with open("input"+str(i)+".txt","r") as f:
#    print count_garbage(f.readline().strip(),0)

with open("input.txt","r") as f:
  print count_garbage(f.readline().strip(),0)
