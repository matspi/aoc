pos = 50
ctr = 0
with open("input_01_1.txt", "r") as input:
    for line in input.readlines():
        d = line[0]
        clicks = int(line[1:])
        if d == "L":
            clicks *= -1

        pos = (pos + clicks) % 100

        if pos == 0:
            ctr += 1


print(ctr)
