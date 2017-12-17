#!/usr/bin/env python

with open("input.txt","r") as f:
  dance_moves = f.readline().strip().split(',')

programs = [chr(i+ord('a')) for i in range(16)]

for dance_move in dance_moves:
  if dance_move[0] == 's':
    #spin
    amount = int(dance_move[1:])
    programs = programs[-amount:] + programs[:-amount]
  elif dance_move[0] == 'x':
    #exchange
    pos1 = int(dance_move[1:].split('/')[0])
    pos2 = int(dance_move[1:].split('/')[1])
    programs[pos1],programs[pos2] = programs[pos2],programs[pos1]
  elif dance_move[0] == 'p':
    #partner
    p1 = programs.index(dance_move[1:].split('/')[0])
    p2 = programs.index(dance_move[1:].split('/')[1])
    programs[p1],programs[p2] = programs[p2],programs[p1]
print ''.join(programs)
