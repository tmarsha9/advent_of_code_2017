#!/usr/bin/env python

with open("input.txt","r") as f:
  steps = f.readline().strip().split(",")

x = 0
y = 0
z = 0

for step in steps:
  if step == "nw":
    x-=1
    y+=1
  elif step == "n":
    y+=1
    z-=1
  elif step == "ne":
    x+=1
    z-=1
  elif step == "sw":
    x-=1
    z+=1
  elif step == "s":
    y-=1
    z+=1
  else: #step == "se":
    x+=1
    y-=1
print max(abs(x),abs(y),abs(z))
