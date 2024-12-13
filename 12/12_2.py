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

def count_sides(fences):
  sides = 0
  
  while len(fences) > 0:
    f = fences[0]
    del(fences[0])
    sides += 1
    x,y=f[0]
    direction = f[1]
   
    if direction in [0, 2]:
      dirs = [1,3]
    else:
        dirs = [0,2]
    
    for d in dirs:
      new_x=x
      new_y=y
      
      while True:
        new_y = new_y+dirs_y[d]
        new_x = new_x+dirs_x[d]
        
        t=((new_x, new_y), direction)
        
        if t in fences:
          fences.remove(t)
        else:
          break

      
  return sides

def grow(seed):
  points_to_visit = collections.deque()
  points_to_visit.append(seed)
  x,y=seed
  
  area = 1
  fences = []
  
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
        fences.append(((x,y), i))
        
  s = count_sides(fences)
        
  return area*s
  
def build_regions():
  regions=[]
  for y in range(len(data)):
    for x in range(len(data[0])):
      if (x,y) not in visited:
        r = grow((x,y))
        regions.append(r)
        
  return regions

print(sum(build_regions()))