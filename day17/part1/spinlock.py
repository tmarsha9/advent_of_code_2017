#!/usr/bin/env python

with open("input.txt","r") as f:
  stride = int(f.readline().strip())

buffer = [0]
position = 0

for i in xrange(1,2018):
  position=(position+stride+1)%len(buffer)
  buffer.insert(position,i)

print buffer[(buffer.index(2017)+1)%len(buffer)]
