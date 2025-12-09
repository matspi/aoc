import math

tiles = []
with open("input_09_1.txt") as f:
    for line in f.readlines():
        x, y = line.strip().split(",")
        tiles.append((int(x), int(y)))

areas = []
for i, a in enumerate(tiles):
    for j, b in enumerate(tiles[:i]):
        x = abs(a[0] - b[0]) + 1
        y = abs(a[1] - b[1]) + 1

        areas.append((x * y, i, j))

areas = sorted(areas)

print(areas[-1])
