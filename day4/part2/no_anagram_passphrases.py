#!/usr/bin/env python

f = open("input.txt", "r")

num_valid = 0
for line in f:
  processed = []
  all_items = line.split()

  bad = False
  for item in all_items:
    item = set(list(item))
    if item in processed:
      bad = True
      break
    else:
      processed.append(item)
  if not bad:
    num_valid+=1
print num_valid
