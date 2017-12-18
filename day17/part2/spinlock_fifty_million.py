#!/usr/bin/env python

with open("input.txt","r") as f:
  stride = int(f.readline().strip())

value = 0
buffer_size = 1
position = 0

#this method makes value 0 stay at the end of the buffer
#since the buffer is circular, the next place after 0 is
#the beginning of the array. Here, I only keep track of 
#the item after 0 (called value). It is only updated
#when the place after 0 is updated. That only occurs
#when the new item is inserted between the old value and
#0, which is when the place to insert before is 0.

for i in xrange(1,50000001):
  position=(position+stride+1)%buffer_size
  if position == 0:
    value = i
  buffer_size+=1
print value
