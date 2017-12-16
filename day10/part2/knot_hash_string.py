#!/usr/bin/env python

NUMBERS_SIZE=256
EXTRA_LENGTHS = [17, 31, 73, 47, 23]
TOTAL_ROUNDS = 64


def reverse(pos, length, numbers):
  l = pos
  r = (pos+length-1)%NUMBERS_SIZE
  while length > 1:
    length-=2
    numbers[l],numbers[r] = numbers[r],numbers[l]
    l=(l+1)%NUMBERS_SIZE
    r=(r-1)%NUMBERS_SIZE

  return numbers

def make_dense_hash(sparse_hash):
  rv = []
  for i in range(16):
    next = sparse_hash[i*16]
    for j in range(1,16):
      next^=sparse_hash[i*16+j]
    rv.append(next)
  return rv

def to_hex(dense_hash):
  rv = ""
  for i in range(len(dense_hash)):
    rv += '{:02x}'.format(dense_hash[i])
  return rv

with open("input.txt", "r") as f:
  lengths = [ord(i) for i in f.readline().strip()]

lengths += EXTRA_LENGTHS

position = 0
skip = 0
numbers = range(0,NUMBERS_SIZE)

for i in range(TOTAL_ROUNDS):
  for l in lengths:
    numbers = reverse(position,l,numbers)
    position=(position+l+skip)%NUMBERS_SIZE
    skip+=1

numbers = make_dense_hash(numbers)
numbers = to_hex(numbers)
print numbers
