

dirs_x=[0, 1, 0, -1]
dirs_y=[-1, 0, 1, 0]
dirs = ['^', '>', '<', 'v']

def get_data():
  data = []
  with open("06/06_input.txt", "r") as f:
    for l in f.readlines():
      data.append(list(l.strip()))
  return data


def next_coords(x,y,d):
  return x+dirs_x[d], y+dirs_y[d]

def coords_in_maze(x,y, data):
  return x>=0 and x<len(data[0]) and y>=0 and y<len(data)


def walk(x, y, d, data):
  data[y][x] = 'X'
  next_x, next_y = next_coords(x,y,d)
  if coords_in_maze(next_x, next_y, data):
    if data[next_y][next_x] == '#':
      d = (d+1) % 4
      next_x = x
      next_y = y
  
  return next_x, next_y, d

def do_walk(start_x, start_y, start_dir, data):
  x=start_x
  y=start_y
  d = start_dir
  seen=[]
  while coords_in_maze(x, y, data):
    if seen.count((x,y,d)) > 0:
      return True
    seen.append((x,y,d))
    x,y,d = walk(x,y,d, data)

  return False


def main():


  input = get_data()


  start_y = [i for i in range(len(input)) if input[i].count('^') > 0][0]
  start_x = [i for i in range(len(input[start_y])) if input[start_y][i] in dirs][0]
  dir = [i for i in range(len(dirs)) if input[start_y][start_x] ==dirs[i]][0]




  do_walk(start_x, start_y, dir, input)

  orig_data = get_data()
  obstacles=0



  coords = [(x,y) for y in range(len(input)) for x in range(len(input[y])) if input[y][x] == 'X' and not (orig_data[y][x] in dirs)]



  from multiprocessing import Pool

  with Pool(16) as p:
    results = p.map(check_obstacle, coords)

  print(sum(results))

def check_obstacle(inp):
  x,y=inp
  data = get_data()
  start_y = [i for i in range(len(data)) if data[i].count('^') > 0][0]
  start_x = [i for i in range(len(data[start_y])) if data[start_y][i] in dirs][0]
  d = [i for i in range(len(dirs)) if data[start_y][start_x] ==dirs[i]][0]

  data[y][x] = '#'
  if do_walk(start_x, start_y, d, data):
    return 1
  return 0

# for y in range(len(input)):
#   for x in range(len(input[y])):
#     if input[y][x] == 'X' and not (orig_data[y][x] in dirs):
#       data = get_data()
#       data[y][x] = '#'
#       if do_walk(start_x, start_y, dir, data):
#         obstacles += 1

# print(obstacles)


if __name__ == "__main__":
    main()