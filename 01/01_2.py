ids = []

with open("input_02_1.txt", "r") as input:
    for line in input.readlines():
        for idline in line.split(","):
            for from_, to in idline.split("-")[:2]:
                ids.append((from_, to))

        clicks = int(line[1:])
        if d == "L":
            clicks *= -1

        new_pos = pos + clicks

        if clicks > 0:
            ctr += new_pos // 100 - pos // 100
        else:
            ctr += (pos - 1) // 100 - (new_pos - 1) // 100

        pos = new_pos % 100


print(ctr)
