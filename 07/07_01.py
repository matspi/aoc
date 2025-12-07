grid=[]
with open("input_07_1.txt") as f:
    for line in f.readlines():
        grid.append(list(line.strip()))


def start(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                return (r, c)
    return None

r,c = start(grid)
grid[r+1][c] = "|"

split=0
def step(grid, r):
    global split
    row = grid[r]
    for c, d in enumerate(row):
        if d == "|":
            if grid[r+1][c] == ".":
                grid[r+1][c] = "|"
            elif grid[r+1][c] == "^":
                split+=1
                grid[r+1][c-1] = "|"
                grid[r+1][c+1] = "|"
    return grid                

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

for r in range(len(grid)-1):
    grid = step(grid, r)
    print_grid(grid)
   
print(split)   