#!/usr/bin/env python

data = []
with open("input.txt", "r") as f:
  for line in f:
    line = line.strip().split(": ")

    data.append((int(line[0]),int(line[1])))

delay = 0
run = True

while run:
  run = False
  for item in data:
    if (item[0]+delay)%(2*(item[1]-1)) == 0:
      delay+=1
      run = True
      break

print delay
