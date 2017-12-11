#!/usr/bin/env python

import sys

def usage_and_exit():
  print 'usage: {} value'.format(sys.argv[0])
  sys.exit(1)

def access_grid(x,y,grid):
  try:
    return grid[(x,y)]
  except KeyError:
    return 0

#input for my test = 312051
if len(sys.argv) != 2:
  usage_and_exit()

try:
  input = int(sys.argv[1])
except ValueError:
  usage_and_exit()

if input <= 0:
  usage_and_exit()

square = 1



layer = 0 #how far out from the center
x = 0
y = 0

grid = {}       #key is (x,y) coordinate, val is sum at that location
grid[(x,y)] = 1
print '{}: {}'.format((x,y),access_grid(x,y,grid))

while True:
  layer+=1
  y = 1-layer
  x = layer

  #compute right side of square
  for i in range(2*layer-1):
    square+=1

    sum  = access_grid( x+1,   y, grid )
    sum += access_grid( x+1, y+1, grid )
    sum += access_grid(   x, y+1, grid )
    sum += access_grid( x-1, y+1, grid )
    sum += access_grid( x-1,   y, grid )
    sum += access_grid( x-1, y-1, grid )
    sum += access_grid(   x, y-1, grid )
    sum += access_grid( x+1, y-1, grid )

    if sum > input:
      print 'first value larger than {}: {}\nsquare: {}'.format(input,sum,square)
      sys.exit(0)

    grid[(x,y)] = sum
    print '{}: {}'.format((x,y),sum)
    y+=1

  #compute top of square
  for i in range(2*layer):
    square+=1

    sum  = access_grid( x+1,   y, grid )
    sum += access_grid( x+1, y+1, grid )
    sum += access_grid(   x, y+1, grid )
    sum += access_grid( x-1, y+1, grid )
    sum += access_grid( x-1,   y, grid )
    sum += access_grid( x-1, y-1, grid )
    sum += access_grid(   x, y-1, grid )
    sum += access_grid( x+1, y-1, grid )

    if sum > input:
      print 'first value larger than {}: {}\nsquare: {}'.format(input,sum,square)
      sys.exit(0)

    grid[(x,y)] = sum
    print '{}: {}'.format((x,y),sum)
    x-=1

  #compute left side of square
  for i in range(2*layer):
    square+=1

    sum  = access_grid( x+1,   y, grid )
    sum += access_grid( x+1, y+1, grid )
    sum += access_grid(   x, y+1, grid )
    sum += access_grid( x-1, y+1, grid )
    sum += access_grid( x-1,   y, grid )
    sum += access_grid( x-1, y-1, grid )
    sum += access_grid(   x, y-1, grid )
    sum += access_grid( x+1, y-1, grid )

    if sum > input:
      print 'first value larger than {}: {}\nsquare: {}'.format(input,sum,square)
      sys.exit(0)

    grid[(x,y)] = sum
    print '{}: {}'.format((x,y),sum)
    y-=1

  #compute bottom of square
  for i in range(2*layer+1):
    square+=1

    sum  = access_grid( x+1,   y, grid )
    sum += access_grid( x+1, y+1, grid )
    sum += access_grid(   x, y+1, grid )
    sum += access_grid( x-1, y+1, grid )
    sum += access_grid( x-1,   y, grid )
    sum += access_grid( x-1, y-1, grid )
    sum += access_grid(   x, y-1, grid )
    sum += access_grid( x+1, y-1, grid )

    if sum > input:
      print 'first value larger than {}: {}\nsquare: {}'.format(input,sum,square)
      sys.exit(0)

    grid[(x,y)] = sum
    print '{}: {}'.format((x,y),sum)
    x+=1
