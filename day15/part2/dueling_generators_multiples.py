#!/usr/bin/env python

A_FACTOR = 16807
B_FACTOR = 48271

MOD = 2147483647

with open("input.txt","r") as f:
  line = f.readline().strip().split()
  a_start = int(line[4])

  line = f.readline().strip().split()
  b_start = int(line[4])

a = (a_start*A_FACTOR)%MOD
b = (b_start*B_FACTOR)%MOD
count = 0

for i in range(5000000L):
  #make sure values are multiples of 4 or 8
  while a%4 != 0:
    a=(a*A_FACTOR)%MOD
  while b%8 != 0:
    b=(b*B_FACTOR)%MOD

  #let judge compare
  if a%(1<<16) == b%(1<<16):
    count+=1

  #generate next values
  a=(a*A_FACTOR)%MOD
  b=(b*B_FACTOR)%MOD
print count
