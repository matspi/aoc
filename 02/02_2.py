import re


ids = []

with open("input_02_2.txt", "r") as input:
    for line in input.readlines():
        for idline in line.split(","):
            from_ = int(idline.split("-")[0])
            to = int(idline.split("-")[1])

            for id in range(from_, to + 1):
                ids.append(str(id))


REPEATER = re.compile(r"(.+?)\1+$")


def repeated(id):
    match = REPEATER.match(id)
    if match:
        return int(id)
    return 0


sum = 0
for id in ids:
    sum += repeated(id)

print(sum)
