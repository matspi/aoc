
with open("10/10_input.txt", "r") as f:
  data = [[int(i) if i !='.' else 10 for i in line.strip()] for line in f.readlines()]


dirs_x = [0, 1, 0, -1]
dirs_y = [1, 0, -1, 0]

def valid_coords(x, y):
  return y>=0 and y<len(data) and x>=0 and x<len(data[0])

def walk(x, y, current_height):
  if current_height == 9:
    return 1

  num_paths = 0

  for d in range(len(dirs_x)):
    new_x = x+dirs_x[d]
    new_y = y+dirs_y[d]

    if not valid_coords(new_x, new_y):
      continue

    if data[new_y][new_x] != current_height + 1:
      continue

    # else => valid path continuation
    num_paths += walk(new_x, new_y, current_height+1)

  return num_paths

result=0
for y in range(len(data)):
  for x in range(len(data[0])):
    if data[y][x] == 0:
      paths = walk(x, y, 0)

      result+=paths


print(result)