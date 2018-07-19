#!/usr/bin/env python

import sys

#all particles will eventually move away from origin
#all that matters is which particle has the lowest acceleration
  #if tie, then lowest velocity
  #if tie, then 

def get_pos_manhattan(particle):
  return abs(particle[0]) + abs(particle[1]) + abs(particle[2])

def get_vel_manhattan(particle):
  return abs(particle[3]) + abs(particle[4]) + abs(particle[5])

def get_acc_manhattan(particle):
  return abs(particle[6]) + abs(particle[7]) + abs(particle[8])

particles = []
id = -1
with open("input.txt", "r") as f:
  for line in f:
    px =0
    py =0
    pz =0
    vx =0
    vy =0
    vz =0
    ax =0
    ay =0
    az =0
    id += 1

    pos_end = line.find('>')+1
    position = line[3:pos_end-1]

    vel_end = line.find('>',pos_end)+1
    velocity = line[pos_end+5:vel_end-1]

    acc_end = line.find('>',vel_end)+1
    acceleration = line[vel_end+5:acc_end-1]


    px,py,pz = [int(x) for x in     position.split(',')]
    vx,vy,vz = [int(x) for x in     velocity.split(',')]
    ax,ay,az = [int(x) for x in acceleration.split(',')]

    particles.append((px,py,pz,vx,vy,vz,ax,ay,az,id))

min_acc = get_acc_manhattan(particles[0])
min_particles = [particles[0]]

for i in range(1,len(particles)):
  particle = particles[i]

  if get_acc_manhattan(particle) < min_acc:
    min_particles = [particle]
    min_acc = get_acc_manhattan(particle)
  elif get_acc_manhattan(particle) == min_acc:
    min_particles.append(particle)

if len(min_particles) == 1:
  print(min_particles[0][9])
  sys.exit(0)

particles = min_particles
min_vel = get_vel_manhattan(particles[0])
min_particles = [particles[0]]
for i in range(1,len(particles)):
  particle = particles[i]

  if get_vel_manhattan(particle) < min_vel:
    min_vel = get_vel_manhattan(particle)
    min_particles = [particle]
  elif get_vel_manhattan(particle) == min_vel:
    min_particles.append(particle)

if len(min_particles) == 1:
  print(min_particles[0][9])
  sys.exit(0)

print("Unfinished code! More work needed to compute answer!")
