ingreds = []
ranges = []
with open("input_05_1.txt", "r") as input:
    read_ranges = True
    for line in input.readlines():
        if line.strip() == "":
            read_ranges = False
            continue

        if read_ranges:
            ranges.append([int(i) for i in line.strip().split("-")])
        else:
            ingreds.append(int(line.strip()))


def in_range(ranges, i):
    for r in ranges:
        if i >= r[0] and i <= r[1]:
            return True
    return False


cnt = [in_range(ranges, i) for i in ingreds].count(True)

print(cnt)
