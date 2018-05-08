#!/usr/bin/env python

data = []
with open("input.txt", "r") as f:
  for line in f:
    data.append(line.strip('\n'))

#find start pos
row = 0
for i in range(len(data[0])):
  if data[0][i] == '|':
    col = i

direction = 'down'
steps = 0

while True:
  if direction == 'down':
    if data[row][col] == '|' or data[row][col] == '-':
      row += 1
    elif data[row][col] == '+':
      #check left and right
      #data is already padded, so col+1 or col-1 exist
      if data[row][col+1] != ' ':
        direction = 'right'
        col += 1
      else:
        direction = 'left'
        col -= 1
    elif data[row][col] == ' ':
      break
    else:
      #character on path, ignore
      row += 1
  elif direction == 'up':
    if data[row][col] == '|' or data[row][col] == '-':
      row -= 1
    elif data[row][col] == '+':
      #check left and right
      if data[row][col+1] != ' ':
        direction = 'right'
        col += 1
      else:
        direction = 'left'
        col -= 1
    elif data[row][col] == ' ':
      break
    else:
      row -= 1
  elif direction == 'left':
    if data[row][col] == '|' or data[row][col] == '-':
      col -= 1
    elif data[row][col] == '+':
      #check up and down
      if data[row+1][col] != ' ':
        direction = 'down'
        row += 1
      else:
        direction = 'up'
        row -= 1
    elif data[row][col] == ' ':
      break
    else:
      col -= 1
  else: #direction == 'right'
    if data[row][col] == '|' or data[row][col] == '-':
      col += 1
    elif data[row][col] == '+':
      #check up and down
      if data[row+1][col] != ' ':
        direction = 'down'
        row += 1
      else:
        direction = 'up'
        row -= 1
    elif data[row][col] == ' ':
      break
    else:
      col += 1

  #increment steps if not done
  steps += 1

print(steps)
