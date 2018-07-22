#!/usr/bin/env python

class Image:

  def __init__(self,rules):
    self.rules = rules

    #image always starts as follows
    self.image = [
    ['.', '#', '.'],
    ['.', '.', '#'],
    ['#', '#', '#']
    ]
    self.size = 3 #also len(self.image)

  def count_pixels_on(self):
    count = 0

    for i in range(len(self.image)):
      for j in range(len(self.image[i])):
        if self.image[i][j] == '#':
          count += 1
    return count

  def rotate_clockwise(self,image):
    """rotates image clockwise"""
    for i in range(len(image)):
      for j in range(i+1,len(image)):
        image[i][j],image[j][i] = image[j][i],image[i][j]
    self.flip_horizontal(image)

  def flip_horizontal(self,image):
    """flips image horizontally"""
    for i in range(len(image)):
      for j in range(len(image[i])/2):
        image[i][j],image[i][len(image[i])-1-j] = image[i][len(image[i])-1-j],image[i][j]

  def match_to_rule(self,row,col,width,height):
    """
      attempts to match a subimage to any of the rules
      returns what the subimage is replaced with
    """
    subimage = []
    for i in range(row,row+height):
      tmp_row = []
      for j in range(col,col+width):
        tmp_row.append(self.image[i][j])
      subimage.append(tmp_row)

    for i,rule in enumerate(self.rules):
      if len(rule[0]) != len(subimage):
        continue

      if self.is_match(subimage,rule[0]):
        return rule[1]
    print('NO MATCH')
    return None

  def is_match(self,image,rule):
    """determines if the image matches the rule. the rule can be flipped or rotated in any orientation"""

    for i in range(2):
      for i in range(4):
        if image == rule:
          return True
        self.rotate_clockwise(rule)
      self.flip_horizontal(rule)
    return False

  def combine_pieces(self, pieces):
    """
      uses the pieces given to create a new image
    """
    new_image = []

    for i in range(len(pieces)):
      new_rows = [[] for x in range(len(pieces[i][0]))]
      for j in range(len(pieces[i])):
        for k in range(len(pieces[i][j])):
          new_rows[k] += pieces[i][j][k]

      for row in new_rows:
        new_image.append(row)

    self.image = new_image

  def iterate(self):
    new_pieces = []

    if len(self.image) % 2 == 0:
      new_size = self.size + self.size/2
      #break image into 2x2 pieces and match each one to a rule
      for row in range(0,self.size,2):
        tmp_pieces = []
        for col in range(0,self.size,2):
          tmp_pieces.append(self.match_to_rule(row,col,2,2))
        new_pieces.append(tmp_pieces)

    else: #len(self.image) % 3 == 0:
      new_size = self.size + self.size/3
      #break image into 3x3 pieces and match each one to a rule
      #keep track of where each new piece goes in final image
      for row in range(0,self.size,3):
        tmp_pieces = []
        for col in range(0,self.size,3):
          tmp_pieces.append(self.match_to_rule(row,col,3,3))
        new_pieces.append(tmp_pieces)

    self.combine_pieces(new_pieces)
    self.size = new_size

def print_image(image):
  for row in image:
    print(row)

###MAIN###

#read in rules from input.txt
rules = []
with open("input.txt", "r") as f:
  for line in f:
    line = [item.strip().split('/') for item in line.split("=>")]
    for i,row in enumerate(line[0]):
      line[0][i] = list(row)
    for i,row in enumerate(line[1]):
      line[1][i] = list(row)
    rules.append(line)

#create image class and iterate fractal art enhancement process by applying rules
fractal = Image(rules)

for i in range(5): #number of iterations for my problem was 5 iterations
  fractal.iterate()
print(fractal.count_pixels_on())
