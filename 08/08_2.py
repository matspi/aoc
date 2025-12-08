import math

points = []
with open("input_08_1.txt") as f:
    for line in f.readlines():
        x, y, z = line.strip().split(",")
        points.append((int(x), int(y), int(z)))


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def calc_dists():
    result = []
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[:i]):
            result.append((distance(p1, p2), i, j))

    return result


dists = calc_dists()
dists = sorted(dists)

circuits = []
connections = set()
for _, i, j in dists:
    if i in connections:
        if j in connections:
            circ1 = [c for c in circuits if j in c][0]
            circ2 = [c for c in circuits if i in c][0]

            if circ1 == circ2:
                continue

            circuits.remove(circ1)
            circuits.remove(circ2)

            new_circ = set(circ1)
            new_circ.update(circ2)

            circuits.append(list(new_circ))
        else:
            circ1 = [c for c in circuits if i in c][0]
            circ1.append(j)
    elif j in connections:
        circ1 = [c for c in circuits if j in c][0]
        circ1.append(i)
    else:
        circuits.append([i, j])

    connections.add(i)
    connections.add(j)

    if len(connections) == len(points):
        print(points[i][0] * points[j][0])
