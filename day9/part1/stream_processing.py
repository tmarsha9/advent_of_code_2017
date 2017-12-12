#!/usr/bin/env python

import sys

def skip_garbage(stream,index):
  if stream[index] != '<':
    print "skip_garbage must be called at beginning of garbage!"
    sys.exit(1)

  index+=1
  while index < len(stream):
    if stream[index] == '!':
      index+=1
    elif stream[index] == '>':
      return index
    index+=1
  return None

def get_score(stream,index,level):
  if stream[index] != '{':
    print "get_score must be called at beginning of group!"
    sys.exit(1)

  index+=1
  score = level
  while index < len(stream):
    if stream[index] == '!':
      index+=1
    elif stream[index] == '{':
      group_score,index = get_score(stream,index,level+1)
      score += group_score
    elif stream[index] == '}':
      return score,index
    elif stream[index] == '<':
      index = skip_garbage(stream,index)

    index+=1

  print stream,index
  return None

#for i in range(8):
#  with open("input"+str(i)+".txt","r") as f:
#    print get_score(f.readline().strip(),0,1)[0]

with open("input.txt","r") as f:
  print get_score(f.readline().strip(),0,1)[0]
