import itertools
import collections

with open("12/12_input.txt", "r") as f:
  data = [line.strip() for line in f.readlines()]
  
in_region=[] # keep track of what we already have added to a region

def valid_coord(x,y):
  return x>=0 and x<len(data[0]) and y>=0 and y<len(data)
  
dirs_x=[0, 1, 0, -1]
dirs_y=[1, 0, -1, 0]

visited=[]
perimeters=data.copy()

def grow(seed):
  points_to_visit = collections.deque()
  points_to_visit.append(seed)
  x,y=seed
  
  area = 1
  perimeter = 0
  
  code=data[y][x]
  this_region=[]
  this_region.append(seed)
  
  while len(points_to_visit):
    p = points_to_visit.pop()
    x,y=p
    for i in range(len(dirs_x)):
      new_y = y+dirs_y[i]
      new_x = x+dirs_x[i]
      if valid_coord(new_x, new_y) and \
        (new_x, new_y) not in this_region and \
        data[new_y][new_x] == code:
          points_to_visit.append((new_x, new_y))
          area += 1
          this_region.append((new_x, new_y))
          visited.append((new_x, new_y))
      elif (new_x, new_y) not in this_region:
        perimeter += 1
        
  return area*perimeter
  
def build_regions():
  regions=[]
  for y in range(len(data)):
    for x in range(len(data[0])):
      if (x,y) not in visited:
        r = grow((x,y))
        regions.append(r)
        
  return regions

print(sum(build_regions()))