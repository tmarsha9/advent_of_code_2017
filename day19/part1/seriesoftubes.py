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
output = []

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
      #end of path, output characters seen
      break
    else:
      #character on path, add to output
      output.append(data[row][col])
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
      output.append(data[row][col])
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
      output.append(data[row][col])
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
      output.append(data[row][col])
      col += 1

print(''.join(output))
