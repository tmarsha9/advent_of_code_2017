#!/usr/bin/env python

class Node:
  visited = False

  def __init__(self, name, children=[]):
    self.children = children
    self.name = name

  def get_children(self):
   return self.children

  def add_child(self, child):
    self.children.add(child)

def find_root(graph):
  for n in graph:
    for child in graph[n].children:
      graph[child].visited = True

  for n in graph:
    if not graph[n].visited:
      return n

  return None


nodes = {}

with open("input.txt","r") as f:
  for line in f:
    line = line.split()
    name = line[0]
    if len(line) > 3:
      children = [child.strip() for child in ' '.join(line[3:]).split(',')] #beautiful or an abomination?
      nodes[name] = Node(name,children)
    else:
      nodes[name] = Node(name)

print find_root(nodes)
