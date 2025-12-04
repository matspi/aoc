grid = []

with open("input_04_1.txt", "r") as input:
    for line in input.readlines():
        grid.append(list(line.strip()))


def get(grid, y, x):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return "."
    return grid[y][x]


import copy


def remove(grid):
    new_grid = copy.deepcopy(grid)
    sum = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != "@":
                continue
            eight = [
                get(grid, y - 1, x - 1),
                get(grid, y - 1, x),
                get(grid, y - 1, x + 1),
                get(grid, y, x - 1),
                get(grid, y, x + 1),
                get(grid, y + 1, x - 1),
                get(grid, y + 1, x),
                get(grid, y + 1, x + 1),
            ]
            if eight.count("@") < 4:
                new_grid[y][x] = "x"
                sum += 1
    return sum, new_grid


sum = 0
removed, grid = remove(grid)
while removed > 0:
    sum += removed
    removed, grid = remove(grid)

print(sum)
