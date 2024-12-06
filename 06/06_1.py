
data = []
with open("06/06_input.txt", "r") as f:
  for l in f.readlines():
    data.append(list(l.strip()))

dirs_x=[0, 1, 0, -1]
dirs_y=[-1, 0, 1, 0]
dirs = ['^', '>', '<', 'v']

start_y = [i for i in range(len(data)) if data[i].count('^') > 0][0]
start_x = [i for i in range(len(data[start_y])) if data[start_y][i] in dirs][0]
dir = [i for i in range(len(dirs)) if data[start_y][start_x] ==dirs[i]][0]

def next_coords(x,y,dir):
  return x+dirs_x[dir], y+dirs_y[dir]

def coords_in_maze(x,y):
  return x>=0 and x<len(data[0]) and y>=0 and y<len(data)

def walk(x, y, dir):
  data[y][x] = 'X'
  next_x, next_y = next_coords(x,y,dir)
  if coords_in_maze(next_x, next_y):
    if data[next_y][next_x] == '#':
      dir = (dir+1) % 4
      next_x = x
      next_y = y
  
  return next_x, next_y, dir

x=start_x
y=start_y
while coords_in_maze(x, y):
  x,y,dir = walk(x,y,dir)

fields=0
for y in range(len(data)):
  for x in range(len(data[y])):
    fields += data[y][x].count('X')

print(fields)