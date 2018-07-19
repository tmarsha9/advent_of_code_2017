#!/usr/bin/env python

import sys
from math import sqrt

#simulate particle movement until collisions can be guaranteed to no longer occur
#one way of doing this is by keeping track of the distance between particles every step
 #whenever there is a step whree the distances only increase, no more collisions can occur because the particles never change direction

def get_pos(particle):
  return (particle[0],particle[1],particle[2])

def get_vel(particle):
  return (particle[3],particle[4],particle[5])

def get_acc(particle):
  return (particle[6],particle[7],particle[8])

def get_distance(p1, p2):
  p1pos = get_pos(p1)
  p2pos = get_pos(p2)
  return sqrt((p1pos[0]-p2pos[0])**2 + (p1pos[1]-p2pos[1])**2 + (p1pos[2]-p2pos[2])**2)

def add_acc_to_vec(particle):
  return (particle[0], particle[1], particle[2], particle[3]+particle[6], particle[4]+particle[7], particle[5]+particle[8], particle[6], particle[7], particle[8], particle[9], particle[10])

def add_vec_to_pos(particle):
  return (particle[0]+particle[3], particle[1]+particle[4], particle[2]+particle[5], particle[3], particle[4], particle[5], particle[6], particle[7], particle[8], particle[9], particle[10])

def kill_particle(particle):
  return (particle[0], particle[1], particle[2], particle[3], particle[4], particle[5], particle[6], particle[7], particle[8], particle[9], False)

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

    particles.append((px,py,pz,vx,vy,vz,ax,ay,az,id,True)) #last field says if the particle is alive or not

collision_count = 0
distances = [] #square matrix. could be optimized to lower triangular if needed
for i in range(len(particles)):
  distances.append([sys.maxint] * len(particles))


run = True
while run:
  run = False

  destroy_us = [] #locations where collisions have occured

  #check distance between every pair of nodes to see if it has increased or decreased
  for p1 in range(len(particles)):
    if not particles[p1][10]:
      continue
    for p2 in range(len(particles)):
      if p1==p2 or not particles[p2][10]:
        continue
      new_distance = get_distance(particles[p1],particles[p2])
      #if any distances have decreased, make sure to continue this process
      if new_distance < distances[p1][p2]:
        run = True
      distances[p1][p2] = new_distance

      #if the distance between two particles is 0, mark this location to have all particles destroyed
      #multiple particles could collide at the same point at the same time
      if new_distance == 0:
        if get_pos(particles[p1]) not in destroy_us:
          destroy_us.append(get_pos(particles[p1]))


  #after all distances have been checked, go ahead and destroy any particles that collided
  for p in range(len(particles)):
    if get_pos(particles[p]) in destroy_us:
      particles[p] = kill_particle(particles[p])
      collision_count += 1

    #and step the simulation by one
    if particles[p][10]:
      particles[p] = add_acc_to_vec(particles[p])
      particles[p] = add_vec_to_pos(particles[p])

#no particles are moving towards each other anymore
#number of particles left is total minus the number destroyed in collisions
print(len(particles)-collision_count)
