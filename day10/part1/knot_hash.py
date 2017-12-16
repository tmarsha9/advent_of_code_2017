#!/usr/bin/env python

NUMBERS_SIZE=256


def reverse(pos, length, numbers):
  l = pos
  r = (pos+length-1)%NUMBERS_SIZE
  while length > 1:
    length-=2
    numbers[l],numbers[r] = numbers[r],numbers[l]
    l=(l+1)%NUMBERS_SIZE
    r=(r-1)%NUMBERS_SIZE

  return numbers

with open("input.txt", "r") as f:
  lengths = [int(i) for i in f.readline().strip().split(',')]

position = 0
skip = 0
numbers = range(0,NUMBERS_SIZE)

for l in lengths:
  numbers = reverse(position,l,numbers)
  position=(position+l+skip)%NUMBERS_SIZE
  skip+=1
print numbers[0]*numbers[1]
