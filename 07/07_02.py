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
rows, cols = len(grid), len(grid[0])
counts = [[0]*cols for i in range(rows)]

def dfs(c,r):
    if counts[r][c]:
        return counts[r][c]

    # descend
    while r < rows and grid[r][c] != "^":
        r += 1

    if r == rows:
        return 1

    if counts[r][c]:
        return counts[r][c]

    if c > 0: # left edge
        counts[r][c] += dfs(c-1, r)
    if c < cols-1: # right edge
        counts[r][c] += dfs(c+1, r)

    return counts[r][c]        

s_count = dfs(c, r)

#print(counts)        

print(s_count)