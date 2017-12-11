#!/usr/bin/env python

class Node:
  visited = False

  def __init__(self, name, weight, children=[]):
    self.children = children
    self.name = name
    self.weight = weight

  def get_children(self):
   return self.children

  def add_child(self, child):
    self.children.add(child)

def find_root(graph):
  for n in graph:
    for child in graph[n].children:
      graph[child].visited = True

  rv = None
  #reset visited for other functions
  for n in graph:
    if not graph[n].visited:
      rv = n
    graph[n].visited = False

  return rv

def get_weight(name, graph):
  sum = 0

  n = graph[name]

  if len(n.children) == 0:
    return n.weight
  else:
    for child in n.children:
      sum += get_weight(child,graph)
    return n.weight + sum

def check_weight(name, graph):
  n = graph[name]

  rv = (True,None,None)

  if len(n.children) == 0:
    return rv
  else:
    weights = [ (get_weight(child,graph),child) for child in n.children]

    for i in range(len(weights)):
      if weights[i][0] != weights[i-1][0]:
        if weights[i][0] != weights[(i+1)%len(weights)][0]:
          good = weights[i-1]
          bad  = weights[i]
        else:
          good = weights[i]
          bad  = weights[i-1]
        rv = (False,good,bad)
        break

  return rv

nodes = {}

with open("input.txt","r") as f:
  for line in f:
    line = line.split()
    name = line[0]
    weight = int(line[1].strip('()'))
    if len(line) > 3:
      children = [child.strip() for child in ' '.join(line[3:]).split(',')] #beautiful or an abomination?
      nodes[name] = Node(name,weight,children)
    else:
      nodes[name] = Node(name,weight)

root = find_root(nodes)

to_check = [root]
while True:
  n = to_check[0]
  to_check = to_check[1:]

  ok,good,bad = check_weight(n,nodes)
  if ok:
    for child in nodes[n].children:
      to_check.append(child)
  else:
    print good[0]-bad[0]+nodes[bad[1]].weight
    break
