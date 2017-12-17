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

def get_hash(string):
  lengths = [ord(i) for i in string]

  lengths += EXTRA_LENGTHS

  position = 0
  skip = 0
  numbers = range(0,NUMBERS_SIZE)

  for i in range(TOTAL_ROUNDS):
    for l in lengths:
      numbers = reverse(position,l,numbers)
      position=(position+l+skip)%NUMBERS_SIZE
      skip+=1

  numbers = to_hex(make_dense_hash(numbers))
  return numbers

#main
with open("input.txt","r") as f:
  string = f.readline().strip() + "-"

#regions = [[-1]*128]*128 <-- Longest bug to find. At least I learned something ^_^
regions = [[-1]*128 for i in range(128)]

hashes = []
for i in range(128):
  hashes.append(long(get_hash(string+str(i)),16))

region = 0
for i in range(128):
  for j in range(128):
    if regions[i][j] == -1 and hashes[i]&(1<<(127-j)):
      regions[i][j] = region
      queue = [(i,j)]
      while len(queue)>0:
        ii,jj = queue.pop(0)
        if ii-1 >= 0 and regions[ii-1][jj] == -1 and hashes[ii-1]&(1<<(127-jj))!=0:
          regions[ii-1][jj] = region
          queue.append((ii-1,jj))
        if ii+1 < 128 and regions[ii+1][jj] == -1 and hashes[ii+1]&(1<<(127-jj))!=0:
          regions[ii+1][jj] = region
          queue.append((ii+1,jj))
        if jj-1 >= 0 and regions[ii][jj-1] == -1 and hashes[ii]&(1<<(127-(jj-1)))!=0:
          regions[ii][jj-1] = region
          queue.append((ii,jj-1))
        if jj+1 < 128 and regions[ii][jj+1] == -1 and hashes[ii]&(1<<(127-(jj+1)))!=0:
          regions[ii][jj+1] = region
          queue.append((ii,jj+1))
      region+=1
print region
