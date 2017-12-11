#!/usr/bin/env python

f = open("input.txt", "r")

instructions = []

for item in f:
  instructions.append(int(item))

current_instruction = 0
instruction_count = 0

while True:
  try:
    next_instruction = current_instruction+instructions[current_instruction]
    if instructions[current_instruction] >= 3:
      instructions[current_instruction]-=1
    else:
      instructions[current_instruction]+=1
    current_instruction = next_instruction
    instruction_count+=1
  except IndexError:
    print instruction_count
    break
