#!/usr/bin/env python

import sys

registers = {}

max_val = 0 #all regs init to 0, so 0 is valid initialization

with open("input.txt","r") as f:
  for line in f:
    line = line.split()

    if line[0] not in registers:
      registers[line[0]] = 0
    if line[4] not in registers:
      registers[line[4]] = 0

    if eval(str(registers[line[4]]) + ' ' + line[5] + ' ' + line[6]):
      if line[1] == 'inc':
        op = '+'
      else:
        op = '-'
      new_val = eval(str(registers[line[0]]) + ' ' + op + ' ' + line[2])
      registers[line[0]]  = new_val
      max_val = max(max_val,new_val)
print max_val
