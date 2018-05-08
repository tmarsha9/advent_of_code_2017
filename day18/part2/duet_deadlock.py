#!/usr/bin/env python

#Started by Tyler Marshall a while ago
#Finished by Tyler Marshall on 2018-5-7

regs0 = {} #registers a-z for program 0
regs1 = {} #registers a-z for program 1
for i in range(26):
  regs0[chr(ord('a')+i)] = 0
  regs1[chr(ord('a')+i)] = 0
regs0['p'] = 0
regs1['p'] = 1

regs = []
regs.append(regs0)
regs.append(regs1)

buffers = []
buffers.append([])
buffers.append([])

instructions = []
instruction_counters = [0,0]

blocked = [0,0]

program_1_send_count = 0

current_program = 0
other_program = 1

#read instructions with minimal processing
with open("input.txt", "r") as f:
  for line in f:
    instructions.append(line.strip().split())

while True:
  if(blocked[current_program] and blocked[other_program]):
    #both are blocked -> deadlock
    break
  elif blocked[current_program]:
    #if current program is blocked, try to execute the other
    current_program = other_program
    other_program = (other_program+1)%2

  items = instructions[instruction_counters[current_program]]

  #try to convert values to ints
  #if fails, it stays as str
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
      buffers[other_program].append(regs[current_program][items[1]])
      if current_program == 1:
        program_1_send_count += 1
      blocked[other_program] = 0
    else:
      buffers[other_program].append(int(items[1]))
      if current_program == 1:
        program_1_send_count += 1
      blocked[other_program] = 0
  elif items[0] == "set":
    if isinstance(items[2],str):
      regs[current_program][items[1]] = regs[current_program][items[2]]
    else:
      regs[current_program][items[1]] = int(items[2])
  elif items[0] == "add":
    if isinstance(items[2],str):
      regs[current_program][items[1]] += regs[current_program][items[2]]
    else:
      regs[current_program][items[1]] += int(items[2])
  elif items[0] == "mul":
    if isinstance(items[2],str):
      regs[current_program][items[1]] *= regs[items[2]]
    else:
      regs[current_program][items[1]] *= int(items[2])
  elif items[0] == "mod":
    if isinstance(items[2],str):
      regs[current_program][items[1]] %= regs[current_program][items[2]]
    else:
      regs[current_program][items[1]] %= int(items[2])
  elif items[0] == "rcv":
      if isinstance(items[1],str):
        if len(buffers[current_program]) == 0:
          #nothing to receive
          blocked[current_program] = 1
        else:
          regs[current_program][items[1]] = buffers[current_program][0]
          if len(buffers[current_program]) > 1:
            buffers[current_program] = buffers[current_program][1:]
          else:
            buffers[current_program] = []
      else:
        print("[ERROR]: Cannot receive on an integer value. Stopping...")
        break
  else: #items[0] == jgz
    if isinstance(items[1],str):
      if regs[current_program][items[1]] > 0:
        if isinstance(items[2],str):
          instruction_counters[current_program] += regs[current_program][items[2]]-1
        else:
          instruction_counters[current_program] += int(items[2])-1
    else:
      if int(items[1]) > 0:
        if isinstance(items[2],str):
          instruction_counters[current_program] += regs[current_program][items[2]]-1
        else:
          instruction_counters[current_program] += int(items[2])-1

  #make sure to try rcv again in case data gets put into buffer
  #only move to next instruction if we didn't block on this one
  if blocked[current_program] == 0:
    instruction_counters[current_program] += 1

  if instruction_counters[current_program] < 0 or instruction_counters[current_program] >= len(instructions):
    print('off end of instructions')
    print(current_instruction)
    break

print(program_1_send_count)
