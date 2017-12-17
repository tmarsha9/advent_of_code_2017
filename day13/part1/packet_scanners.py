#!/usr/bin/env python

severity = 0
with open("input.txt", "r") as f:
  for line in f:
    line = line.strip().split(": ")
    depth = int(line[0])
    range = int(line[1])

    if depth%(2*(range-1)) == 0:
      severity+=depth*range
print severity
