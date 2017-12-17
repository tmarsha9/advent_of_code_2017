#!/usr/bin/env python

class Node:
  def __init__(self,id):
    self.id = id
    self.group = -1
    self.edges = set()

class Graph:
  nodes = {}
  def __init__(self,nodes=[],edges=[]):
    for node in nodes:
      add_node(node)
    for edge in edges:
      add_edge(edge)

  def add_node(self,id):
    if id not in self.nodes:
      self.nodes[id] = Node(id)
  
  def add_edge(self,edge):
    self.nodes[edge[0]].edges.add(self.nodes[edge[1]])
    self.nodes[edge[1]].edges.add(self.nodes[edge[0]])

g = Graph()

with open("input.txt","r") as f:
  for line in f:
    line = line.split()
    g.add_node(line[0])
    edges = [(line[0],e.strip(',')) for e in line[2:]]
    for edge in edges:
      g.add_node(edge[1])
      g.add_edge(edge)

group = 0

while len(g.nodes)>0:
  queue = [g.nodes[g.nodes.keys()[0]]]

  while len(queue)>0:
    n = queue.pop(0)
    if n.group == -1:
      n.group = group
      for edge in n.edges:
        if edge not in queue:
          queue.append(edge)
      del g.nodes[n.id]
  group+=1
print group
