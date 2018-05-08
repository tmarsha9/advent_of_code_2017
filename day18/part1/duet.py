#!/usr/bin/env python

regs = {} #registers a-z
for i in range(26):
  regs[chr(ord('a')+i)] = 0

instructions = []
current_instruction = 0
recovered = 0

#read instructions with minimal processing
with open("input.txt", "r") as f:
  for line in f:
    instructions.append(line.strip().split())

while True:
  items = instructions[current_instruction]
  try:
    items[1] = int(items[1])
  except ValueError as e:
    pass

  try:
    items[2] = int(items[2])
  except (ValueError,IndexError) as e:
    pass


  if items[0] == "snd":
    if isinstance(items[1],str):
      recovered = regs[items[1]]
    else:
      recovered = int(items[1])
  elif items[0] == "set":
    if isinstance(items[2],str):
      regs[items[1]] = regs[items[2]]
    else:
      regs[items[1]] = int(items[2])
  elif items[0] == "add":
    if isinstance(items[2],str):
      regs[items[1]] += regs[items[2]]
    else:
      regs[items[1]] += int(items[2])
  elif items[0] == "mul":
    if isinstance(items[2],str):
      regs[items[1]] *= regs[items[2]]
    else:
      regs[items[1]] *= int(items[2])
  elif items[0] == "mod":
    if isinstance(items[2],str):
      regs[items[1]] %= regs[items[2]]
    else:
      regs[items[1]] %= int(items[2])
  elif items[0] == "rcv":
    if recovered != 0:
      break
  else: #items[0] == jgz
    if isinstance(items[1],str):
      if regs[items[1]] > 0:
        current_instruction += int(items[2])-1
    else:
      if int(items[1]) > 0:
        current_instruction += int(items[2])-1

  current_instruction+=1
  if current_instruction < 0 or current_instruction >= len(instructions):
    print('off end of instructions')
    print(current_instruction)
    break

print(recovered)
