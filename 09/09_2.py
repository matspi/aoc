import shapely

tiles = []

with open("input_09_1.txt") as f:
    for line in f.readlines():
        x, y = line.strip().split(",")
        tiles.append((int(x), int(y)))

polygon = shapely.Polygon(tiles)

areas = []
for i, a in enumerate(tiles):
    for j, b in enumerate(tiles[:i]):
        x = abs(a[0] - b[0]) + 1
        y = abs(a[1] - b[1]) + 1

        A = (a[0], a[1])
        B = (a[0], b[1])
        C = (b[0], b[1])
        D = (b[0], a[1])

        rect = shapely.Polygon((A, B, C, D))

        if polygon.contains(rect):
            areas.append((x * y, i, j))

areas = sorted(areas)

print(areas[-1])
