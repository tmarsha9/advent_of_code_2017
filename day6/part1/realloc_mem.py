#!/usr/bin/env python

with open("input.txt", "r") as f:
  memory = [int(i) for i in f.readline().split()]

#memory = [0,2,7,0]

configs = set()
configs.add(str(memory))

realloc_count = 0

while True:
  realloc_count+=1
  #print memory #watch mem change over time
  max = 0
  for i in range(1,len(memory)):
    if memory[i] > memory[max]:
      max = i

  val = memory[max]
  memory[max] = 0 #redist max bank

  #spread workload over other banks
  extra_count = 0
  for i in range(max+1,len(memory)+max+1):
    if extra_count < val%len(memory):
      memory[i%len(memory)] += val/len(memory) + 1 #add average plus remainder to locations directly after max
    else:
      #add average to every location
      memory[i%len(memory)] += val/len(memory)
    extra_count+=1

  if str(memory) in configs:
    print realloc_count
    break
  else:
    configs.add(str(memory))
