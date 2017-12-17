#!/usr/bin/env python

with open("input.txt","r") as f:
  dance_moves = f.readline().strip().split(',')

programs = [chr(i+ord('a')) for i in range(16)]
cycle = 0
past = []

for i in xrange(1000000000):
  if ''.join(programs) in past: #if we found an item that we've seen before, cycle detected
    print(past[1000000000%i]) #cycle length is i
    break

  past.append(''.join(programs))

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
