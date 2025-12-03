sum = 0

with open("input_03_1.txt", "r") as input:

    for line in input.readlines():
        line = line.strip()
        f = 0
        for i, c in enumerate(line[:-1]):
            f = max(f, int(c))
        s = 0
        for j, c in enumerate(line[line.index(str(f)) + 1 :]):
            s = max(s, int(c))

        sum += f * 10 + s

print(sum)
