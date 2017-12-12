#!/usr/bin/env python

import sys

registers = {}

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
      registers[line[0]] = eval(str(registers[line[0]]) + ' ' + op + ' ' + line[2])
print max(registers.values())
